from Ui_stackedWidget import Ui_MainWindow
import 影响规律
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
  # -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """

        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.influence_law = 影响规律.Form()
        self.tableWidget_4.verticalHeader().setVisible(True)


#        self.config = ConfigParser.ConfigParser()
#        self.config.read("default.cfg")
#        self.db = Database(self)
#        self.model = Model()
#        self.model = QStandardItemModel(self.tableView)
#        self.tableView = QtWidgets.QTableView(self.groupBox_33)
#        self.tableView.setGeometry(QtCore.QRect(10, 20, 271, 161))
#        self.tableView.setObjectName("tableView")
#        self.tableView.setModel(self.model)
#        if not self.radioButton_10.clicked:
#            self.model.setHorizontalHeaderItem(2, QStandardItem('备注'))
#        self.tableView_set()

#        self.tableView = QtWidgets.QTableView(self.groupBox_33)
#        self.tableView.setGeometry(QtCore.QRect(10, 20, 271, 161))
#        self.tableView.setObjectName("tableView")
#    def tableView_set(self):
#        self.model = QtGui.QStandardItemModel(self.tableView)
#
#        self.model=QStandardItemModel(3,3)
#        self.model.setHorizontalHeaderLabels(['计算指标', '临界值', '实际值'])
#        self.tableView.verticalHeader().setVisible(False)
#        self.model.setItem(0, 0, QStandardItem('环空返速(m/s)'))
#        self.model.setItem(1, 0, QStandardItem('钻井泵排量'))
#        self.model.setItem(2, 0, QStandardItem('止动环空返速'))
#        self.model.setItem(3, 0, QStandardItem('岩屑床厚度'))
#        self.model.setItem(4, 0, QStandardItem(''))
#        self.tableView_set=QTableView()
#        self.tableView.setModel(self.model)

    @pyqtSlot(int)
    def on_toolBox_currentChanged(self, index):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type int
        """

    @pyqtSlot(int)
    def on_stackedWidget_currentChanged(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type int
        """

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Sl1ot documentation goes here.
        """
#        connect(pushButton_6,  SIGNAL(clicked), StackedWidget,  SLOT(setCurrentIndex(int)))
#        QStackedWidget.setCurrentIndex(self, int)

    @pyqtSlot(int)
    def on_toolBox_3_currentChanged(self, index):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type int
        """

    @pyqtSlot()
    def on_pushButton_15_clicked(self):

        my_str = self.lineEdit_19.text()
        dh = self.lineEdit_20.text()
        dp = self.lineEdit_21.text()
        ρm = self.lineEdit_23.text()
        τ0 = self.lineEdit_24.text()
        μpv = self.lineEdit_25.text()
        ds = self.lineEdit_31.text()
        e = self.lineEdit_22.text()
        Ca = self.lineEdit_26.text()
        Vrop = self.lineEdit_27.text()  # 机械钻速，rop
        N = self.lineEdit_28.text()
        ρs = self.lineEdit_30.text()
        ds = self.lineEdit_31.text()
        C = self.lineEdit_32.text()
        Q = self.lineEdit_29.text()
        self.tableWidget_4.setItem(0, 1, QTableWidgetItem(my_str))
        self.tableWidget_4.setItem(2, 1, QTableWidgetItem(dh))
        self.tableWidget_4.setItem(3, 1, QTableWidgetItem(dp))
        self.tableWidget_4.setItem(4, 1, QTableWidgetItem(ρm))
        self.tableWidget_4.setItem(5, 1, QTableWidgetItem(τ0))
        self.tableWidget_4.setItem(6, 1, QTableWidgetItem(μpv))
        self.tableWidget_4.setItem(7, 1, QTableWidgetItem(ds))
        self.tableWidget_4.setItem(8, 1, QTableWidgetItem(e))
        self.tableWidget_4.setItem(9, 1, QTableWidgetItem(Ca))
        self.tableWidget_4.setItem(10, 1, QTableWidgetItem(Vrop))
        self.tableWidget_4.setItem(11, 1, QTableWidgetItem(N))
        self.tableWidget_4.setItem(12, 1, QTableWidgetItem(ρs))
        self.tableWidget_4.setItem(13, 1, QTableWidgetItem(ds))
        self.tableWidget_4.setItem(14, 1, QTableWidgetItem(C))

