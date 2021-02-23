import pandas
import requests
import io
import bs4
import re


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ssStock.settings")


import django
django.setup()
class GetCompanyTodayStockData:
    __URL     = 'https://finance.naver.com/item/sise_day.nhn?code='
    __HEADER = { 'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\Safari/537.36') }
    
    def __init__(self,stockCode):
        self.stockCode = stockCode
        self.get_today_stock_data()
    
    def get_today_stock_data(self):
        targetUrl = GetCompanyTodayStockData.__URL + self.stockCode + '&page=1'
        res = requests.get(targetUrl,headers = GetCompanyTodayStockData.__HEADER)
        tempDataFrameList = pandas.read_html(res.text)
        tempDataFrame = tempDataFrameList[0] #Naver stock has 2table, one is stock data other one is pagenation table
        tempDataFrame = tempDataFrame.dropna() #drop 'na' data
        print(tempDataFrame.loc[1,"종가"])
        
if __name__ == '__main__':
    GetCompanyTodayStockData('005930')