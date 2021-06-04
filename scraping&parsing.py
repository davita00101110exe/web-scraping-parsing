import requests
from bs4 import BeautifulSoup
import csv
from random import randint
from time import sleep

f = open('sites.csv', 'w', encoding='utf-8_sig', newline='\n')
f_obj = csv.writer(f)
f_obj.writerow(['საიტი', 'საიტის აღწერა', 'ჰიტი (გუშინ)'])
ind = 1
while ind <= 5:
    url = 'https://top.ge/page/' + str(ind)
    r = requests.get(url)
    c = r.text
    soup = BeautifulSoup(c, 'html.parser')
    sites = soup.find('tbody')
    all_sites = sites.find_all('tr')
    for site in all_sites:
        name = site.find('a', class_='stie_title').text
        desc = site.find('td', class_='tr_paddings desc_pd hidden-xs ipad_hidden').text
        hits = site.find('span', class_='stat_now_big').text
        f_obj.writerow([name, desc, hits])
    ind += 1
    sleep(randint(15, 20))
