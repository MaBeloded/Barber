import requests
from bs4 import BeautifulSoup as b


url_1 = 'https://barber-shop.su/kak-raskrutit-barbershop/'


def ann_1(url_1):
    r = requests.get(url_1)
    soup = b(r.text, 'html.parser')
    oven = soup.find_all('div', class_='content-area')
    all_oven = []
    print(oven)
    for i in oven:
       all_oven.append(i.text)
    return all_oven

ann_1(url_1)
