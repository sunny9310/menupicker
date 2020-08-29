import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

driver = webdriver.Chrome('C:\\Users\\SUNNY\\Downloads\\chromedriver_win32\\chromedriver.exe')
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.

driver.get('https://www.tripadvisor.co.kr/Restaurants-g294197-oa00-Seoul.html');
time.sleep(2)					# 2초간 동작하는 걸 봅시다
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.quit()
db = client.dbrestaurants

trs = soup.select('#component_2 > div > div')

for i in range(31, 61) :
    adv = soup.find('div', {'data-test':str(i)+"_list_item"})
    name = adv.select_one('span > div._1kNOY9zw > div._2Q7zqOgW > div._2kbTRHSI > div > span > a').text
    menu = adv.select_one('span > div._1kNOY9zw > div._2Q7zqOgW > div._2rmp5aUK > div > div.MIajtJFg._1cBs8huC._3d9EnJpt > span> span').text
    print( name, menu)