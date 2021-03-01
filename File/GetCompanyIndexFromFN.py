import requests
import bs4
import re
import os
import pandas
from enum import Enum, auto

class TableInfo(Enum):
    BASIC_INFO = 0
    SHORT_FIN = 1
    SEC_KEEP_INFO = 2
    MAIN_STOCK_HOLDER = 3
    MAIN_STOCK_HOLDER_CHANGE = 4
    BOND_RANK_BEFORE_YEAR = 5
    BOND_RANK_THIS_YEAR = 6
    INVESTING_OPNION = 7
    COM_VAL_CONSIDATION_INDEX = 8
    COM_VAL_SEPERATE_INDEX = 9
    TOTAL_FIN = 10

class GetCompanyIndexFromFN:
    
    __URL     = 'http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A'
    
    def __init__(self,stockCode):
        self.stockCode = stockCode
        self.url = GetCompanyIndexFromFN.__URL + str(stockCode)
        self.companySize = 0
        self.roe = 0
        self.per = 0
        self.delv = 0
        self.beta = 0
        self.getCompanyIndex()
        
    def getCompanyIndex(self):
        res = requests.get(self.url)
        rawHtmlList = pandas.read_html(res.text)
        print(rawHtmlList[TableInfo.COM_VAL_CONSIDATION_INDEX.value])
        self.companySize = rawHtmlList[TableInfo.COM_VAL_CONSIDATION_INDEX.value].iloc[0,1]
        self.per = rawHtmlList[TableInfo.COM_VAL_CONSIDATION_INDEX.value].iloc[4,1]
        self.roe = rawHtmlList[TableInfo.COM_VAL_CONSIDATION_INDEX.value].iloc[6,1]
        self.delv = rawHtmlList[TableInfo.COM_VAL_CONSIDATION_INDEX.value].iloc[7,1]
        self.beta = rawHtmlList[TableInfo.COM_VAL_CONSIDATION_INDEX.value].iloc[8,1]
        
        
        
if __name__ == '__main__':
    SH = GetCompanyIndexFromFN('055550')
    print(SH.companySize)
    print(SH.per)
    print(SH.roe)
    print(SH.delv)
    print(SH.beta)
        
        