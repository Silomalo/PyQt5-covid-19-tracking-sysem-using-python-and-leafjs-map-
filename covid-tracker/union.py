import sys
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint, QTimer, QTime, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore,QtSql
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect
from ui import login as login
from ui import main as main
import geomap as geo
import mysql.connector as mc
from PyQt5.QtWidgets import QDialog,QTableWidget, QTableWidgetItem,QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QLabel, QGridLayout,QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
data = ["uasin-gishu","kericho","nandi"]
class Geoclass(geo.MyApp, QtWidgets.QMainWindow):
    def __init__(self):
        super(Geoclass, self).__init__()
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
        self.Recordid = QLineEdit()
        self.Recorddate = QLineEdit()
        self.Recordcounty = QLineEdit()
        self.Recordlat = QLineEdit()
        self.Recordlong = QLineEdit()
        self.Recordnew = QLineEdit()
        self.Recordrec = QLineEdit()
        self.Recorddeath = QLineEdit()
        self.Recordinfo = QTextEdit()
        self.Recordpop =  QTextEdit()
        mainLayout.addWidget((self.Recorddate),0,0)
        mainLayout.addWidget((self.Recordcounty),0,1)
        mainLayout.addWidget(QLabel("Latitude:"),1,0)
        mainLayout.addWidget((self.Recordlat),1,1)
        mainLayout.addWidget(QLabel("Longitude:"),2,0)
        mainLayout.addWidget((self.Recordlong),2,1)
        mainLayout.addWidget(QLabel("New:"),3,0)
        mainLayout.addWidget((self.Recordnew),3,1)
        mainLayout.addWidget(QLabel("Recoverd:"),4,0)
        mainLayout.addWidget((self.Recordrec),4,1)
        mainLayout.addWidget(QLabel("Fatality:"),5,0)
        mainLayout.addWidget((self.Recorddeath),5,1)
        mainLayout.addWidget(self.Recordinfo)
        mainLayout.addWidget(self.Recordpop)
        #mainLayout.addWidget(self.Recordid)

        self.saveButton = QPushButton('Save Data')
        self.saveButton.clicked.connect(self.saveUpdatedData)
        mainLayout.addWidget(self.saveButton)
        self.closeButton = QPushButton('Abadon')
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.closeButton)
        self.setLayout(mainLayout)
        

    def displayInfo(self):
        self.show()
    def saveUpdatedData(self):
        try:
            date = self.Recorddate.text()
            county = self.Recordcounty.text()
            latitude=float(self.Recordlat.text())
            longitude=float(self.Recordlong.text())
            new=int(self.Recordnew.text())
            recovered=int(self.Recordrec.text())
            deceased=int(self.Recorddeath.text())
            info= self.Recordinfo.toPlainText()
            pop= self.Recordpop.toPlainText()
            rid= int(self.Recordid.text())

            self.uPrecords(date, county,latitude,longitude, new, recovered, deceased, info, pop,rid)
        
            #self.add_records(date, county,latitude,longitude, new, recovered, deceased, info, pop)
        except ValueError:
            print("error")
            QMessageBox.warning(QMessageBox(), 'Error', 'Please Recheck your Entries.')
            return False

    def uPrecords(self, date, county,latitude,longitude, new, recovered, deceased, info, pop,rid):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = "UPDATE records SET date= ?,county= ?,latitude= ?,longitude= ?, new= ?,recovered = ?,deceased = ?,info = ?,pop = ? WHERE id = ?"
        value = (date, county,latitude,longitude, new, recovered, deceased, info, pop, rid)
        cursor.execute(query,value)
        conn.commit()
        QMessageBox.information(QMessageBox(),'Successful','Record Updated Successful')
        conn.close()
        self.close()
        
