from django.db import models

# Create your models here.
class CompanyData(models.Model):
    companyName = models.CharField(max_length=200)
    companyStockCode = models.CharField(primary_key=True,max_length=200)
    companyBuz = models.TextField()
    companyProd = models.TextField()
    companyListStartDate = models.CharField(max_length=200)
    companyCEO = models.CharField(max_length=200)
    companySite = models.CharField(max_length=200)
    companyLocal = models.CharField(max_length=200)
    
    def __str__(self):
        return self.companyName