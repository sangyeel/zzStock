import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ssStock.settings")
import re

import django
django.setup()

from CompanyData.models import CompanyData #This line should be under upper Django Setup line
from GetCompanyFinData import GetCompanyFinData
from CompanyDataFromKrx.models import CompanyDataFromKrx
from CompanyData.models import CompanyData
from GetCompanyTodayStockData import GetCompanyTodayStockData
import pandas as pd

def getComanyFinDataFromDB():
    tempCompanyDataSet = CompanyData.objects.all()
    totalCompanyDataCnt = CompanyData.objects.count()
    currentIndex = 0;
    for tempCompanyData in tempCompanyDataSet:
        currentIndex = currentIndex + 1
        tempCompanyStockCode = str(tempCompanyData)
        savedData = GetCompanyFinData(tempCompanyStockCode)
        print("%d / %d" %(currentIndex,totalCompanyDataCnt))

def findCompanyDataFromDB(companyName):
    foundCompanyData = CompanyData.objects.filter(companyName = companyName)
    print(foundCompanyData)
    
def GetCompanyDataFromDB(companyName):
    foundCompanyStockCode = CompanyData.objects.get(companyName = companyName)
    print(foundCompanyStockCode)
    
def GetTodayStockTotal():
    tempCompanyDataSet = CompanyDataFromKrx.objects.all()
    totalCompanyDataCnt = CompanyDataFromKrx.objects.count()
    currentIndex = 0;
    curCompanyDf = pd.DataFrame(columns=['companyName', 'stockTotalSize'])
    for tempCompanyData in tempCompanyDataSet:
        try:
            print('start')
            curCompany = CompanyData.objects.get(companyStockCode = tempCompanyData.companyStockCode)
            curCompanyTodayStockInfo = GetCompanyTodayStockData(tempCompanyData.companyStockCode)
            curComanyStockTotalSize = int(curCompanyTodayStockInfo.todayStockPrice) * int(tempCompanyData.companyStockTotal)
            curCompanyDf.loc[currentIndex] = [curCompany.companyName,curComanyStockTotalSize]
            currentIndex = currentIndex + 1
            print("%d / %d" %(currentIndex,totalCompanyDataCnt))
        except Exception as e:
            print(e)
            print(tempCompanyData.companyStockCode)#우선주들은 여기서 이미 다 빠짐 company 정보가 없어서..
    
    print(curCompanyDf)
if __name__ == '__main__':
    GetTodayStockTotal()
    