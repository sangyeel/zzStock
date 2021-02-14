from django.db import models

# Create your models here.
class CompanyFinData(models.Model):
    companyName = models.CharField(max_length=200)
    companyFinYear = models.CharField(max_length=200)
    companyStockCode = models.CharField(primary_key=True,max_length=200)
    companyTotalAssets = models.CharField(max_length=200)
    companyTotalDebt = models.CharField(max_length=200)
    comapnyTotalCapital = models.CharField(max_length=200)
    companyTotalSales = models.CharField(max_length=200)
    companyTotalBuzProfits = models.CharField(max_length=200)
    companyTotalIncomeBeforeTax = models.CharField(max_length=200)
    companyTotalNetIncome = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.companyName