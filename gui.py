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
        label.setStyleSheet("color: #CFD8DC")
        # label.setChecked(label.editor.fontUnderline())
        label.move(105,105)
        label.setFont(QFont('Fredoka One', 29))
        # label.setStyleSheet(“background-color: blue;”)
        self.setStyleSheet("""
        background-color: #5D6D7E;
        
        """)
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
        # button.setFont(QFont('Comic Sans MS', 20,)
        button.setFixedSize(100,35)
        button.move(290,185)
        button.setFont(QFont("Fredoka One",13.5))
        # button.setStyleSheet("color: ")
        button.setStyleSheet("""
        background-color: #80CBC4;
        color: #FDFEFE;
        border-radius: 5px;
        """)
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
        button = QPushButton("Guide", self) 
        button.setFont(QFont("Fredoka One",13.5))
        button.setFixedSize(100,35)
        button.move(290,240)
        button.setStyleSheet("""
        background-color: #80CBC4;
        color: #FDFEFE;
        border-radius: 5px;
        """)

        
        # setting geometry of button 
        # button.setGeometry(200, 150, 100, 30) 

        # adding action to a button 
        button.clicked.connect(self.clickme)

    def Button3(self): 

        # creating a push button 
        button = QPushButton("Exit", self) 
        # button.setFixedSize(100,0)
        button.setFont(QFont("Fredoka One",13.5))
        button.setFixedSize(100,35)
        button.move(290,295)
        button.setStyleSheet("""
        background-color: #E57373;
        color: #FDFEFE;
        border-radius: 5px;
        """)

        
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
    mw.resize(700,450)
    mw.show()
    sys.exit(app.exec_())