#        self.tableWidget_4.setItem(15, 1, QTableWidgetItem(Q))

    @pyqtSlot()
    def on_pushButton_16_clicked(self):
        """
        Slot documentation goes here.
        """
        global θ
        θ = self.lineEdit_18.text()
#        jiao=int(jiao)
#        global θ

        self.tableWidget_4.setItem(1, 1, QTableWidgetItem(θ))


# class Database:
#    def __int__(self,  parent = None):
#        print('connecting')
#        self.data = QtSql.QtSqlDatabase.addDatabase('QMYSQL')
#        self.data.setFirstName(parent.config.get('Database', ))

#    @pyqtSlot()
#    def on_radioButton_10_clicked(self):
#        """
#        Slot documentation goes here.
#        """
#        self.model.setItem(0, 2, QStandardItem('备注'))
#        self.
#    @pyqtSlot()
#    def TabView(self, tableView, Model):
#            self.tableView = QtWidgets.QTableView(self.groupBox_33)
#            self.tableView.setGeometry(QtCore.QRect(10, 20, 271, 161))
#            self.tableView.setObjectName("tableView")
#            self.HeaderList = ['计算指标', '临界值', '实际值']
#            self.DataModel = Model
#            self.DataModel.setHorizontalHeaderLabels(self.HeaderList)
#            self.DataModel.setItem(0, 0, QStandardItem('环空返速'))
#            self.DataModel.setItem(1, 0, QStandardItem('钻井泵排量'))
#            self.DataModel.setItem(2, 0, QStandardItem('止动环空返速'))
#            self.DataModel.setItem(3, 0, QStandardItem('岩屑床厚度'))
#            self.DataModel.setItem(4, 0, QStandardItem(''))
#            self.tableview = tableView
#            self.tableview.setModel(self.DataModel)


    @pyqtSlot()
    def on_radioButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tableWidget_5.setItem(0, 2,  QTableWidgetItem('实际值'))
        self.tableWidget_5.setItem(1, 0,  QTableWidgetItem('环空返速(m/s)'))
        self.tableWidget_5.setItem(2, 0,  QTableWidgetItem('钻井泵排量(L/min)'))
        self.tableWidget_5.setItem(3, 0,  QTableWidgetItem('止动环空返速(m/s)'))
        self.tableWidget_5.setItem(4, 0,  QTableWidgetItem('岩屑床厚度(mm)'))
        self.tableWidget_5.setItem(5, 0,  QTableWidgetItem(''))

    @pyqtSlot()
    def on_radioButton_10_clicked(self):
        """
        Slot documentation goes here.
        """
#        self.tableWidget_5.setHorizontalHeaderLabels([0, 1] , QTableWidgetItem('备注'))
        self.tableWidget_5.setItem(0, 2,  QTableWidgetItem('备注'))
        self.tableWidget_5.setItem(1, 0,  QTableWidgetItem('临界环空返速(m/s)'))
        self.tableWidget_5.setItem(2, 0,  QTableWidgetItem('临界排量'))
        self.tableWidget_5.setItem(3, 0,  QTableWidgetItem('止动环空返速(m/s)'))
        self.tableWidget_5.setItem(4, 0,  QTableWidgetItem('止动环空排量(L/min)'))
        self.tableWidget_5.setItem(5, 0,  QTableWidgetItem('临界岩屑床厚度(mm)'))

    @pyqtSlot()
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        global wow
        items = ['层流流态', '过渡流态', '紊流流态']
        wow, ok = QInputDialog.getItem(
            self, '请选择流态', '选择', items, 0, True)  # 0,1,2选择不同的Item
        if wow[0] == '层':
            print(wow)
        elif wow[0] == '过':
            print(wow)
        else:
            print(wow)
