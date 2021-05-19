# using MediaWiki API to get most viewed de.wikipedia articles of the day and get random articles
from utils import *
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QGridLayout

class wiki_rank(QDialog): #define a class to show the rank of articles from Wikiprdia
    def __init__(self):
        super().__init__()
        
        #set the elements of the window
        self.setWindowTitle('Wikipedia: Top Read')
        self.btnGet = QPushButton('Get Rank', self)
        self.btnSprs = QPushButton('Surprise Me', self)
        self.btnQuit = QPushButton('Quit', self)
        self.text = QLabel()
        self.text.setOpenExternalLinks(True)
        
        #set the position of elements
        layout = QGridLayout(self)
        layout.addWidget(self.text, 0, 1, 3, 15)
        layout.addWidget(self.btnGet, 15, 1, 1, 3)
        layout.addWidget(self.btnSprs, 15, 7, 1, 3)
        layout.addWidget(self.btnQuit, 15, 13, 1, 3)

        #connet button to function
        self.btnGet.clicked.connect(self.show_rank)
        self.btnSprs.clicked.connect(self.show_rand)
        self.btnQuit.clicked.connect(self.close)

    def show_rank(self):
        str=get_rank()
        self.text.setText(str) #show  the rank

    def show_rand(self):
        str = get_rand()
        self.text.setText(str) #show random articles
    
if __name__ == '__main__':
    a = QApplication(sys.argv)
    ex = wiki_rank()
    ex.show()
    sys.exit(a.exec_())