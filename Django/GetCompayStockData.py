import pandas
import requests
import io
import bs4
import re


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ssStock.settings")


import django
django.setup()

from CompanyStockData.models import CompanyStockData
class GetCompanyStockData:
    __URL     = 'https://finance.naver.com/item/sise_day.nhn?code='
    __HEADER = { 'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\Safari/537.36') }
    
    def __init__(self,stockCode):
        self.stockCode = stockCode
        self.lastPageNum = 0
        self.get_last_page_number()
        self.get_stock_data_with_data_frame()
    
    
    def get_last_page_number(self):
        # request first html for getting end page
        targetUrl = GetCompanyStockData.__URL+self.stockCode + '&page=1'
        res = requests.get(targetUrl,headers = GetCompanyStockData.__HEADER)
        bs4Obj = bs4.BeautifulSoup(res.text,'html.parser')
        # find last page number attr is 'pgRR'
        pageNation = bs4Obj.find('td',class_='pgRR')
        try:
            lastPageURL = pageNation.find('a')['href']
        except:
            lastPageURL = GetCompanyStockData.__URL+self.stockCode + '&page=2'
        lastPageNumReg = re.split('page=',lastPageURL)
        lastPageNum = lastPageNumReg[1]
        self.lastPageNum = str(lastPageNum)
        self.lastPageNum = int(self.lastPageNum)
        
    def get_stock_data_with_data_frame(self):
        for i in range(0,self.lastPageNum):
            pageNum = i+1
            targetUrl = GetCompanyStockData.__URL + self.stockCode + '&page=' + str(pageNum)
            res = requests.get(targetUrl,headers = GetCompanyStockData.__HEADER)
            tempDataFrameList = pandas.read_html(res.text)
            tempDataFrame = tempDataFrameList[0] #Naver stock has 2table, one is stock data other one is pagenation table
            tempDataFrame = tempDataFrame.dropna() #drop 'na' data
            for i in tempDataFrame.index:
                CompanyStockData(companyStockCode = self.stockCode,\
                companyStockDate = tempDataFrame.loc[i,"날짜"],\
                companyStockEndPrice = tempDataFrame.loc[i,'종가'],\
                companyStockStartPrice = tempDataFrame.loc[i,'시가'],\
                companyStockLowPrice = tempDataFrame.loc[i,'저가'],\
                companyStockHighPrice = tempDataFrame.loc[i,'고가'],\
                companyStockQuantity = tempDataFrame.loc[i,'거래량']).save()
            
if __name__ == '__main__':
    parsedData = GetCompanyStockData('318010')