class Mainclass(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainclass, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        header = self.tableWidgetUser.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # PAGE 1
        self.secondWindow = Updaterecords()
        self.dash.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.dashboard))
        self.dailyInput.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.records))
        self.btnAdd.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.userReg))
        self.btnUser.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.userManipulation))
        self.manipulate.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.manipulation))
        self.saveRecord.clicked.connect(self.add_rec)
        self.saveUser.clicked.connect(self.add_u)
        self.refreshbtn.clicked.connect(self.showrecords)
        self.refreshbtn_2.clicked.connect(self.showUserData)
        self.btnFindCounty.clicked.connect(self.showrecordsByCounty)
        self.findByMail.clicked.connect(self.showrecordsByemail)
        self.deleteByMail.clicked.connect(self.deleteUser)
        self.btnFindDate.clicked.connect(self.showrecordsByDate)
        self.deletebtn.clicked.connect(self.deleteRecord)
        self.mapView.clicked.connect(self.openMapView)
        self.refreshPage.clicked.connect(self.refreshPg)
        self.update.clicked.connect(self.updateRec)
        
        self.comboSearchBtn.clicked.connect(self.initiateCountySum)
        self.showrecords();
        self.showUserData();
        self.totalPositiveSum();
        self.recoveredSum();
        self.recoveredDeceased();

    def openMapView(self):
        self.g = Geoclass()
        self.g.show()
 
    def add_rec(self):
        try:
            date = self.date.text()
            county = self.countyName.currentText()
            latitude=float(self.lat.text())
            longitude=float(self.long_2.text())
            new=float(self.newInfe.text())
            recovered=float(self.recovered.text())
            deceased=float(self.deceased.text())
            info= self.infotxt.toPlainText()
            pop= self.popComment.toPlainText()
            self.add_records(date, county,latitude,longitude, new, recovered, deceased, info, pop)
        except ValueError:
            print("error")
            self.recordsErrorHandler.setText("Latitude, longitude,newCases,Recovered and Deceased must be Integers ")
            return False

        self.date.clear()
        self.countyName.clear()
        self.lat.clear()
        self.long_2.clear()
        self.newInfe.clear()
        self.recovered.clear()
        self.deceased.clear()
        self.infotxt.clear()
        self.popComment.clear()
    def add_u(self):
        mail = self.userEmail.text()
        password = self.userPassword.text()
        self.add_users(mail, password)
        self.userEmail.clear()
        self.userPassword.clear()
    def add_users(self, mail, password):
        try:
            query = "INSERT INTO login (username, password) VALUES (?, ?)"
            cursor.execute(query, (mail, password))
            conn.commit()
            self.userErrorHandler.clear()
            self.userSuccessHandler.setText("User added successfully! ")
            self.showUserData();
        except Exception:
            self.userSuccessHandler.clear()
            self.userErrorHandler.setText("Duplicated credentials are not allowed! ")
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add user.')
            print("Duplicated values")
    def add_records(self,date, county,latitude,longitude, new, recovered, deceased, info, pop):
        query = "INSERT INTO records (date, county,latitude,longitude, new, recovered, deceased, info, pop) VALUES (?, ?,?,?,?,?,?,?,?)"
        cursor.execute(query, (date, county,latitude,longitude, new, recovered, deceased, info, pop))
        conn.commit()
        QMessageBox.information(QMessageBox(),'Successful','Record added Successful')
        self.showrecords();
    def showrecords(self):
        self.connection = sqlite3.connect("users.db")
        query = "SELECT id,county,date,latitude,longitude,new,recovered,deceased,info,pop FROM records"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
    def updateRec(self):
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            myid= self.id.text()
            query = "SELECT id,county,date,latitude,longitude,new,recovered,deceased,info,pop FROM records WHERE id LIKE '"+myid+"' "
            cursor.execute(query)
            data = cursor.fetchmany()
        
            Rid = data[0][0]
            date= data[0][2]
            county= data[0][1]
            lat= data[0][3]
            longi= data[0][4]
            new= data[0][5]
            rec= data[0][6]
            death= data[0][7]
            info= data[0][8]
            pop=data[0][9] 

            self.secondWindow.Recorddate.setText(date)
            self.secondWindow.Recordcounty.setText(county)
            self.secondWindow.Recordlat.setText(str(lat))
            self.secondWindow.Recordlong.setText(str(longi))
            self.secondWindow.Recordnew.setText(str(new))
            self.secondWindow.Recordrec.setText(str(rec))
            self.secondWindow.Recorddeath.setText(str(death))
            self.secondWindow.Recordinfo.setText(info)
            self.secondWindow.Recordpop.setText(pop)
            self.secondWindow.Recordid.setText(str(Rid))
            self.secondWindow.displayInfo()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could find Record for Specified ID.')
          
            
        conn.close()
    def showUserData(self):
        self.connection = sqlite3.connect("users.db")
        query = "SELECT * FROM login"
        result = self.connection.execute(query)
        self.tableWidgetUser.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetUser.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetUser.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
    def showrecordsByemail(self):
        mail = self.lineFindByEmail.text()
        self.connection = sqlite3.connect("users.db")
        query = "SELECT * FROM login WHERE username LIKE '"+mail+"'"
        result = self.connection.execute(query)
        self.tableWidgetUser.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidgetUser.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidgetUser.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
    def showrecordsByCounty(self):
        eneo = self.lineFindBycounty.currentText()
        self.connection = sqlite3.connect("users.db")
        query = "SELECT id,county,date,latitude,longitude,new,recovered,deceased,info,pop FROM records WHERE county LIKE '"+eneo+"'"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()
    def showrecordsByDate(self):
        mydate = self.findbydate.text()
        self.connection = sqlite3.connect("users.db")
        query = "SELECT id,county,date,latitude,longitude,new,recovered,deceased,info,pop FROM records WHERE date LIKE '"+mydate+"'"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
        self.connection.close()    
    def deleteRecord(self):
        deldate = self.deleteDate.text()
        delcounty = self.deleteCounty.currentText()
        try:
            self.connection = sqlite3.connect("users.db")
            query = "DELETE from records WHERE date LIKE '"+deldate+"' and county LIKE '"+delcounty+"'"
            result = self.connection.execute(query)
            self.connection.commit()
            self.connection.close()
            QMessageBox.information(QMessageBox(),'Successful','Deleted From Table Successful')
            self.showrecords();
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete Record from the database.')
    def deleteUser(self):
        mail = self.lineeditmail.text()
        try:
            self.connection = sqlite3.connect("users.db")
            query = "DELETE from login WHERE username LIKE '"+mail+"'"
            result = self.connection.execute(query)
            self.connection.commit()
            self.connection.close()
            QMessageBox.information(QMessageBox(),'Successful','Deleted user Successful')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete user from the database.')


    ###########################   sum  ########################################
    def totalPositiveSum(self):
        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT SUM(new) FROM records")
            rows = cur.fetchone()
            for row in rows:
                self.positiveCases.setNum(row)
            cur.close()
            conn.close()
        except Exception:
             print("newCases are null")
    def recoveredSum(self):
        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT SUM(recovered) FROM records")
            rows = cur.fetchone()
            for row in rows:
                self.recoveredCases.setNum(row)
            cur.close()
            conn.close()
        except Exception:
             print("Recovered Cases are null")
    def recoveredDeceased(self):
        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT SUM(deceased) FROM records")
            rows = cur.fetchone()
            for row in rows:
                self.deseasedCases.setNum(row)
            cur.close()
            conn.close()
        except Exception:
             print("Decesed Cases are null")
    ###########################   sum at County Based  ########################################
    def initiateCountySum(self):
        cnty= self.countySearchCombo.currentText()
        self.totalPositiveCounty(cnty)
        self.totalRecoveredCounty(cnty)
        self.totalDeceasedCounty(cnty)
    def totalPositiveCounty(self, cnty):
        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT SUM(new) FROM records WHERE county  LIKE '"+cnty+"'")
            rows = cur.fetchone()
            for row in rows:
                self.newCombo.setNum(row)
            cur.close()
            conn.close()
        except Exception:
             QMessageBox.warning(QMessageBox(), 'CoTrac', 'No Record found for the selected county.')
    def totalRecoveredCounty(self, cnty):
        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT SUM(recovered) FROM records WHERE county  LIKE '"+cnty+"'")
            rows = cur.fetchone()
            for row in rows:
                self.recCombo.setNum(row)
            cur.close()
            conn.close()
        except Exception:
            print("No Record Found")
    def totalDeceasedCounty(self, cnty):
        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT SUM(deceased) FROM records WHERE county  LIKE '"+cnty+"'")
            rows = cur.fetchone()
            for row in rows:
                self.decesedCombo.setNum(row)
            cur.close()
            conn.close()
        except Exception:
            print("No Record Found")


    def refreshPg(self):
        self.w = Mainclass()
        self.w.show()
        self.hide()
