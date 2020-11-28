import sys
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont
from PyQt5.QtCore import *
from PyQt5 import QtCore
from test import *
# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)

#Play variables
# box_range = 30
# check_range = 40


# n = box_range*2+10
# store_colors = [[[]*n]*n]*3

# _, frame = cap.read()

# height, width, channels = frame.shape

# #Center
# start_x = width//2 - box_range
# end_x = width//2 + box_range
# start_y = height//2 - box_range
# end_y = height//2 + box_range

# #Moving box up
# start_y -= 200
# end_y -= 200

# cnt = 0


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.layout = QVBoxLayout()
        label = QLabel("Geriatric Agility Detection", self)
        label.setStyleSheet("color: #CFD8DC")
        label.move(105,105)

        label.setFont(QFont('Fredoka One', 29))
        self.setStyleSheet("""
        background-color: #5D6D7E;
        
        """)
        label.adjustSize()

        self.setWindowTitle("My Own Title")
        self.setLayout(self.layout)

        self.Button1()
        self.Button2()
        self.Button3()


    def Button1(self): 

        button = QPushButton("Start", self)
        button.move(290,185)
        # button.setFont(QFont("Fredoka One",13.5))
        button.setStyleSheet("""
        background-color: #80CBC4;
        color: #FDFEFE;
        border-radius: 5px;
        left: 100px;
        """)
        button.clicked.connect(register_Background)


    def Button2(self): 

        button = QPushButton("Guide", self) 
        button.setFont(QFont("Fredoka One",13.5))
        button.setFixedSize(100,35)
        button.move(290,240)
        button.setStyleSheet("""
        background-color: #80CBC4;
        color: #FDFEFE;
        border-radius: 5px;
        """)

        

        button.clicked.connect(self.clickme)

    def Button3(self): 

        button = QPushButton("Exit", self) 
        button.setFont(QFont("Fredoka One",13.5))
        button.setFixedSize(100,35)
        button.move(290,295)
        button.setStyleSheet("""
        background-color: #E57373;
        color: #FDFEFE;
        border-radius: 5px;
        """)

        

        button.clicked.connect(self.clickme) 

    def clickme(self): 
        # printing pressed 
        print("pressed")

    def registerBackground(self): 
        # printing pressed 
        print("pressed")


if __name__ == "__main__":
    # cap = cv2.VideoCapture(0)
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(700,450)
    mw.setFixedSize(700, 450)
    mw.show()
    sys.exit(app.exec_())