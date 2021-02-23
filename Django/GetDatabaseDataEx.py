import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ssStock.settings")


import django
django.setup()

from CompanyData.models import CompanyData #This line should be under upper Django Setup line
from GetCompanyFinData import GetCompanyFinData

def getComanyDataFromDB():
    tempCompanyDataSet = CompanyData.objects.all()
    for tempCompanyStockCode in tempCompanyDataSet:
        savedData = GetCompanyFinData(tempCompanyStockCode)
        

def findCompanyDataFromDB(companyName):
    foundCompanyData = CompanyData.objects.filter(companyName = companyName)
    print(foundCompanyData)
    
def GetCompanyDataFromDB(companyName):
    foundCompanyStockCode = CompanyData.objects.get(companyName = companyName)
    print(foundCompanyStockCode)
    
    
if __name__ == '__main__':
    getComanyDataFromDB()
    