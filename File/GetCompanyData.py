import pandas
import requests
'''
https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage 홈페이지로 접속
Excel 버튼을 누를떄 chrom http trace를 이용해서 post 정보를을 캡쳐
해당 URL을 아래 __URL에 저장.
상장사 전체 회사 정보를 받아오는 함수
'''

class GetCompanyData:
    __URL  = ('http://kind.krx.co.kr/corpgeneral/corpList.do?'+
    'beginIndex=&'+
    'comAbbrv=&'+
    'comAbbrvTmp=&'+
    'currentPageSize=5000&'+
    'fiscalYearEnd=all&'+
    'marketType=&'+
    'method=download&'+
    'orderMode=3&'+
    'orderStat=D&'+
    'pageIndex=1&'+
    'repIsuSrtCd:&'+
    'searchCodeType:&'+
    'searchType=13')
    
    def __init__(self):
        
        res = requests.get(GetCompanyData.__URL)
        #pandas read_html return list of datafram even if there are only one tr/td, 
        #res data is looks like a HTML.
        companyDataList = pandas.read_html(res.text,converters={'종목코드': str})
        self.stockInfoDf = companyDataList[0] #Df is datafram
        
        for i in self.stockInfoDf.index:
            print(self.stockInfoDf.loc[i, '회사명'],\
                self.stockInfoDf.loc[i, '종목코드'],\
                self.stockInfoDf.loc[i, '업종'],\
                self.stockInfoDf.loc[i, '주요제품'],\
                self.stockInfoDf.loc[i, '상장일'],\
                self.stockInfoDf.loc[i, '대표자명'],\
                self.stockInfoDf.loc[i, '홈페이지'],\
                self.stockInfoDf.loc[i, '지역'])
                        
if __name__ == '__main__':
    parsedData = GetCompanyData()