class MyActions(login.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyActions, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.create_tableUser()
        self.create_tableRecords()
        
        self.loginbtn.clicked.connect(self.login)
        

    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    def create_tableUser(self):
        query = "CREATE TABLE IF NOT EXISTS login(username VARCHAR UNIQUE, password VARCHAR)"
        cursor.execute(query)
        conn.commit()
    def create_tableRecords(self):
        query = "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, county VARCHAR, date VARCHAR, latitude INTEGER,longitude INTEGER,new INTEGER,recovered INTEGER,deceased INTEGER, info VARCHAR, pop VARCHAR)"
        cursor.execute(query)
        conn.commit()

    def add_us(self):
        username = input("New username: ")
        password = input("New password: ")
        self.add_user(username, password)
    def add_user(self, username, password):
        
        query = "INSERT INTO login (username, password) VALUES (?, ?)"
        cursor.execute(query, (username, password))
        conn.commit()

    def check_user(self, username, password):
        query = 'SELECT * FROM login WHERE username = ? AND password = ?'
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        conn.commit()
        print('[DEBUG][check] result:', result)
        return result

    def login(self):
        username = self.email.text()
        password = self.pin.text()
        if self.check_user(username, password):
            self.errorsms.setText("You are logged in")
            self.w = Mainclass()
            self.w.show()
            self.hide()
        else:
            self.errorsms.setText("Check your credentials! ")
    
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qt_app=MyActions()
    qt_app.show()
    app.exec_()