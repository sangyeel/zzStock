from django.db import models

# Create your models here.
#date,end_price,price_change,start_price,high,low,quantity
#Django does not support the composite key, Just use the ID as PK
class CompanyStockData(models.Model):
    companyStockCode = models.CharField(max_length=200)
    companyStockDate = models.CharField(max_length=200)
    companyStockEndPrice = models.CharField(max_length=200)
    companyStockStartPrice = models.CharField(max_length=200)
    companyStockLowPrice = models.CharField(max_length=200)
    companyStockHighPrice = models.CharField(max_length=200)
    companyStockQuantity = models.CharField(max_length=200)
    
    def __str__(self):
        return self.companyStockCode