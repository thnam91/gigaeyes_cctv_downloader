import os
import requests 
from selenium import webdriver
import datetime

driver = webdriver.Chrome()
driver.get("https://gigaeyes.co.kr/")


url = "https://gigaeyes.co.kr/videoManageN/summaryManageMake"
header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '114',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=584EADBE46A3385B52F5EFD963A8256A.web02',
    'Host': 'gigaeyes.co.kr',
    'Origin': 'https://gigaeyes.co.kr',
    'Referer': 'https://gigaeyes.co.kr/homeN/index',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {
    'cam_id': '800079841341001',
    'summary_type': '13',
    'start_time': '20200203113000',
    'end_time': '20200203123000',
    'new_yn': 'Y',
    'makeType': 'summary'
}

res = requests.post(url, headers=header, data=data)
print(res.status_code)