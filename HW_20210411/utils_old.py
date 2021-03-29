import requests
from bs4 import BeautifulSoup

def get_rank(url): #this function can get the weekly rank of articles from Wikiprdia
    bs = BeautifulSoup(requests.get(url, proxies={
    'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'}).content) #use bs to get html

    title = str((bs.find(class_="mw-headline")).contents) #get title of the report page
    str_rank = title[title.index("M"):title.index(")")+1]+'\n' #store title in str_rank
    
    table = bs.find(class_='wikitable') #get the main body of the rank table
    flag = 0 #if this column represents the rank, the next column represents article titles which will be used
    count = 1 #number of articles
    for item in table.find_all('td'): #find all units of the table
        if flag == 1: #if the previous column represents the rank
            str_rank=str_rank+'\n'+str(count-1)+'  '+str(item.find('a')['title']) #store title of articles
            #print('%2d  %s' % (count - 1, item.find('a')['title']))
            flag = 0
        if str(item) == '<td>' + str(count) + '\n</td>': #if the content represents the rank
            flag = 1
            count = count + 1
        if count == 12:
            break
    return str_rank