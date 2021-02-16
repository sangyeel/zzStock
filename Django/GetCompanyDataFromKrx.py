import pandas
import requests
import io

#상장주식수 파싱하기위해서 아래 URL에서 얻어옴..
#GenerateOTP에서 OTP를 받아오고 download url에서 code의 value로 넣어줌

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ssStock.settings")


import django
django.setup()

from CompanyDataFromKrx.models import CompanyDataFromKrx

class GetCompanyDataFromDartKrx:
    __GENURL  = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    __GENPOSTDATA = {\
        "csvxls_isNo": "false",\
        "mktId": "ALL",\
        "name": "fileDown",\
        "share": "1",\
        "url": "dbms/MDC/STAT/standard/MDCSTAT01901"}
    __DOWNURL = "http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd"#Response string is CSV format
    __DOWNPOSTDATA ={'code': ''}

    def __init__(self):
        genRes = requests.post(GetCompanyDataFromDartKrx.__GENURL,data = GetCompanyDataFromDartKrx.__GENPOSTDATA)
        GetCompanyDataFromDartKrx.__DOWNPOSTDATA['code'] = genRes.text
        downRes = requests.post(GetCompanyDataFromDartKrx.__DOWNURL,data = GetCompanyDataFromDartKrx.__DOWNPOSTDATA)
        downRes.encoding = 'euc-kr'
        companyDf = pandas.read_csv(io.StringIO(downRes.text))#downRes.text is not a file so we should add the IO formatter
        #표준코드,단축코드,한글 종목명,한글 종목약명,영문 종목명,상장일,시장구분,증권구분,소속부,주식종류,액면가,상장주식수
        for i in companyDf.index:
            CompanyDataFromKrx(companyStockCode = companyDf.loc[i, '단축코드'],\
            companyStockMarket = companyDf.loc[i, '시장구분'],\
            companyStockFaceValue = companyDf.loc[i, '액면가'],\
            companyStockTotal = companyDf.loc[i, '상장주식수']).save()
            print('items : {}/{}'.format(i,companyDf.index))

            

if __name__ == '__main__':
    parsedData = GetCompanyDataFromDartKrx()