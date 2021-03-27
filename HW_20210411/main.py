from utils import *
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QGridLayout

class wiki_rank(QDialog): #define a class to show the the weekly rank of articles from Wikiprdia
    def __init__(self):
        super().__init__()
        
        #set the elements of the window
        self.setWindowTitle('Wikipedia: Weekly Top 10')
        self.btnGet = QPushButton('Get Rank', self)
        self.btnPre = QPushButton('Previous Week', self)
        self.btnNext = QPushButton('Next Week', self)
        self.btnQuit = QPushButton('Quit', self)
        self.text = QLabel()
        
        #set the position of elements
        layout = QGridLayout(self)
        layout.addWidget(self.text, 0, 1, 3, 15)
        layout.addWidget(self.btnGet, 4, 1, 1, 3)
        layout.addWidget(self.btnPre, 4, 5, 1, 3)
        layout.addWidget(self.btnNext, 4, 9, 1, 3)
        layout.addWidget(self.btnQuit, 4, 13, 1, 3)

        #connet button to function
        self.btnGet.clicked.connect(self.show_rank)
        self.btnPre.clicked.connect(self.show_pre)
        self.btnNext.clicked.connect(self.show_next)
        self.btnQuit.clicked.connect(self.close)

    url = 'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report' #the url of the rank of this week

    def show_rank(self):
        global url
        url = 'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report'
        str=get_rank(url)
        self.text.setText(str) #show  the rank

    def show_pre(self):
        global url #make sure that url can be editted
        bs = BeautifulSoup(requests.get(url, proxies={
        'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'}).content)
        link = bs.find(name='span', attrs={'class': 'plainlinks'}) #get the url of the rank of the previous week
        url = 'https://en.wikipedia.org/' + link.find('a')['href'] #make sure that the url is accessible
        str=get_rank(url)
        self.text.setText(str)

    def show_next(self):
        global url
        if url == 'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report': #no 'next week' link on the page of this week
            self.text.setText('NO DATA!')
        else:
            bs = BeautifulSoup(requests.get(url, proxies={
            'https': 'http://127.0.0.1:1087', 'http': 'http://127.0.0.1:1087'}).content)
            link = bs.find(name='span', attrs={'style':'float:right;'}) #get the url of the rank of the next week
            url = 'https://en.wikipedia.org/' + link.find('a')['href']
            str=get_rank(url)
            self.text.setText(str)
    
if __name__ == '__main__':
    a = QApplication(sys.argv)
    ex = wiki_rank()
    ex.show()
    sys.exit(a.exec_())