# -*- codnum7ng: utf-8 -*-

"""
Module num7mplementnum7ng Form.
"""
from __future__ import with_statement

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *
import math
import sys
import numpy as np

from Ui_影响规律 import Ui_Form

class Form(QWidget,Ui_Form):
    """
    Class documentation goes here.
    """
 
    def __init__(self):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
    def paint(self):

        self.textEdit.append ('lol')
        
        
        
        
    def base(self):
        try:
            self.num1 = self.lineEdit.text()
            self.num2 = self.lineEdit_2.text()
            self.num3 = self.lineEdit_3.text()
            self.θ = self.lineEdit_4.text()
            self.my_str = self.lineEdit_5.text()
            self.dh = self.lineEdit_6.text()
            self.dp = self.lineEdit_7.text()
            self.e= self.lineEdit_8.text()
            self.Vrop = self.lineEdit_9.text()
            self.N = self.lineEdit_10.text()
            self.Q = self.lineEdit_11.text()
            if self.radioButton.isChecked():
                self.μpv = self.lineEdit_12.text()                
            elif self.radioButton_2.isChecked():
                self.τ0 = self.lineEdit_12.text()
            elif self.radioButton_3.isChecked():
                self.k = self.lineEdit_12.text()
            else :
                self.n = self.lineEdit_12.text()
                
            self.ρm = self.lineEdit_13.text()
            self.Cconc = self.lineEdit_14.text()
            self.ρs = self.lineEdit_15.text()
            self.ds = self.lineEdit_16.text()
            self.C = self.lineEdit_17.text()
            self.phd1 = self.lineEdit_18.text()
            self.f = self.lineEdit_19.text()
        except Exception as e :
            print('Invaild input: ', e)
            print('please try again')
        
    def cal(self):
        try : 
#            self.base()
            self.θ = float(self.θ)
            self.my_str = float(self.my_str)
            self.dh = float(self.dh)
            self.dp = float(self.dp)
            self.e= float(self.e)
            self.Vrop = float(self.Vrop)
            self.N = float(self.N)
            self.Q = float(self.Q)
            self.ρm = float(self.ρm)
            self.Cconc = float(self.Cconc)
            self.ρs = float(self.ρs)
            self.ds = float(self.ds)
            self.C = float(self.C)
            self.phd1 = float(self.phd1)
            self.f = float(self.f) 
            self.θ = self.θ/180* (math.pi)
            self.i1 = (30/180)*(math.pi)
            self.i2= (65/180)*(math.pi)
            self.i3 = (90/180)*(math.pi)
            self.num1 = float(self.num1)        
            self.num2 = float(self.num2)        
            self.num3 = float(self.num3)
#            self.Cconc = 0.01778*self.Vrop+0.505
            if self.radioButton.isChecked():
                self.μpv = float(self.μpv)
            elif self.radioButton_2.isChecked():
                self.τ0 = float(self.τ0)

            elif self.radioButton_3.isChecked():
                self.k = float(self.k)
        
            else :
                self.n = float(self.n)

            
            
        except Exception as e : 
            print('Invaild input:', e)
            print('please try again') 
               
            
        
        
    @pyqtSlot()
    def on_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.radioButton_5.setText('动切力与岩屑床厚度之间关系曲线')
        self.radioButton_6.setText('动切力与止动环空返速之间关系曲线')
        self.groupBox_3.setTitle('动切力(Pa)分析范围')
        self.label_11.setText('塑性粘度(mPa.s)')
        
    
    @pyqtSlot()
    def on_radioButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.radioButton_5.setText('塑性粘度与岩屑床厚度之间关系曲线')
        self.radioButton_6.setText('塑性粘度与止动环空返速之间关系曲线')
        self.groupBox_3.setTitle('塑性粘度(mPa*s)分析范围')
        self.label_11.setText('动切力(pa)')
    
    @pyqtSlot()
    def on_radioButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        self.radioButton_5.setText('流性指数与岩屑床厚度之间关系曲线')
        self.radioButton_6.setText('流性指数与止动环空返速之间关系曲线')
        self.groupBox_3.setTitle('流性指数分析范围')
        self.label_11.setText('塑性粘度(mPa.s^n)')
        

    
    @pyqtSlot()
    def on_radioButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        self.radioButton_5.setText('稠度系数与岩屑床厚度之间关系曲线')
        self.radioButton_6.setText('稠度系数与止动环空返速之间关系曲线')
        self.groupBox_3.setTitle('稠度系数(mPa*s^n)分析范围')
        self.label_11.setText('流性指数')

    
        
    def iter(self):
        try:
            while True :
                if self.μav < 53 :
                    self.Vse1   = 0.00516*self.μav +0.916
                    print('1st,Vse1 :', self.Vse1)
                    self.Vc = self.Vt + self.Vse1
                    self.μav = self.μpv + self.num8[self.num7-1]/((12*self.Vc/(self.dh-self.dp))+(self.num8[self.num7-1]/(2*self.μpv)))
                    print('loop,av1:', self.μav)
                    if self.μav < 53 :
                        self.Vse2  =  0.00516*self.μav +0.916
                        print('1st,Vse2 :', self.Vse2)
                    else :
                        self.Vse2 = 0.02554*(self.μav-53)+0.9997
                        print('1st,Vse2 :', self.Vse2)
                else : 
                    self.Vse1 = 0.02554*(self.μav-53)+0.9997
                    print('2st,Vse1 :', self.Vse1)
                    self.Vc = self.Vt + self.Vse1
                    self.μav = self.μpv + self.num8[self.num7-1]/(((12*self.Vc)/(self.dh-self.dp))+self.num8[self.num7-1]/(2*self.μpv))
                    print('loop,av2:', self.μav)
                    if self.μav < 53 :
                        self.Vse2  =  0.00516*self.μav +0.916
                        print('1st,Vse2 :', self.Vse2)
                    else :
                        self.Vse2 = 0.02554*(self.μav-53)+0.9997
                        print('1st,Vse2 :', self.Vse2)
                if abs(self.Vse1 - self.Vse2) <= 0.01 :
                    print('End   Vse1: , Vse2: ', self.Vse1, self.Vse2)
                    print('end av :', self.μav)
                    self.Vc = 0
                    self.Vse2 = 3