#        global wow

    @pyqtSlot()
    def on_pushButton_17_clicked(self):
        """
        Slot documentation goes here.
        """
        my_str = self.lineEdit_19.text()
        dh = self.lineEdit_20.text()
        dp = self.lineEdit_21.text()
        ρm = self.lineEdit_23.text()
        τ0 = self.lineEdit_24.text()
        μpv = self.lineEdit_25.text()
        ds = self.lineEdit_31.text()
        e = self.lineEdit_22.text()
        Ca = self.lineEdit_26.text()
        Vrop = self.lineEdit_27.text()
        N = self.lineEdit_28.text()
        ρs = self.lineEdit_30.text()
        ds = self.lineEdit_31.text()
        C = self.lineEdit_32.text()
        Q = self.lineEdit_29.text()

        Hb = 0.015*dh*(μav+6.15*μav**0.5)*(1+0.587*E)*(Vc-Va)
        if Hb <= 0:
            Hb = 0

        pbed = 0.37
        Pbed1 = self.lineEdit_33.text()
        if pbed1 != '':
            pbed = pbed1
        print(pbed)

        Cang = 0.0342*θ-0.000233*θ**2-0.213
        Cang30 = 0.0342*30-0.000233*900-0.213
        Csize = 1.286 - 0.0409448*ds
        Crpm = (600-N)/600
        if ρm <= 1.0425:
            Cdenf = 1
        else:
            Cdenf = 1-0.27799(ρm-1.0425)

        if wow[0] == '层' and self.radioButton_7.isChecked and 0 < int(θ) <= 10:
            μav1
            Vs = 0.32681*ds**2*(ρs-ρm)/(μav1)
            Vamin = (Vrop/Ca*(1-(dp/dh)**2))+1.25*Vs
            Qmin = Vamin*(dh**2-dp**2)/1273.2
            Rt = (Va-Vs)/Va
            if Rt > 0.5:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')

            print(Vs)
        elif wow[0] == '过' and self.radioButton_7.isChecked() and 0 < int(θ) <= 10:

            Vs = 0.07068*ds*(ρs-ρm)**0.6667/(ρm*μav1)**0.3333
            Vamin = (Vrop/Ca*(1-(dp/dh)**2))+1.25*Vs
            Qmin = Vamin*(dh**2-dp**2)/1273.2
            Rt = (Va-Vs)/Va
            if Rt > 0.5:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')

        elif wow[0] == '紊' and self.radioButton_7.isChecked() and 0 < int(θ) <= 10:
            μav1
            Vs = 0.0813*(ds*(ρs-ρm))**0.5/(ρm)**0.5
            Vamin = (Vrop/Ca*(1-(dp/dh)**2))+1.25*Vs
            Qmin = Vamin*(dh**2-dp**2)/1273.2
            Rt = (Va-Vs)/Va
            if Rt > 0.5:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')

        elif wow[0] == '层' and self.radioButton_8.isChecked() and 0 < int(θ) <= 10:
            #            k = 1
            #            n = 1
            μav2
            Vs = 0.32681*ds**2*(ρs-ρm)/(μav2)
            Vamin = (Vrop/Ca*(1-(dp/dh)**2))+1.25*Vs
            Qmin = Vamin*(dh**2-dp**2)/1273.2
            Rt = (Va-Vs)/Va
            if Rt > 0.5:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')

        elif wow[0] == '过' and self.radioButton_8.isChecked() and 0 < int(θ) <= 10:
            μav2
            Vs = 0.07068*ds*(ρs-ρm)**0.6667/(ρm*μav2)**0.3333
            Vamin = (Vrop/Ca*(1-(dp/dh)**2))+1.25*Vs
            Qmin = Vamin*(dh**2-dp**2)/1273.2
            Rt = (Va-Vs)/Va
            if Rt > 0.5:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')

        elif wow[0] == '紊' and self.radioButton_8.isChecked() and 0 < int(θ) <= 10:
            μav2
            Vs = 0.0813*(ds*(ρs-ρm))**0.5/(ρm)**0.5
            Vamin = (Vrop/Ca*(1-(dp/dh)**2))+1.25*Vs
            Qmin = Vamin*(dh**2-dp**2)/1273.2
            Rt = (Va-Vs)/Va
            if Rt > 0.5:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')
        elif wow[0] == '层' and self.radioButton_7.isChecked() and 10 < int(θ) <= 30:
            Vs = 0.32681*ds**2*(ρs-ρm)/(μav1)

            if μav1 <= 53:
                Vse = 0.00516*μav1+0.916
            else:
                Vse = 0.02554*(μav1-53)+0.9997
            Vsc30 = Vse*Cang30*Csize*Cdenf*Crpm
