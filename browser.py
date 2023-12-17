import subprocess
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#main window class (to create a window)-sub class of QMainWindow class
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.profile = QWebEngineProfile.defaultProfile()
        self.clear_cookies()
        self.browser = QWebEngineView(self)
        self.browser.setPage(QWebEnginePage(self.profile, self.browser))
        self.browser.setUrl(QUrl('http://localhost:5000/homepage/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        prevBtn = QAction('Prev',self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)
        
        goBtn = QAction('Go',self)
        goBtn.triggered.connect(self.loadUrl)
        navbar.addAction(goBtn)
        
        nextBtn = QAction('Next',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        
        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        
        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        
        clearBtn = QAction('Forget',self)
        clearBtn.triggered.connect(self.clear_cookies)
        navbar.addAction(clearBtn)
        
        self.searchBar = QLineEdit()
        #when someone presses return(enter) call loadUrl method
        self.searchBar.returnPressed.connect(self.loadUrl)
        #adding created seach bar to navbar
        navbar.addWidget(self.searchBar)
        #if url in the searchBar is changed then call updateUrl method
        self.browser.urlChanged.connect(self.updateUrl)
    #end of init
    def clear_cookies(self):
        # Clear all cookies for the default profile
        self.profile.cookieStore().deleteAllCookies()
    #method to navigate back to home page
    def home(self):
        self.browser.setUrl(QUrl('http://localhost:5000/homepage/'))
    #method to load the required url
    def loadUrl(self):
        #fetching entered url from searchBar
        url = self.searchBar.text()
        #loading url
        self.browser.setUrl(QUrl(url))
    #method to update the url
    def updateUrl(self, url):
        #changing the content(text) of searchBar
        self.searchBar.setText(url.toString())
    #end of window class

subprocess.Popen('python -m http.server 5000')

QApplication.setApplicationName('Ghajini Browser')

QApplication.setStyle("plastique")

dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()

MyApp = QApplication([])

MyApp.setStyleSheet(dark_stylesheet)

window = Window()

window.setWindowIcon(QIcon('icon.png'))

MyApp.exec_()
