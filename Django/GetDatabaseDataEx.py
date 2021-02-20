import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ssStock.settings")


import django
django.setup()

from CompanyData.models import CompanyData #This line should be under upper Django Setup line

def getComanyDataFromDB():
    tempCompanyData = CompanyData.objects.all()
    print(type(tempCompanyData))
    print(tempCompanyData)
    
if __name__ == '__main__':
    getComanyDataFromDB()
    