#            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vsc = Vs + θ*(Vsc30-Vs)/30
            Vc = Vt + Vsc
            Qc = Vc*(dh**2-dp**2)/1273.2
            Ca = (1-Q/Qc)*(1-pbed)*(0.97-0.00231*μav1)
            if Ca <= 5 and Va > Vc:
                self.textEdit.setText('安全')

        elif wow[0] == '过' and self.radioButton_7.isChecked() and 10 < int(θ) <= 30:
            Vs = 0.07068*ds*(ρs-ρm)**0.6667/(ρm*μav)**0.3333

            if μav1 <= 53:
                Vse = 0.00516*μav1+0.916
            else:
                Vse = 0.02554*(μav1-53)+0.9997
            Vsc30 = Vse*Cang30*Csize*Cdenf*Crpm
#            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vsc = Vs + θ*(Vsc30-Vs)/30
            Vc = Vt + Vsc
            Qc = Vc*(dh**2-dp**2)/1273.2
            Ca = (1-Q/Qc)*(1-pbed)*(0.97-0.00231*μav1)
            if Ca <= 5 and Va > Vc:
                self.textEdit.setText('安全')

        elif wow[0] == '紊' and self.radioButton_7.isChecked() and 10 < int(θ) <= 30:
            Vs = 0.0813*(ds*(ρs-ρm))**0.5/(ρm)**0.5

            if μav1 <= 53:
                Vse = 0.00516*μav1+0.916
            else:
                Vse = 0.02554*(μav1-53)+0.9997
            Vsc30 = Vse*Cang30*Csize*Cdenf*Crpm
#            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vsc = Vs + θ*(Vsc30-Vs)/30
            Vc = Vt + Vsc
            Qc = Vc*(dh**2-dp**2)/1273.2
            Ca = (1-Q/Qc)*(1-pbed)*(0.97-0.00231*μav1)
            if Ca <= 5 and Va > Vc:
                self.textEdit.setText('安全')

        elif wow[0] == '层' and self.radioButton_8.isChecked() and 10 < int(θ) <= 30:
            μav2
            Vs = 0.32681*ds**2*(ρs-ρm)/(μav2)

            if μav2 <= 53:
                Vse = 0.00516*μav2+0.916
            else:
                Vse = 0.02554*(μav2-53)+0.9997
            Vsc30 = Vse*Cang30*Csize*Cdenf*Crpm
#            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vsc = Vs + θ*(Vsc30-Vs)/30
            Vc = Vt + Vsc
            Qc = Vc*(dh**2-dp**2)/1273.2
            Ca = (1-Q/Qc)*(1-pbed)*(0.97-0.00231*μav2)
            if Ca <= 5 and Va > Vc:
                self.textEdit.setText('安全')

        elif wow[0] == '层' and self.radioButton_8.isChecked() and 10 < int(θ) <= 30:
            μav2
            Vs = 0.07068*ds*(ρs-ρm)**0.6667/(ρm*μav2)**0.3333

            if μav2 <= 53:
                Vse = 0.00516*μav2+0.916
            else:
                Vse = 0.02554*(μav2-53)+0.9997
            Vsc30 = Vse*Cang30*Csize*Cdenf*Crpm
#            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vsc = Vs + θ*(Vsc30-Vs)/30
            Vc = Vt + Vsc
            Qc = Vc*(dh**2-dp**2)/1273.2
            Ca = (1-Q/Qc)*(1-pbed)*(0.97-0.00231*μav2)
            if Ca <= 5 and Va > Vc:
                self.textEdit.setText('安全')

        elif wow[0] == '层' and self.radioButton_8.isChecked() and 10 < int(θ) <= 30:
            μav2
            Vs = 0.0813*(ds*(ρs-ρm))**0.5/(ρm)**0.5

            if μav2 <= 53:
                Vse = 0.00516*μav2+0.916
            else:
                Vse = 0.02554*(μav2-53)+0.9997
            Vsc30 = Vse*Cang30*Csize*Cdenf*Crpm
#            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vsc = Vs + θ*(Vsc30-Vs)/30
            Vc = Vt + Vsc
            Qc = Vc*(dh**2-dp**2)/1273.2
            Ca = (1-Q/Qc)*(1-Pbed)*(0.97-0.00231*μav2)
            if Ca <= 5 and Va > Vc:
                self.textEdit.setText('安全')


#
#        elif wow[0]=='层' and self.radioButton_7.isChecked() and 30 < int(θ) <=65 :


