import PyQt4.QtGui
import PyQt4.uic
import os.path
import re
import sys
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl


class MainForm(PyQt4.QtGui.QMainWindow,PyQt4.QtGui.QDialog):
    def __init__(self,parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = PyQt4.uic.loadUi('./ramennapuri.ui')
    

        # pixmap = PySide.QtGui.QPixmap() 
        # pixmap.load("mem.jpg")
        # self.scene = PySide.QtGui.QGraphicsScene(self)
        # item = PySide.QtGui.QGraphicsPixmapItem(pixmap)
        # self.scene.addItem(item)
        # self.ui.graphicsView.setScene(self.scene)
        #self.x = ""
        self.establish()
        self.open_file_button = PyQt4.QtGui.QPushButton('pushButton')  
        #self.pic(self.x)    
        self.view()

    def pushButton(self):
        filename = PyQt4.QtGui.QFileDialog.getOpenFileName(self,"Open file",os.path.expanduser('~~')+'/Desktop') 
        self.x = filename[0]
        self.pic(self.x)

    def establish(self):
        self.ui.pushButton.clicked.connect(self.pushButton)

    def pic(self,x):
        pixmap = PyQt4.QtGui.QPixmap() 
        pixmap.load(self.x)
        self.scene = PyQt4.QtGui.QGraphicsScene(self)
        item = PyQt4.QtGui.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)

    def view(self):
    
        self.ui.webView.load(QUrl("https://www.google.co.jp/maps/place/%E5%B1%B1%E5%BD%A2%E7%9C%8C%E7%B1%B3%E6%B2%A2%E5%B8%82/@37.8460899,140.1367754,14z/data=!4m5!3m4!1s0x5f8aedd77c776f45:0x7afef37ef8b8df7!8m2!3d37.9222401!4d140.1167811"))
        self.ui.webView.show()

    def text_Edite(self):
        self.ui.text_Edite.clicked.connect(self.text_Edite)

    def textEdite_3(self):
        self.ui.textEdite_3.clicked.connect(self.textEdite_3)

    def textEdite_4(self):
        self.ui.textEdite_4.clicked.connect(self.textEdite_4)
 
    def horizontalSlider(self):
        self.ui.horizontalSlider.connect(self.horizontalSlider)

    def horizontalSlider_2(self):
        self.ui.horizontalSlider_2.connect(self.horizontalSlider_2)

    def horizontalSlider_3(self):
        self.ui.horizontalSlider_3.connect(self.horizontalSlider_3)




if __name__ == '__main__':
    app = PyQt4.QtGui.QApplication(sys.argv)
    # pixmap = PySide.QtGui.QPixmap() 
    # pixmap.load("mem.jpg")
    main_form = MainForm()
    main_form.ui.show()

    sys.exit(app.exec_())
