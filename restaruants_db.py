import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

url = "https://www.tripadvisor.co.kr/Restaurants-g294197-Seoul.html"
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#component_2 > div > div')
#compon

for tr in trs :
    name = tr.select_one('span > div._1kNOY9zw > div._2Q7zqOgW > div._2kbTRHSI > div > span > a')
    image = tr.select_one('span > div._1kNOY9zw > div._2jF2URLh > span > a > div._2KPNYP9B > div > div.iroXhDrr > ul')

    menu = tr.select_one('span > div._1kNOY9zw > div._2Q7zqOgW > div._2rmp5aUK > div > div.MIajtJFg._1cBs8huC._3d9EnJpt > span> span')
    if name is not None:
        name = ''.join([i for i in name if not i.isdigit()]).replace('.','').strip()
    if menu is not None:
        print(image)
        # print(name, menu.text)

