#_*_ coding: utf-8 _*_
import pandas
import requests

#상장주식수 파싱하기위해서 아래 URL에서 얻어옴..
#GenerateOTP에서 OTP를 받아오고 download url에서 code의 value로 넣어줌

class GetCompanyDataFromDartKrx:
    __GENURL  = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    __GENPOSTDATA = {\
        "csvxls_isNo": "false",\
        "mktId": "ALL",\
        "name": "fileDown",\
        "share": "1",\
        "url": "dbms/MDC/STAT/standard/MDCSTAT01901"}
    __DOWNURL = "http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd"
    __DOWNPOSTDATA ={'code': ''}

    def __init__(self):
        genRes = requests.post(GetCompanyDataFromDartKrx.__GENURL,data = GetCompanyDataFromDartKrx.__GENPOSTDATA)
        GetCompanyDataFromDartKrx.__DOWNPOSTDATA['code'] = genRes.text
        downRes = requests.post(GetCompanyDataFromDartKrx.__DOWNURL,data = GetCompanyDataFromDartKrx.__DOWNPOSTDATA)
        downRes.encoding = 'euc-kr'
        print(downRes.text)

if __name__ == '__main__':
    parsedData = GetCompanyDataFromDartKrx()