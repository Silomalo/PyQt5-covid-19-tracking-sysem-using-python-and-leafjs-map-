import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QGridLayout,QTextEdit

from PyQt5 import QtCore, QtGui, QtWidgets


class Updaterecords(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update')
        self.setFixedWidth(500)
        self.setFixedHeight(450)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setStyleSheet("""
            QWidget{
                border:none;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.938, y2:0.380682, stop:0 rgba(232, 170, 127, 255), stop:0.823864 rgba(216, 255, 255, 230));	
            }
            QLineEdit{
                font-size: 30px;
                height:30px;
                text-align:center;
                font-size:15px;
                border:none;
                background-color:transparent;
	            border-bottom: 1px solid gray;
                border-left: 1px solid gray;
                color:blue;
            }
            QLabel{
                font-size: 25px;
                font-family:gabriola;
                background-color:transparent;
            }
            QTextEdit{
                max-height:70px;
                font-size:12px;
                background-color:transparent;
	            border: 1px solid gray;
                color:blue;
            }
            
            QPushButton{
                font-size: 25px;
                font-family:gabriola;
                width:130px;
            }
            QPushButton{
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.102273 rgba(0, 115, 210, 255), stop:1 rgba(255, 255, 255, 255));
            border-radius:10px
            }
            QPushButton:pressed{
                
                background-color: rgba(0, 170, 255,.4);
            }
            """)
        
        mainLayout = QGridLayout()
        self.date = QLineEdit()
        self.county = QLineEdit()
        self.lat = QLineEdit()
        self.long = QLineEdit()
        self.new = QLineEdit()
        self.rec = QLineEdit()
        self.death = QLineEdit()
        self.info = QTextEdit()
        self.pop =  QTextEdit()
        mainLayout.addWidget((self.date),0,0)
        mainLayout.addWidget((self.county),0,1)
        mainLayout.addWidget(QLabel("Latitude:"),1,0)
        mainLayout.addWidget((self.lat),1,1)
        mainLayout.addWidget(QLabel("Longitude:"),2,0)
        mainLayout.addWidget((self.long),2,1)
        mainLayout.addWidget(QLabel("New:"),3,0)
        mainLayout.addWidget((self.new),3,1)
        mainLayout.addWidget(QLabel("Recoverd:"),4,0)
        mainLayout.addWidget((self.rec),4,1)
        mainLayout.addWidget(QLabel("Fatality:"),5,0)
        mainLayout.addWidget((self.death),5,1)
        mainLayout.addWidget(self.info)
        mainLayout.addWidget(self.pop)

        self.saveButton = QPushButton('Save Data')
        self.saveButton.clicked.connect(self.close)
        mainLayout.addWidget(self.saveButton)
        
        self.closeButton = QPushButton('Abadon')
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.closeButton)

        self.setLayout(mainLayout)
        

    def displayInfo(self):
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setFixedWidth(800)

        self.secondWindow = Updaterecords()

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""
            QLineEdit{height: 40px; font-size: 30px}
            QLabel{font-size: 30px}
            
        """)

        self.name = QLineEdit()
        self.age = QLineEdit()
        mainLayout.addWidget(QLabel('Name:'))
        mainLayout.addWidget(self.name)
        mainLayout.addWidget(QLabel('Age:'))
        mainLayout.addWidget(self.age)

        self.Confirm = QPushButton('Confirm')
        self.Confirm.setStyleSheet('font-size: 30px')
        self.Confirm.clicked.connect(self.passingInformation)
        mainLayout.addWidget(self.Confirm)

        self.setLayout(mainLayout)
        self.date= "12/12/2019"
        self.county= "Nairobi"
        self.lat= "213"
        self.long= "231"
        self.new= "123"
        self.rec= "12"
        self.death= "1"
        self.info= "info"
        self.pop= "pop"
    def passingInformation(self):
        self.secondWindow.date.setText(self.date)
        self.secondWindow.county.setText(self.county)
        self.secondWindow.lat.setText(self.lat)
        self.secondWindow.long.setText(self.long)
        self.secondWindow.new.setText(self.new)
        self.secondWindow.rec.setText(self.rec)
        self.secondWindow.death.setText(self.death)
        self.secondWindow.info.setText(self.info)
        self.secondWindow.pop.setText(self.pop)
        self.secondWindow.displayInfo()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