#        elif wow[0]=='紊' and self.radioButton_7.isChecked() and 30 < int(θ) <=65 :
#
#            μav1
#
#        elif wow[0]=='层' and self.radioButton_7.isChecked() and 30 < int(θ) <=65 :
#            μav1
#
#
#        elif wow[0]=='层' and self.radioButton_8.isChecked() and 30 < int(θ) <=65 :
#            μav2
#
#        elif wow[0]=='层' and self.radioButton_8.isChecked() and 30 < int(θ) <=65 :
#            μav2
#        elif wow[0]=='层' and self.radioButton_8.isChecked() and 30 < int(θ) <=65 :
#            μav2

        elif wow[0] == '层' and self.radioButton_7.isChecked() and int(θ) > 65:
            # +0.55*sin(2*θ))/(ρm*μav2)**0.333]
            Vc1 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ)]
            if μav1 <= 53:
                Vse = 0.00516*μav1+0.916
            else:
                Vse = 0.02554*(μav1-53)+0.9997
            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vc = Vt + Vsc

            if Hb/dh < 10 and Va > Vc:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')

        elif wow[0] == '过' and self.radioButton_7.isChecked() and int(θ) > 65:
            # +0.55*sin(2*θ))/(ρm*μav2)**0.333]
            Vc1 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ)]
            if μav1 <= 53:
                Vse = 0.00516*μav1+0.916
            else:
                Vse = 0.02554*(μav1-53)+0.9997
            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vc = Vt + Vsc

            if Hb/dh < 10 and Va > Vc:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')
        elif wow[0] == '层' and self.radioButton_7.isChecked() and int(θ) > 65:
            # +0.55*sin(2*θ))/(ρm*μav2)**0.333]
            Vc1 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ)]
            if μav1 <= 53:
                Vse = 0.00516*μav1+0.916
            else:
                Vse = 0.02554*(μav1-53)+0.9997
            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vc = Vt + Vsc

            if Hb/dh < 10 and Va > Vc:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')

        elif wow[0] == '层' and self.radioButton_8.isChecked() and int(θ) > 65:
            # +0.55*sin(2*θ))/(ρm*μav2)**0.333]
            Vc2 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ)]
            if μav2 <= 53:
                Vse = 0.00516*μav2+0.916
            else:
                Vse = 0.02554*(μav2-53)+0.9997
            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vc = Vt + Vsc

            if Hb/dh < 10 and Va > Vc:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')
        elif wow[0] == '层' and self.radioButton_8.isChecked() and int(θ) > 65:
            # *sin(2*θ))/(ρm*μav2)**0.333]
            Vc2 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ+0.55)]
            if μav2 <= 53:
                Vse = 0.00516*μav2+0.916
            else:
                Vse = 0.02554*(μav2-53)+0.9997
            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vc = Vt + Vsc

            if Hb/dh < 10 and Va > Vc:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')
        elif wow[0] == '层' and self.radioButton_8.isChecked() and int(θ) > 65:
            # *sin(2*θ))/(ρm*μav2)**0.333]
            Vc2 = 0.4*[(ρs-ρm)/ρm]**0.667*[(1+0.71*θ+0.55)]
            if μav2 <= 53:
                Vse = 0.00516*μav2+0.916
            else:
                Vse = 0.02554*(μav2-53)+0.9997
            Vsc = Vse*Cang*Csize*Cdenf*Crpm
            Vc = Vt + Vsc

            if Hb/dh < 10 and Va > Vc:
                self.textEdit.setText('安全')
            else:
                self.textEdit.setText('不安全')
#            Qs = Va*(dh**2-dp**2)/1273.2# Qs安全钻进时的环空排量

    @pyqtSlot()
    def on_pushButton_18_clicked(self):
        """
        Slot documentation goes here.
        """
        self.influence_law.show()

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        self.influence_law.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
#    ui.toolBox_2.currentChanged.connect(uo.show)
#    ui.toolBox_2.currentChanged.connect(ui.stackedWidget.setCurrentIndex)
#    uo.close.connect(ui.show)
#    ui.stackedWidget.currentChanged['int'].connect(uo.close)
#    uo.close.connect(ui.stackedWidget.setCurrentIndex)
    ui.show()
    sys.exit(app.exec_())

#    @pyqtSlot()
#    def on_pushButton_2_clicked(self):
#        """
#        Slot documentation goes here.
#        """
#
