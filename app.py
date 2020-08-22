import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

driver = webdriver.Chrome('C:\\Users\\SUNNY\\Downloads\\chromedriver_win32\\chromedriver.exe')
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.

page = [0, 30, 60, 90]
for i in range(0,4):
    driver.get('https://www.tripadvisor.co.kr/Restaurants-g294197-oa'+str(page[i])+'-Seoul.html');
    time.sleep(2)					# 2초간 동작하는 걸 봅시다
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    db = client.dbrestaurants

    trs = soup.select('#component_2 > div > div')

    for tr in trs :
        # image = tr.select_one(
        #     'span > div._1kNOY9zw > div._2jF2URLh > span > a > div._2KPNYP9B > div > div.iroXhDrr > ul > li._10EZNUuy.Z-I2OInc > div')
        name = tr.select_one('span > div._1kNOY9zw > div._2Q7zqOgW > div._2kbTRHSI > div > span > a')
        menu = tr.select_one('span > div._1kNOY9zw > div._2Q7zqOgW > div._2rmp5aUK > div > div.MIajtJFg._1cBs8huC._3d9EnJpt > span> span')
        if name is not None:
            name = name.text
            # name = ''.join([i for i in name if not i.isdigit()]).replace('.','').strip()
        if menu is not None:

            print(name, menu.text)

            # doc = {
            #     'name': name,
            #     'menu': menu
            #         }
            # db.restaurants.insert_one(doc);