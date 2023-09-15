# -*- coding: utf-8 -*-

"""
Module implementing Form.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_我的影响规律 import Ui_Form


class Form(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Form, self).__init__(parent)
        self.setupUi(self)
        my_str = self.lineEdit_5.text()
        dh = self.lineEdit_6.text()
        dp = self.lineEdit_7.text()
        e= self.lineEdit_8.text()
        Vrop = self.lineEdit_9.text()
        N = self.lineEdit_10.text()
#        Q = self.lineEdit_11.text()
        μpv = self.lineEdit_12.text()
        ρm = self.lineEdit_13.text()
        Ca = self.lineEdit_14.text()
        ρs = self.lineEdit_15.text()
        ds = self.lineEdit_16.text()
        C = self.lineEdit_17.text()
        kongxidu = self.lineEdit_18.text()
        f = self.lineEdit_19.text()
        n = 0.1
        k = 0.2
        #床与井壁间摩擦系数
#        Q = int(Q)
#        ρm = int(ρm)
#        τ0 = int(τ0)
#        μpv = int(μpv)
#        ds = int(ds)
#        dh = int(dh)
#        dp = int(dp)
#        e = int(e)
#        Ca = int(Ca)
#        Vrop = int(Vrop)
#        N = int(N)
#        ρs = int(ρs)
#        C = int(C)
#        μav2 = 0.084*(1195.3)**n*k*(Va/dh-dp)**(n-1)*((2*n+1)/3*n)**n
#        μav1 = μpv+0.112*(τ0*(dh-dp)/Va)
#        Va = 1273.2*Q/(dh**2-dp**2)
#        Vt = (Vrop*dh**2)/(dh**2-dp**2)*Ca
#        E = e/(dh-dp)
#        Qs = Va*(dh**2-dp**2)/1273.2
#        self.tableWidget.horizontalHeader().setVisible(False)
#        self.tableWidget.verticalHeader().setVisible(False)
##        Q = int(Q)
##        self.Va = 1273.2*self.Q/(dh**2-dp**2)
#        self.μav1 = μpv +( τ0*(dh-dp))/(0.112*Va)
#        self.μav2 = 0.084*(1195.3)**n*k*(Va/dh-dp)**(n-1)*((2*n+1)/3*n)**n
#        self.E = e/(dh-dp)
    
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
        self.label_11.setText('塑性粘度(mPa.s)')

    
    @pyqtSlot()
    def on_radioButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        self.radioButton_5.setText('稠度系数与岩屑床厚度之间关系曲线')
        self.radioButton_6.setText('稠度系数与止动环空返速之间关系曲线')
        self.groupBox_3.setTitle('稠度系数(mPa*s^n)分析范围')
        self.label_11.setText('稠度系数(mPa*s^n)')

    
    @pyqtSlot()
    def on_radioButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_radioButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        

    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        
        
 
        

    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        num1 = self.lineEdit.text()#lineEdit.toPlainText()
        num1 = float(num1)
        num2 = self.lineEdit_2.text()
        num2 = float(num2)
        num3 = self.lineEdit_3.text()
        num3 = float(num3)
        num4 = (num2) - (num1) + num3
        #好RANGE，比终止值多了一个，所以能刚好range到
        print(num4)
        num5 = ((num4*100)/(num3*100)) + 1
        print(num5)
        self.tableWidget.setColumnCount(num5)
#        for column in range(num5):
#            for row in range(5):
#                for num in range(num1, num2, num3):
        num8 = [num8/100.0 for num8 in range(int(num1*100.0), int(num2*100.0), int(num3*100.0))]   
                
#            num8 = num8/100.0         
#      item = QStandardItem("row %s, column %s"%(row, column))
        for num7 in  range(1, int(num5)):
            print(num8)
            item1 = QTableWidgetItem('%s'%int(num7))
            self.tableWidget.setItem(0, num7,  QTableWidgetItem(item1))
            i = len(num8) - 1
            for w in repr(num8[i]):
                print(i)
                print(w)
#                item2 = QTableWidgetItem('%s'%((i)))
#                print(item2)
#                self.tableWidget.setItem(1,num7, QTableWidgetItem(item2))
            
        if self.radioButton_2.isChecked() and  30 < θ <= 65 :
            print('uuu')
#            global Ae
#            Hb = 0.01*dh*(3221*μav1**2-442*μav+44)*(1+0.587*E)*(2.33-2.12*Va)-5.0
#            rh = dh/2
#            Ae = rh*(arccos((rh-Hb)/rh)-((rh-Hb)*(2*rh*Hb-Hb**2)**0.5)/rh**2
#            = 9.80665*Ae*C*g*(cos(θ)-f*sin(θ))*0.5*(rh**2-(rh-Hb)**2)**(-1)
#            Vp =  (1.5)*τ0*(dh-dp)*1/(12*μpv)
            
        if  self.radioButton.isChecked() and  θ > 65  :
            Vc1 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ)+0.55*sin(2*θ)/(ρm*μav1)**0.333]
            Hb = 0.015*dh*(μav1+6.15*μav1**0.5)*(1+0.587*E)*(Vc-Va)
#            Vp = 
             
        if self.radioButton_2.isChecked() and  30 < θ <= 65  :  
            Hb = 0.01*dh*(3221*μav1**2-442*μav1+44)*(1+0.587*E)*(2.33-2.12*Va)-5.0
            
            
           
        if self.radioButton_2.isChecked() and  θ > 65  :
            Hb = 0.015*dh*(μav1+6.15*μav1**0.5)*(1+0.587*E)*(Vc-Va)
            Vc1 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ)+0.55*sin(2*θ)/(ρm*μav1)**0.333]
            
        if  self.radioButton_3.isChecked() and  30 < θ <= 65  :
            Hb = 0.01*dh*(3221*μav1**2-442*μav1+44)*(1+0.587*E)*(2.33-2.12*Va)-5.0
            
        if  self.radioButton_3.isChecked() and  θ > 65  :
            Hb = 0.015*dh*(μav1+6.15*μav1**0.5)*(1+0.587*E)*(Vc-Va)
            
            
            
        if  self.radioButton_4.isChecked() and  30 < θ <= 65  :
            Hb = 0.01*dh*(3221*μav1**2-442*μav1+44)*(1+0.587*E)*(2.33-2.12*Va)-5.0
            
            
        if  self.radioButton_4.isChecked() and  θ > 65  :
            Hb = 0.015*dh*(μav1+6.15*μav1**0.5)*(1+0.587*E)*(Vc-Va)
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
