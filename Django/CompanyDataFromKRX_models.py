표준코드,단축코드,한글 종목명,한글 종목약명,영문 종목명,상장일,시장구분,증권구분,소속부,주식종류,액면가,상장주식수
from django.db import models

# Create your models here.
class CompanyDataFromKRX(models.Model):
    companyStandardCode = models.CharField(max_length=200)
    companyStockCode = models.CharField(primary_key=True,max_length=200)
    companyStockKind = models.CharField(max_length=200)#보통주,우선주
    companyStockMarket = models.CharField(max_length=200)#KOSPI,KOSDAQ
    companyStockFaceValue = models.CharField(max_length=200)
    companyStockTotal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.companyStockCode