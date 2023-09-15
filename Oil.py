# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
#from PyQt5.QtWidgets import QMainWindow
#from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_Oil import Ui_MainWindow
import sys
import 影响规律
import math

#class MouseEvent(QMouseEvent):
#    def __init__(self):
#    closeApp = pyqtSignal()
#class Communicate(QObject):
#    open = pyqtSignal()
#class F1(QWidget):
#class MyToolBox(QToolBox):   
#   def __init__(self): 
#        
#        lv = QListWidget() 
#        toolbox1 = QToolBox() 
#        toolbox1.setGeometry(0, 0, 81, 561)
#        toolbox1.addItem(lv,"111")  
#        toolbox1.addItem(groupbox2,"设计与校核")  
#        toolbox1.addItem(groupbox3,"影响规律")
#        toolbox1.addItem(groupbox3,"井段计算")
        
    

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.base()
        Buttons = self.stackedWidget.findChildren(QAbstractButton) 
        self.wow1 = Buttons[0]
        self.wow2 = Buttons[7]
        self.wow3 = Buttons[8]
        self.wow4 = Buttons[9]
        self.wow1.installEventFilter(self)
        self.wow2.installEventFilter(self)
        self.wow3.installEventFilter(self)
        self.wow4.installEventFilter(self)
        self.influence_law = 影响规律.Form()
#        self.First.mousePressEvent(self.button())

#        self.btn = []
#        self.btn = self.findChildren(QToolBoxButton)
 #        self.counter = self.btn.count()
#        print(self.btn)
#        self.b = QToolBox()
#        for i in self.btn:
#            
#            print(self.counter)
##        
#        QWidget.mousePressEvent
#    def mousePressEvent(self, event):
#        self.i = self.toolBox.currentIndex()
#        sender = self.sender()
#        if sender = self.First and self.i !=5 :
#            self.stackedWidget.setCurrentIndex(5)
#        if sender = self.Third

        
#        if event.button() = self.First:
#            self.clicked.emit(True)
#            
#        print(self.i)
        
#    @pyqtSlot()
#    def on_First_mousePressEvent(self, event):
#        i = self.stackedWidget.currentIndex()
#        print(i)
#        if event.button() == Qt.LeftButton :
#            self.stackedWidget.setCurrentIndex(7)
#        if event.type() == QEvent.MouseButtonPress: 
#                mouseEvent = QMouseEvent(event)     
#                if mouseEvent.buttons() == Qt.LeftButton and i !=7 :
#                    self.stackedWidget.setCurrentIndex(7)    
    @pyqtSlot()
    def eventFilter(self, obj, event):
#        u = self.stackedWidget.currentIndex()
        if obj == self.wow1:
            if event.type() == QEvent.MouseButtonPress:    
                    self.stackedWidget.setCurrentIndex(7)
                    
        if obj == self.wow2:
            if event.type() == QEvent.MouseButtonPress: 
                self.stackedWidget.setCurrentIndex(8)
        if obj == self.wow3:
            if event.type() == QEvent.MouseButtonPress: 
                self.influence_law.show()
                return  QMainWindow.eventFilter(self, obj, event)  
                return
        if obj == self.wow4:
            if event.type() == QEvent.MouseButtonPress: 
                self.stackedWidget.setCurrentIndex(10)
        return  QMainWindow.eventFilter(self, obj, event)   

#self.QWidget.mousePressEvent (self, QMouseEvent)    
#    def mousePressEvent(self, e):
#        print(1)
#    def  wow(self):
#        self.First.mousePressEvent.connect(self.stackedWidget.setCurrentIndex(7))
#    def on_First_mousePressEvent(self, e):
#        self.stackedWidget.setCurrentIndex(7)
#        print(7)
            
