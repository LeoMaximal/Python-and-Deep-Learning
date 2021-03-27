import requests
from bs4 import BeautifulSoup

def get_rank(url):
    #url = 'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report'
    bs = BeautifulSoup(requests.get(url, proxies={
    'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'}).content)

    title = str((bs.find(class_="mw-headline")).contents)
    str_rank = title[title.index("M"):title.index(")")+1]+'\n'
    
    table = bs.find(class_='wikitable')
    flag = 0
    count = 1
    for item in table.find_all('td'):
        if flag == 1:
            str_rank=str_rank+'\n'+str(count-1)+'  '+str(item.find('a')['title'])
            #print('%2d  %s' % (count - 1, item.find('a')['title']))
            flag = 0
        if str(item) == '<td>' + str(count) + '\n</td>':
            flag = 1
            count = count + 1
        if count == 12:
            break
    return str_rank