import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for page_num in range(1,11):
    url = "https://www.mangoplate.com/search/%EC%84%9C%EC%9A%B8%20%EB%A0%88%EC%8A%A4%ED%86%A0%EB%9E%91?keyword=%EC%84%9C%EC%9A%B8%20%EB%A0%88%EC%8A%A4%ED%86%A0%EB%9E%91&page=" + str(page_num)
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    db = client.dbrestaurants
    trs = soup.select(
        'body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li > div > figure')
# body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li:nth-child(1) > div:nth-child(1) > figure > figcaption > div > a > h2
# body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li:nth-child(1) > div:nth-child(1) > figure > figcaption > div > p.etc
# body > main > article > div.column-wrapper > div > div > section > div.search-list-restaurants-inner-wrap > ul > li:nth-child(1) > div:nth-child(1) > figure > figcaption > div > p.etc > span


    for tr in trs:
        image = tr.select_one('a > div > img')
        name = tr.select_one('figcaption > div > a > h2').text.strip()
        loc = tr.select_one('figure > figcaption > div > p.etc').text.strip()

        doc ={
                 'name': name,
                 'location': loc
                                }
        db.restaurants.insert_one(doc);

        print(doc)
