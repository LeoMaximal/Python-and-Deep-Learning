import requests
from bs4 import BeautifulSoup

def wiki_rank(previous):
    url = 'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report'
    if previous > 0 and isinstance(previous, int):
        for i in range(1, previous + 1):
            bs = BeautifulSoup(requests.get(url, proxies={
            'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'}).content)
            link = bs.find(name='span', attrs={'class': 'plainlinks'})
            url = 'https://en.wikipedia.org/' + link.find('a')['href']
    
    bs = BeautifulSoup(requests.get(url, proxies={
    'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'}).content)
    table = bs.find(class_='wikitable')
    flag = 0
    count = 1
    for item in table.find_all('td'):
        if flag == 1:
            print(count - 1, item.find('a')['title'])
            flag = 0
        if str(item) == '<td>' + str(count) + '\n</td>':
            flag = 1
            count = count + 1
        if count == 12:
            break
    return None