#                    self.Vc = self.Vt + self.Vse2
                    yield self.μav
                    
                    break
            
        except TypeError : pass 
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """ 
        self.base()
        self.cal()
#        self.Cconc = 0.01*self.Cconc
        self.Cconc = 0.01778*self.Vrop+0.505
        self.C = 0.01*self.C
        self.rh = self.dh/2
        self.E =self.e/(self.dh-self.dp)
        self.Vt = self.Vrop*math.pow(self.dh, 2)/(36*self.Cconc*((math.pow(self.dh, 2) - (math.pow(self.dp, 2)))))
        print('self.Vt: ', self.Vt)
        self.Va = 1273.2*self.Q/((math.pow(self.dh, 2)-(math.pow(self.dp, 2))))
        print('Va:', self.Va)
        self.Hblist = []
        self.Vplist = []     
        self.num4 = (self.num2) - (self.num1) + self.num3        #RANGE，比终止值多了一个，所以能刚好range到
        self.num5 = ((self.num4*100)/(self.num3*100)) + 1        
        self.tableWidget.setColumnCount(self.num5)                        
        self.num8 = [self.num8 for self.num8 in np.arange(self.num1, self.num2+self.num3, self.num3)]

        if self.θ < 0 :
            my_button=QMessageBox.information(self,'Warning','θ值有问题！请仔细核对!')
                
        elif 0 <= self.θ <= self.i1 :
            my_button=QMessageBox.information(self,'Warning','θ很小，不进行计算！')
            
        elif self.i1 < self.θ <= self.i2 :
            if self.radioButton.isChecked():
                item = QTableWidgetItem('动切力')
                self.tableWidget.setItem(1, 0, QTableWidgetItem(item))
                self.Vse2 = 3
                self.Vc = self.Vt + self.Vse2
                for self.num7 in  range(1, int(self.num5)):                                         
                    item1 = QTableWidgetItem('%s'%self.num7)
                    self.tableWidget.setItem(0, self.num7,  QTableWidgetItem(item1))
                    item2 = QTableWidgetItem('%s'%self.num8[self.num7-1])
                    self.tableWidget.setItem(1, self.num7,  QTableWidgetItem(item2))
                    if self.tableWidget.item(1, self.num5) == '':
                        self.tableWidget.setItem(1, self.num5,  QTableWidgetItem(self.num2))
                    
                    self.μav = self.μpv + self.num8[self.num7-1]/(((12*self.Vc)/(self.dh-self.dp))+self.num8[self.num7-1]/(2*self.μpv))
                    print('1st,av:', self.μav)
                    for self.μav  in  self.iter():  pass
                
                    self.Hb = 0.01*self.dh*((3.221*0.001*math.pow(self.μav, 2)-0.442*(self.μav)+44)*(1+0.587*self.E)*(2.33-2.12*self.Va)-5.0)
                    print('Hb:', self.Hb)
                    item3 = QTableWidgetItem("%s"%self.Hb)
                    self.tableWidget.setItem(2, self.num7,  QTableWidgetItem(item3))
                    self.a = 2*math.sqrt((math.pow(self.rh, 2))-(math.pow((self.rh-self.Hb), 2)))
                    print('a:', self.a)     
                    self.cos= (self.rh-self.Hb)/self.rh
                    self.Ae = math.pow(self.rh, 2)*(math.acos(self.cos)-((self.rh-self.Hb)*self.a/2)/math.pow(self.rh, 2))
                    print('Ae:', self.Ae)
                    self.Vp = 0.001*((9.80665**2*self.Ae*self.C*(self.ρs-self.ρm)*(math.cos(self.θ)-self.f*math.sin(self.θ))/self.a)-1.5*self.num8[self.num7-1])*(self.dh-self.dp)/(12*self.μpv)

                    item4 = QTableWidgetItem('%s'%self.Vp)
                    self.tableWidget.setItem(3, self.num7,  QTableWidgetItem(item4))
                    self.Hblist.append(self.Hb)
                    self.Vplist.append(self.Vp)
                print(self.Hblist)    
               
                
                
                
                
            elif self.radioButton_2.isChecked():
                item = QTableWidgetItem('塑性粘度')
                self.tableWidget.setItem(1, 0, QTableWidgetItem(item))
                for self.num7 in  range(1, int(self.num5)):                                         
                    item1 = QTableWidgetItem('%s'%self.num7)
                    self.tableWidget.setItem(0, self.num7,  QTableWidgetItem(item1))
                    item2 = QTableWidgetItem('%s'%self.num8[self.num7-1])
                    self.tableWidget.setItem(1, self.num7,  QTableWidgetItem(item2))
                    if self.tableWidget.item(1, self.num5) == '':
                        self.tableWidget.setItem(1, self.num5,  QTableWidgetItem(self.num2))
                    self.Vse2 = 3
                    self.Vc = self.Vt + self.Vse2
                    self.μav = self.num8[self.num7-1] + self.τ0*(self.dh-self.dp)/(12*self.Vc)
                    print('1st,av:', self.μav)
                    for self.μav  in  self.iter():  pass
                    self.Hb = 0.01*self.dh*((3.221*0.001*math.pow(self.μav, 2)-0.442*(self.μav)+44)*(1+0.587*self.E)*(2.33-2.12*self.Va)-5.0)
                    item3 = QTableWidgetItem('%s'%self.Hb)
                    self.tableWidget.setItem(2, self.num7,  QTableWidgetItem(item3))
                    self.a = 2*math.sqrt((math.pow(self.rh, 2))-(math.pow((self.rh-self.Hb), 2)))                   
                    self.cos= (self.rh-self.Hb)/self.rh
                    self.Ae = math.pow(self.rh, 2)*(math.acos(self.cos)-((self.rh-self.Hb)*self.a/2)/math.pow(self.rh, 2))
                    self.Vp = ((9.80665*self.Ae*self.C*9.80665*(math.cos(self.θ)-self.f*math.sin(self.θ))/self.a)-1.5*self.τ0)*(self.dh-self.dp)/(12*self.num8[self.num7-1])                   
                    item4 = QTableWidgetItem('%s'%self.Vp)
                    self.tableWidget.setItem(3, self.num7,  QTableWidgetItem(item4))
                    self.Hblist.append(self.Hb)
                    self.Vplist.append(self.Vp)
                    
                    
            elif self.radioButton_3.isChecked():
                item = QTableWidgetItem('流性指数')
                self.tableWidget.setItem(1, 0, QTableWidgetItem(item))
                for self.num7 in  range(1, int(self.num5)):                                         
                    item1 = QTableWidgetItem('%s'%self.num7)
                    self.tableWidget.setItem(0, self.num7,  QTableWidgetItem(item1))
                    item2 = QTableWidgetItem('%s'%self.num8[self.num7-1])
                    self.tableWidget.setItem(1, self.num7,  QTableWidgetItem(item2))
                    if self.tableWidget.item(1, self.num5) == '':
                        self.tableWidget.setItem(1, self.num5,  QTableWidgetItem(self.num2))
                    self.Vse2 = 3
                    self.Vc = self.Vt + self.Vse2
                    self.μav = self.k*math.pow((12*self.Vc/(self.dh-self.dp)+2*(self.num8[self.num7-1])/(3*self.num8[self.num7-1])), self.num8[self.num7-1]-1)
                    for self.μav  in  self.iter(): pass
                    self.Hb = 0.01*self.dh*((3.221*0.001*math.pow(self.μav, 2)-0.442*(self.μav)+44)*(1+0.587*self.E)*(2.33-2.12*self.Va)-5.0)
                    item3 = QTableWidgetItem('%s'%self.Hb)
                    self.tableWidget.setItem(2, self.num7,  QTableWidgetItem(item3))
                    self.cos= (self.rh-self.Hb)/self.rh
                    self.a = 2*math.sqrt((math.pow(self.rh, 2))-(math.pow((self.rh-self.Hb), 2)))                 
                    self.Ae = math.pow(self.rh, 2)*(math.acos(self.cos)-(self.rh-self.Hb)*math.sqrt(self.a/2)/math.pow(self.rh, 2))
                    self.Vp = (9.80665*0.001*self.Ae*self.C*9.80665*(math.cos(self.θ)-self.f*math.sin(self.θ))*(self.num8[self.num7-1]*(self.dh-self.dp)))*(self.ρs-self.ρm)/(4*self.a*self.k*(2*self.num8[self.num7-1]+1))                   
                    item4 = QTableWidgetItem('%s'%self.Vp)
                    self.tableWidget.setItem(3, self.num7,  QTableWidgetItem(item4))
                    self.Hblist.append(self.Hb)
                    self.Vplist.append(self.Vp)
            else :
                item = QTableWidgetItem('稠度系数')
                self.tableWidget.setItem(1, 0, QTableWidgetItem(item))
                for self.num7 in  range(1, int(self.num5)):                                         
                    item1 = QTableWidgetItem('%s'%self.num7)
                    self.tableWidget.setItem(0, self.num7,  QTableWidgetItem(item1))
                    item2 = QTableWidgetItem('%s'%self.num8[self.num7-1])
                    self.tableWidget.setItem(1, self.num7,  QTableWidgetItem(item2))
                    if self.tableWidget.item(1, self.num5) == '':
                        self.tableWidget.setItem(1, self.num5,  QTableWidgetItem(self.num2))
                    self.Vse2 = 3
                    self.Vc = self.Vt + self.Vse2
                    self.μav = self.num8[self.num7-1]*(math.pow(12*self.Va/(self.dh-self.dp), self.n-1))*(math.pow((2*self.n+1)/3*self.n, self.n))
                    print('1st,av:', self.μav)
                    for self.μav  in  self.iter(): pass
                    self.Hb = 0.01*self.dh*((3.221*0.001*math.pow(self.μav, 2)-0.442*(self.μav)+44)*(1+0.587*self.E)*(2.33-2.12*self.Va)-5.0)
                    item3 = QTableWidgetItem('%s'%self.Hb)
                    self.tableWidget.setItem(2, self.num7,  QTableWidgetItem(item3))
                    self.a = 2*math.sqrt((math.pow(self.rh, 2))-(math.pow((self.rh-self.Hb), 2)))
                    self.cos= (self.rh-self.Hb)/self.rh
                    self.Ae = math.pow(self.rh, 2)*(math.acos(self.cos)-(self.rh-self.Hb)*math.sqrt(self.a/2)/math.pow(self.rh, 2))
                    self.Vp = 0.001*(9.80665*0.001*self.Ae*self.C*9.80665*(math.cos(self.θ)-self.f*math.sin(self.θ))*(self.n*(self.dh-self.dp)))*(self.ρs-self.ρm)/(4*self.a*self.num8[self.num7-1]*(2*self.n+1))                  
                    item4 = QTableWidgetItem('%s'%self.Vp)
                    self.tableWidget.setItem(3, self.num7,  QTableWidgetItem(item4))
                    self.Hblist.append(self.Hb)
                    self.Vplist.append(self.Vp)
                
        elif  self.i2 < self.θ <= self.i3  :
            self.my_button=QMessageBox.information(self,'Warning','不进行计算！')
            
            
            
        else :
            my_button=QMessageBox.information(self,'Warning','θ值有问题！请仔细核对!')
        self.update_graph()  
     
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
            
    @pyqtSlot()
    def on_radioButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        self.update_graph()
    
    @pyqtSlot()
    def on_radioButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        self.update_graph()           


    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Form()
    ui.show()
    sys.exit(app.exec_())
