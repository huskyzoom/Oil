# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Ui_tttttt import Ui_MainWindow1
import sys


class MainWindow1(QMainWindow, Ui_MainWindow1):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow1, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_radioButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.radioButton.setChecked(True)

    
    
        
        

    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        
        
        
        
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()
        self.MainWindow2.show()
        

    
    @pyqtSlot(QModelIndex)
    def on_tableWidget_activated(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        self.table.verticalHeader().setVisible(False)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    A = MainWindow1()
    A.show()
    sys.exit(app.exec_())    


class MainWindow2(QMainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow2, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_action_triggered(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_action111_2_triggered(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_action111_triggered(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_action11_triggered(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_action111_3_triggered(self):
        """
        Slot documentation goes here.
        """
        
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        dirName = QFileDialog.getExistingDirectory(
            self,
            self.tr("选择文件夹"),
            "",
            QFileDialog.Options(QFileDialog.ShowDirsOnly))
        print(dirName)
        
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        

