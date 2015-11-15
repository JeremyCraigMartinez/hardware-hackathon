"""
    ********************* VerySimpleWebBrowser ************************

    This is a Very Simple Web Browser implemented over Qt and QtWebKit.

    author: Juan Manuel Garcia <jmg.utn@gmail.com>

    *******************************************************************
    http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz
"""

import sys
from PyQt4 import QtCore, QtGui, QtWebKit

class Browser(QtGui.QMainWindow):

    def __init__(self):
        """
            Initialize the browser GUI and connect the events
        """

        QtGui.QMainWindow.__init__(self)
        self.resize(1600,600)
        self.centralwidget = QtGui.QWidget(self)

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.frame = QtGui.QFrame(self.centralwidget)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout()
        #self.tb_url = QtGui.QLineEdit(self.frame)
        #self.bt_back = QtGui.QPushButton(self.frame)
        #self.bt_ahead = QtGui.QPushButton(self.frame)

        #self.bt_back.setIcon(QtGui.QIcon().fromTheme("go-previous"))
        #self.bt_ahead.setIcon(QtGui.QIcon().fromTheme("go-next"))
        #self.horizontalLayout.addWidget(self.bt_back)
        #self.horizontalLayout.addWidget(self.bt_ahead)
        #self.horizontalLayout.addWidget(self.tb_url)
        #self.gridLayout.addLayout(self.horizontalLayout)

        self.page = QtWebKit
        self.page.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
        self.html = self.page.QWebView()
        self.html = QtWebKit.QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        #self.connect(self.tb_url, QtCore.SIGNAL("returnPressed()"), self.browse)
        #self.connect(self.bt_back, QtCore.SIGNAL("clicked()"), self.html.back)
        #self.connect(self.bt_ahead, QtCore.SIGNAL("clicked()"), self.html.forward)

        self.default_url = sys.argv[1]
        #self.tb_url.setText(self.default_url)
        self.browse()

        #self.view = QtWebKit.QWebSettings
        #self.view.globalSettings.setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
        #Settings = self.ui.webView.settings()
        #QWebSettings.setAttribute(QWebSettings.PluginsEnabled,True)
        #QtWebKit.QWebSettings.setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)


    def browse(self):
        """
            Make a web browse on a specific url and show the page on the
            Webview widget.
        """

        #url = self.tb_url.text() if self.tb_url.text() else self.default_url
        self.html.load(QtCore.QUrl(self.default_url))
        self.html.show()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    main = Browser()
    main.show()
    sys.exit(app.exec_())