#    @pyqtSlot(int)
#    def on_toolBox_currentChanged(self, index):
#        """
#        Slot documentation goes here.
#        
#        @param index DESCRIPTION
#        @type int
#        """
#        
#        
#        i = self.toolBox.currentIndex()
##        j = self.stackedWidget.currentIndex()
#        if i == 2:
#            
#            #这是很重要的，点了一个窗口关闭后，自动还原成原先的，比如TAB1打开后，点TAB3，关闭后显示TAB1 的内容，还有
#            #TAB2的点开后再点TAB3，关闭TAB3弹出的窗口后，自动还原成TAB2的画面！！！！         
#            return
#        
#        if self.toolBox.tab.clicked:
#        print('LOL')
#        self.stackedWidget.setCurrentIndex(i+7)
        
    @pyqtSlot(int)
    def on_listWidget_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.
        
        @param currentRow DESCRIPTION
        @type int
        """      
#        self.toolBox.itemClicked
        self.Fourth = QtWidgets.QWidget()
        self.Fourth.setObjectName("First")
        self.toolBox.removeItem(3)
        self.toolBox.addItem(self.Fourth, '111')
#        self.toolBox.item().setVisible(False)
        i = self.listWidget.currentRow()
        self.stackedWidget.setCurrentIndex(i+1)


    
    @pyqtSlot()
    def on_radioButton_17_clicked(self):
        """
        Slot documentation goes here.
        """
        self.label_78.setText('动切力(Pa)')
        self.label_79.setText('塑性粘度(mpa.s)')
    
    @pyqtSlot()
    def on_radioButton_18_clicked(self):
        """
        Slot documentation goes here.
        """
        self.label_78.setText('流性指数')
        self.label_79.setText('稠度系数(Pa.s^n)')
    
    @pyqtSlot()
    def on_radioButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tableWidget_16.setItem(0, 2,  QTableWidgetItem('实际值'))
        self.tableWidget_16.setItem(1, 0,  QTableWidgetItem('环空返速(m/s)'))
        self.tableWidget_16.setItem(2, 0,  QTableWidgetItem('钻井泵排量(L/min)'))
        self.tableWidget_16.setItem(3, 0,  QTableWidgetItem('止动环空返速(m/s)'))
        self.tableWidget_16.setItem(4, 0,  QTableWidgetItem('岩屑床厚度(mm)'))
        self.tableWidget_16.setItem(5, 0,  QTableWidgetItem(''))

    @pyqtSlot()
    def on_radioButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tableWidget_16.setItem(0, 2,  QTableWidgetItem('备注'))
        self.tableWidget_16.setItem(1, 0,  QTableWidgetItem('临界环空返速(m/s)'))
        self.tableWidget_16.setItem(2, 0,  QTableWidgetItem('临界排量'))
        self.tableWidget_16.setItem(3, 0,  QTableWidgetItem('止动环空返速(m/s)'))
        self.tableWidget_16.setItem(4, 0,  QTableWidgetItem('止动环空排量(L/min)'))
        self.tableWidget_16.setItem(5, 0,  QTableWidgetItem('临界岩屑床厚度(mm)'))
        
    @pyqtSlot()
    def on_pushButton_20_clicked(self):
        """
        Slot documentation goes here.
        """
        
#    def judgeEvent(self):
        
    @pyqtSlot()
    def on_pushButton_20_clicked(self):
        """
        Slot documentation goes here.
        """
        self.base()
        self.calculate()
        self.items1 = ['层流流态', '过渡流态', '紊流流态']
        self.items2 = ['层流流态', '紊流流态']
#        self.base()
        if self.θ <= 30:
            
            self.wow, ok = QInputDialog.getItem(self, '请选择流态', '选择', self.items1, 0, True)#0,1,2选择不同的Item
            if self.wow[0]=='层':
                print(self.wow)
            elif self.wow[0]=='过':
                print(self.wow)
            else:
                print(self.wow)
        if self.θ > 30 :
            self.wow, ok = QInputDialog.getItem(self, '请选择流态', '选择', self.items2, 0, True)#0,1,2选择不同的Item
            if self.wow[0]=='层':
                print(self.wow)
            else :
                print(self.wow)
            
            
            
            
#    def setbase1(self):
#        '校核模式'
#        self.base()
#        self.tableWidget_5.setItem(1, 1, QTableWidgetItem(self.Va))
#        self.tableWidget_5.setItem(2, 1, QTableWidgetItem(self.Q))
#        self.tableWidget_5.setItem(3, 1, QTableWidgetItem(self.Vp))
#        self.tableWidget_5.setItem(4, 1, QTableWidgetItem(self.Hb))
#        self.tableWidget_5.setItem(1, 2, QTableWidgetItem(self.Vp))
#        self.tableWidget_5.setItem(2, 2, QTableWidgetItem(self.Qp))
#        self.tableWidget_5.setItem(3, 2, QTableWidgetItem(self.Vp))
#        self.tableWidget_5.setItem(4, 2, QTableWidgetItem(self.Hb))
#    def setbase2(self):
#        '设计模式'
#        self.base()
#        self.tableWidget_5.setItem(1, 1, QTableWidgetItem(self.Vc))
#        self.tableWidget_5.setItem(2, 1, QTableWidgetItem(self.Qc))
#        self.tableWidget_5.setItem(3, 1, QTableWidgetItem(self.Vp))
#        self.tableWidget_5.setItem(4, 1, QTableWidgetItem(self.Qp))
#        self.tableWidget_5.setItem(5, 1, QTableWidgetItem(self.Hb)) 
        
    @pyqtSlot()
    def on_pushButton_30_clicked(self):
        """
        Slot documentation goes here.
        """
        self.base()
        self.tableWidget_4.setItem(0, 1, QTableWidgetItem(self.my_str))
        self.tableWidget_4.setItem(2, 1, QTableWidgetItem(self.dh))
        self.tableWidget_4.setItem(3, 1, QTableWidgetItem(self.dp))
        self.tableWidget_4.setItem(4, 1, QTableWidgetItem(self.ρm))
        self.tableWidget_4.setItem(5, 1, QTableWidgetItem(self.τ0))
        self.tableWidget_4.setItem(6, 1, QTableWidgetItem(self.μpv))
        self.tableWidget_4.setItem(7, 1, QTableWidgetItem(self.ds))
        self.tableWidget_4.setItem(8, 1, QTableWidgetItem(self.e))
        self.tableWidget_4.setItem(9, 1, QTableWidgetItem(self.Ca))
        self.tableWidget_4.setItem(10, 1, QTableWidgetItem(self.Vrop))
        self.tableWidget_4.setItem(11, 1, QTableWidgetItem(self.N))
        self.tableWidget_4.setItem(12, 1, QTableWidgetItem(self.ρs))
        self.tableWidget_4.setItem(13, 1, QTableWidgetItem(self.ds))
        self.tableWidget_4.setItem(14, 1, QTableWidgetItem(self.C))
        
    
    @pyqtSlot()
    def on_pushButton_16_clicked(self):
        """
        Slot documentation goes here.
        """
        self.base()
        self.tableWidget_15.setItem(1, 1, QTableWidgetItem(self.θ))


    def base(self):
        self.θ = self.lineEdit_64.text()
        self.my_str = self.lineEdit_65.text()
        self.dh = self.lineEdit_66.text()
        self.dp = self.lineEdit_67.text()
        self.e = self.lineEdit_68.text()
        self.ρm= self.lineEdit_69.text()
        self.lineEdit_69.setText('5')
        self.Ca = self.lineEdit_72.text()
        self.Vrop = self.lineEdit_73.text()
        self.N = self.lineEdit_74.text()
        self.Q = self.lineEdit_75.text()
        self.ρs = self.lineEdit_76.text()
        self.ds = self.lineEdit_77.text()
        self.C = self.lineEdit_78.text()
        self.lineEdit_76.setText('0.2')
        
        self.f = self.lineEdit_80.text()#床与井壁间摩擦系数
        self.lineEdit_77.setText('0.37')
        self.Pbed1 = self.lineEdit_79.text()#岩屑床孔隙度
       
        
#        
#        
#        if self.radioButton_8.isChecked:
#            self.k = self.lineEdit_25.text()
#            self.n = self.lineEdit_24.text()
#            self.k = float(self.k)
#            self.n = float(self.n)
#            self.μav2 = self.k*(math.pow(12*self.Va/(self.dh-self.dp), (self.n)-1))*(math.pow(2*(self.n)+1/3*(self.n), n))
#        elif self.radioButton_7.isChecked:
#            self.τ0 = self.lineEdit_24.text()
#            self.μpv = self.lineEdit_25.text()
#            self.τ0 = float(self.τ0)
#            self.μpv = float(self.μpv)
#            self.μav1 = self.μpv+self.τ0*(self.dh-self.dp)*0.112/self.Va
        
        
        
        
        
        
        
    def  calculate(self):
        try :
            self.θ = float(self.θ)
            self.my_str = float(self.my_str)
            self.dh = float(self.dh)
            self.dp = float(self.dp)
            self.e = float(self.e)
            self.ρm = float(self.ρm)
            self.Ca = float(self.Ca)
            self.Vrop = float(self.Vrop)
            self.N = float(self.N)
            self.Q = float(self.Q)
            self.ρs = float(self.ρs)
            self.ds = float(self.ds)
            self.C = float(self.C)
            self.f = float(self.f)
            self.pbed1 = float(self.pbed1)
            self.pbed1 = float(self.pbed1)
            self.Cang = 0.0342*self.θ-0.000233*self.θ**2-0.213
            self.Cang30 = 0.0342*30-0.000233*900-0.213
            self.Csize = 1.286 - 0.0409448*self.ds
            self.Crpm = (600-self.N)/600
            self.θ = self.θ/180* (math.pi)
            self.i1 = (10/180)*(math.pi)
            self.i2 = (30/180)*(math.pi)
            self.i3= (65/180)*(math.pi)
            self.Va = 1273.2*self.Q/((math.pow(self.dh, 2)-(math.pow(dp, 2))))
        except Exception as e :
            print('Invaild input:', e)
            print('please try again') 
            
    @pyqtSlot()
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        self.base()
        self.calculate()
        
        
        self.Va = 1273.2*self.Q/((math.pow(self.dh, 2))-(math.pow(self.dp, 2)))
        self.Vs1 = 0.32681*(math.pow(self.ds, 2))*(self.ρs-self.ρm)/(self.μav1)
        self.Vs2 = 0.07068*ds*(math.pow((ρs-ρm), 0.6667))/(math.pow(ρm*μav1, 0.3333))
        self.Vs3 = 0.0813*(ds*(math.pow(ρs-ρm), 0.5))/(math.pow(ρm, 0.5))
        self.Vs12 = 0.32681*(math.pow(self.ds, 2))*(self.ρs-self.ρm)/(self.μav2)
        self.Vs22 = 0.07068*ds*(math.pow((ρs-ρm), 0.6667))/(math.pow(ρm*μav2, 0.3333))
        self.Vamin1 = self.Vrop/self.Ca*(1-(math.pow((self.dp/self.dh), 2)))+1.25*self.Vs1 
        self.Vamin2 = self.Vrop/self.Ca*(1-(math.pow((self.dp/self.dh), 2)))+1.25*self.Vs2
        self.Vamin3 = self.Vrop/self.Ca*(1-(math.pow((self.dp/self.dh), 2)))+1.25*self.Vs3
        self.Vamin12 = self.Vrop/self.Ca*(1-(math.pow((self.dp/self.dh), 2)))+1.25*self.Vs12
        self.Vamin22 = self.Vrop/self.Ca*(1-(math.pow((self.dp/self.dh), 2)))+1.25*self.Vs22
        self.Qmin1 = self.Vamin1*((math.pow(self.dh, 2))-(math.pow(self.dp, 2)))/1273.2
        self.Qmin2 = self.Vamin2*((math.pow(self.dh, 2))-(math.pow(self.dp, 2)))/1273.2
        self.Qmin3 = self.Vamin3*((math.pow(self.dh, 2))-(math.pow(self.dp, 2)))/1273.2
        self.Qmin12 = self.Vamin12*((math.pow(self.dh, 2))-(math.pow(self.dp, 2)))/1273.2
        self.Qmin22 = self.Vamin22*((math.pow(self.dh, 2))-(math.pow(self.dp, 2)))/1273.2
        
        self.Vt = self.Vrop*math.pow(self.dh, 2)/self.Cconc*((math.pow(dh, 2) - (math.pow(dp, 2))))
        self.Vc = self.Vt +self.Vsc  
        self.Vsc30 = self.Vse1
        self.Vc30 = self.Vt + self.Vsc30
        self.E = self.e/(self.dh-self.dp)
        self.μav1 = self.μpv+self.τ0*(self.dh-self.dp)*0.112/self.Va
        self.μav2 = self.k*(math.pow(12*self.Va/(self.dh-self.dp), (self.n)-1))*(math.pow(2*(self.n)+1/3*(self.n), n))
        
        self.Hb21 = 0.015*self.dh*(self.μav1+6.15*math.pow(self.μav1, 0.5))*(1+0.587*self.E)*(self.Vc-self.Va)#θ大于65
        self.Hb22 = 0.015*self.dh*(self.μav2+6.15*math.pow(self.μav2, 0.5))*(1+0.587*self.E)*(self.Vc-self.Va)#θ大于65
        self.Hb11 = 0.01*(self.dh)(3221*math.pow(self.μav1, 2)-442*(self.μav1)+44)*(1+0.587*self.E)*(2.33-2.12*self.Va)-5.0
        self.Hb12 = 0.01*(self.dh)(3221*math.pow(self.μav2, 2)-442*(self.μav2)+44)*(1+0.587*self.E)*(2.33-2.12*self.Va)-5.0
        self.rh = self.dh/2
        self.a = 2*math.sqrt((math.pow(self.rh, 2))-(math.pow((self.rh-self.Hb), 2)))
        self.Ae = math.pow(self.rh, 2)*(math.acos((self.rh-self.Hb1)/self.rh)-(self.rh-self.Hb1)*math.sqrt(2*self.rh*self.Hb1-(math.pow(self.Hb), 2))/math.pow(self.rh, 2))
        self.Vp1 = ((9.80665*self.Ae*self.C*self.g*(math.cos(self.θ)-self.f*math.sin(self.θ))/self.a)-1.5*self.τ0)*(self.dh-self.dp)/(12*self.μpv)
        self.Vp2 = (9.80665*0.001*self.Ae*self.C*self.g*(math.cos(self.θ)-self.f*math.sin(self.θ))*(self.n*(self.dh-self.dp)))*(self.ρs-self.ρm)/(4*self.a*self.k*(2*self.n+1))
        self.Qp1 = self.Vp1*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
        self.Qp2 = self.Vp2*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
        self.Vc21 = 0.4*(math.pow((((self.ρs-self.ρm)/self.ρm)*self.ds), 0.6667))*((1+0.71*self.θ+0.55*math.sin(2*self.θ))/(math.pow(self.ρm*self.μav1, 0.3333)))
        self.Vc22 = 0.4*(math.pow((((self.ρs-self.ρm)/self.ρm)*self.ds), 0.6667))*((1+0.71*self.θ+0.55*math.sin(2*self.θ))/(math.pow(self.ρm*self.μav2, 0.3333)))
        self.Qs = self.Va*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
       
            
        
        
#        if self.Hb <=0 :
#            self.Hb = 0
#            
#        
#        if  self.pbed1 != '':
#            self.pbed = self.pbed1
#        print(self.pbed)
        
#        if self.ρm <= 1.0425:
#            self.Cdenf = 1
#        else :
#            self.Cdenf = 1-0.27799*(self.ρm-1.0425)
            
        if self.θ <= self.i1 :
            self.judgeEvent()
            
        if  self.i1 < self.θ <=self.i2 :
            self.judgeEvent10()
            
        if  self.i2 < self.θ <=self.i3 :
            self.judgeEvent30()
            
        if  self.θ > self.i3 :
            self.judgeEvent65()
        
    def judgeEvent(self):
        if self.wow[0]=='层' and self.radioButton_7.isChecked and self.radioButton_9.isChecked  :
            '1'
            self.Rt1 = (self.Va-self.Vs1)/self.Va
        
            self.Rt2 = (self.Va-self.Vs2)/self.Va
            self.Rt3 = (self.Va-self.Vs3)/self.Va
            self.Rt12 = (self.Va-self.Vs12)/self.Va
            self.Rt22 = (self.Va-self.Vs22)/self.Va
            self.Vamin = self.Vrop/self.Ca*(1-(math.pow((self.dp/self.dh), 2)))+1.25*self.Vs1
            
            if self.Rt1 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
            self.Hb = 0
            self.setbase1()
            
            
            
            
        elif self.wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked :
            '2'
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs1
            if self.Rt1 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
            self.Hb = 0
                
            self.setbase2()
            
        elif self.wow[0]=='过' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked :
            '3'
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs2
            if self.Rt2 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
            self.Hb = 0    
            self.setbase1()
            
        elif self.wow[0]=='过' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked :
            '4'
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs2
            if self.Rt2 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
            self.Hb = 0    
              
            self.setbase2()    
        
        elif wow[0]=='紊' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked  :
            μav1
            '5'
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs3
            if self.Rt3 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
                
            self.Hb = 0    
            self.setbase1()
                
        elif wow[0]=='紊' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked  :
            '6'
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs3
            if self.Rt3 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
                
            self.Hb = 0    
            self.setbase1()
                
                
        if self.wow[0]=='层' and self.radioButton_8.isChecked and self.radioButton_10.isChecked  :
            μav1
            '7'
            
            self.Vamin = self.Vrop/self.Ca*(1-(math.pow((self.dp/self.dh), 2)))+1.25*self.Vs12
            if self.Rt12 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
                
            self.Hb = 0    
            self.setbase2()
            
            
            
            print(self.Vs)
        elif self.wow[0]=='层' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked  :
            '8'
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs12
            
            if self.Rt12 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
            self.Hb = 0    
            self.setbase2()
            
        elif self.wow[0]=='过' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked  :
            '9'
            self.Vamin = (self.Vrop/self.Ca*(1-(math.pow(self.dp/self.dh), 2)))+1.25*self.Vs22
            if self.Rt22 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
                
            self.Hb = 0    
            self.setbase2()
            
        elif self.wow[0]=='过' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked  :
            '10'
            
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs22
            if self.Rt22 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
                
            self.Hb = 0    
            self.setbase2()   
        
        elif wow[0]=='紊' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked  :
            μav1
            '11'
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs3
            if self.Rt3 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textEdit.setText('不安全')
            self.Hb = 0    
            self.setbase2()
                
        elif wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked :
            '12'
            
            self.Vamin = (self.Vrop/self.Ca*(1-(self.dp/self.dh)**2))+1.25*self.Vs3
            if self.Rt3 > 0.5 :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.Hb = 0    
            self.setbase2()
                 
    def judgeEvent10(self):
        if wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked  :
            '1,层  宾  校核'
            self.Vs
            self.Vsc = self.Vs1 + self.θ*(self.Vsc30-self.Vs1)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase1()    
        elif wow[0]=='层' and self.radioButton_8.isChecked() and self.radioButton_9.isChecked:
            '2'
            
            self.Vsc = self.Vs12 + self.θ*(self.Vsc30-self.Vs12)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase1()   
        elif wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked  :
            '3'
            self.Vs
            self.Vsc = self.Vs1 + self.θ*(self.Vsc30-self.Vs1)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase2()   
        elif wow[0]=='层' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked  :
            '4'
            self.Vs
            self.Vsc = self.Vs12 + self.θ*(self.Vsc30-self.Vs12)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase2()   
        elif wow[0]=='过' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked  :
            '5'
            self.Vs
            self.Vsc = self.Vs2 + self.θ*(self.Vsc30-self.Vs2)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase1()   
        elif wow[0]=='过' and self.radioButton_8.isChecked() and self.radioButton_9.isChecked :
            '6'
            self.Vs
            self.Vsc = self.Vs22 + self.θ*(self.Vsc30-self.Vs22)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase1()   
        elif wow[0]=='过' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked  :
            '7'
            self.Vs
            self.Vsc = self.Vs2 + self.θ*(self.Vsc30-self.Vs2)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase2()   
        elif wow[0]=='过' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked  :
            '8'
            self.Vs
            self.Vsc = self.Vs22 + self.θ*(self.Vsc30-self.Vs22)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase2()   
        elif wow[0]=='紊' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked :
            '9'
            self.Vs
            self.Vsc = self.Vs3 + self.θ*(self.Vsc30-self.Vs3)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase1()   
        elif wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_9.isChecked :
            '10'
            self.Vs
            self.Vsc = self.Vs3 + self.θ*(self.Vsc30-self.Vs3)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase1()   
        elif wow[0]=='紊' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked  :
            '11'
            self.Vs
            self.Vsc = self.Vs3 + self.θ*(self.Vsc30-self.Vs3)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase2()   
        elif wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked :
            '12'
            self.Vs
            self.Vsc = self.Vs3 + self.θ*(self.Vsc30-self.Vs3)/30
            self.Vc = self.Vsc + self.Vt
            if self.Va >= self.Vc :
                self.textEdit.setText('安全')
            else :
                self.textdit.setText('不安全')  
            self.setbase2() 
        
#    def judgeEvent30(self):
#        if wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked  :
#            '1'
#            self.Vc
#            
#        elif wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_9.isChecked  :
#        elif wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked  :
#        elif wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked  :
#        elif wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked  :
#        elif wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_9.isChecked  :
#        elif wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked :
#        elif wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked :
#        
        
#    def  judgeEvent65(self):
#        Hb = 
#        
#        if self.wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked() :
#            '1'
#            
#            self.Qc = self.Vc21*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
#            
#        elif self.wow[0]=='紊' and self.radioButton_7.isChecked() and self.radioButton_9.isChecked() : 
#            '2'
#            self.Qc = self.Vc21*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
#        elif self.wow[0]=='层' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked() : 
#            '3'
#            self.Qc = self.Vc21*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
#        elif self.wow[0]=='紊' and self.radioButton_7.isChecked() and self.radioButton_10.isChecked() : 
#            '4'
#            self.Qc = self.Vc21*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
#        elif self.wow[0]=='层' and self.radioButton_8.isChecked() and self.radioButton_9.isChecked() : 
#            '5'
#            self.Qc = self.Vc22*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
#        elif self.wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_9.isChecked() : 
#            '6'
#            self.Qc = self.Vc22*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
#        elif self.wow[0]=='层' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked() : 
#            '7'
#            self.Qc = self.Vc22*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
#        elif self.wow[0]=='紊' and self.radioButton_8.isChecked() and self.radioButton_10.isChecked() : 
#            '8'
#            self.Qc = self.Vc22*(math.pow(self.dh, 2)-math.pow(self.dp, 2))/1273.2
            
            
            
            

    
    @pyqtSlot()
    def on_action_2_triggered(self):
        """
        Slot documentation goes here.
        """
        QProcess.startDetached("D:\Python3\eric6\my_excel\calc")
        
    def update_graph(self):
        try :
            self.mpl.canvas.axes.clear()
            self.mpl.canvas.axes.grid(True) 
            a= [a for a in np.arange(self.num1, self.num2+self.num3, self.num3)]
            if self.radioButton_5.isChecked():
                
                self.mpl.canvas.axes.plot(a, self.Hblist)
            elif self.radioButton_6.isChecked():
                    self.mpl.canvas.axes.plot(a, self.Vplist)
            self.mpl.canvas.draw()
            
        
        except Exception as e :
            print('Invaild input: ', e)
            print('please try again')    
        
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
