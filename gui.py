import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont
from PyQt5.QtCore import *


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.layout = QVBoxLayout()
        # self.label = QLabel("Geriatric Agility Detection")
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.move(200,500)
        label = QLabel("Geriatric Agility Detection", self)
        label.setStyleSheet("color: #eeeeee")
        # label.setChecked(label.editor.fontUnderline())
        label.move(230,130)
        label.setFont(QFont('Comic Sans MS', 20,))
        # label.setStyleSheet(“background-color: blue;”)
        self.setStyleSheet("background-color: #686d76;")
        label.adjustSize()

        # self.layout.addWidget(self.label)
        self.setWindowTitle("My Own Title")
        self.setLayout(self.layout)

        self.Button1()
        self.Button2()
        self.Button3()


    def Button1(self): 

        # creating a push button 
        button = QPushButton("Start", self) 
        # button.setFixedSize(100,0)
        button.move(340,250)
        button.setStyleSheet("background-color: #19d3da")
        # button.setStyleSheet("border-radius: 1")
        # button.setStyleSheet("border-color: blue")
        # button.setStyleSheet("border-color: #373a40")
        #  button.setStyleSheet("border-radius : 50;  
                            #   border : 2px solid black") 


        
        # setting geometry of button 
        # button.setGeometry(200, 150, 100, 30) 

        # adding action to a button 
        button.clicked.connect(self.clickme) 

    def Button2(self): 

        # creating a push button 
        button = QPushButton("Instructions", self) 
        # button.setFixedSize(100,0)
        button.move(340,310)

        
        # setting geometry of button 
        # button.setGeometry(200, 150, 100, 30) 

        # adding action to a button 
        button.clicked.connect(self.clickme)

    def Button3(self): 

        # creating a push button 
        button = QPushButton("Instructions", self) 
        # button.setFixedSize(100,0)
        button.move(340,370)

        
        # setting geometry of button 
        # button.setGeometry(200, 150, 100, 30) 

        # adding action to a button 
        button.clicked.connect(self.clickme) 

    def clickme(self): 
        # printing pressed 
        print("pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(800,600)
    mw.show()
    sys.exit(app.exec_())