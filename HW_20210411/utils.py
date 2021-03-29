# using GUI to display wikipedia top read or random articles
import requests
import json

def get_descript(title_link):  #using article title to get the short description of the article
    #API query
    url = 'https://de.wikipedia.org/w/api.php?action=query&format=json&prop=description&titles=' + title_link
    r = requests.get(url, proxies={'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'})
    js = json.loads(r.text) #use json to convert query result into dict
    info = js['query']['pages'] #find the useful part
    for item in info: #get info. of the page without knowing the ID
        info = info[item]
    if info.__contains__('description'): #avoid error
        return info['description']
    else:
        return None

def get_rank(): #get most viewed articles
    #API query
    url = 'https://de.wikipedia.org/w/api.php?action=query&format=json&list=mostviewed&pvimlimit=15'
    r = requests.get(url, proxies={'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'})
    js = json.loads(r.text)
    data = js['query']['mostviewed']
    count = 0 #the rank of articles
    str_rank='<p><b style="font-size:18px;"> Daily Top 10 </b><br><br>' #title of output
    for item in data:
        if count > 9: #get top 10
            break
        if item['ns'] == 0: #filter functional pages such as homepage
            count = count + 1
            title = item['title'] #get title
            viewed = str(item['count'] / 1000) #get viewed times
            title_link = title.replace(' ', '_')  #make title into the format of url
            #output contents (in html form)
            str_rank = str_rank + '<b style="color:black;font-size:16px;">' + str(count) + \
            '. <a href=https://de.wikipedia.org/wiki/' + title_link + '>' + title + \
            '</a>  viewed:  '+viewed[0:viewed.index('.') + 2]+'K</b><br>'
            description = get_descript(title_link)
            if description:
                str_rank = str_rank + description + '<br>'
    str_rank = str_rank + '<\p>'
    return str_rank

def get_rand():  #get random articles (main part is a bit different from get_rank)
    #API query
    url = 'https://de.wikipedia.org/w/api.php?action=query&format=json&list=random&rnlimit=50'
    r = requests.get(url, proxies={'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'})
    js = json.loads(r.text)
    str_rand = '<p><b style="font-size:18px;"> Random Pages </b><br><br>'
    count = 0
    for item in js['query']['random']:
        if count > 4: #get the first five articles
            break
        if item['ns'] == 0:
            count = count + 1
            title = item['title']
            title_link = title.replace(' ', '_')
            str_rand = str_rand + '<b><a style="color:black;font-size:16px;" href=https://de.wikipedia.org/wiki/' \
            + title_link + '>' + title + '</a></b><br>'
            description = get_descript(title_link)
            if description:
                str_rand = str_rand + description + '<br>'
    str_rand = str_rand + '</p>'
    return str_rand