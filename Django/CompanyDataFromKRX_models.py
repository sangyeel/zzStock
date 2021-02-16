from django.db import models

# Create your models here.
class CompanyDataFromKrx(models.Model):
    companyStockCode = models.CharField(primary_key=True,max_length=200)
    companyStockMarket = models.CharField(max_length=200)#KOSPI,KOSDAQ
    companyStockFaceValue = models.CharField(max_length=200)
    companyStockTotal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.companyStockCode