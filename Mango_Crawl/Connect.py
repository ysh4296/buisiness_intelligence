#Connect.py

from selenium import webdriver

# driver 로 접속, 로딩시간 3초
driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)

# 웹 페이지 불러오기
def initpage():
    driver.get('https://www.mangoplate.com/top_lists')
    driver.implicitly_wait(3)

def connect(url):
    driver.get('https://www.mangoplate.com/' + url)
    driver.implicitly_wait(3)