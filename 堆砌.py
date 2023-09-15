import sys
from PyQt5 import QtWidgets, QtCore


class MyWidget(QtWidgets.QWidget):
    def __init__(self, i=0):
        super().__init__()
        self.setWindowTitle('窗口')
        label = QtWidgets.QLabel('标签' + str(i))
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(label)
        

class TestWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QtWidgets.QHBoxLayout(self)
        
        #stack  = QtWidgets.QStackedWidget() # ① Widget
        stack  = QtWidgets.QStackedLayout() # ② Layout

        list   = QtWidgets.QListWidget(self)
        list.setDragEnabled(True)
        list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

        layout.addWidget(list)
        #layout.addWidget(stack) # ① 对应 addWidget
        layout.addLayout(stack) # ② 对应 addLayout

        for i in range(10):
            stack.addWidget(MyWidget(i))
            list.addItem("窗口   %04i" % i)

        list.currentRowChanged.connect(stack.setCurrentIndex)


if __name__ == "__main__":
    app    = QtWidgets.QApplication(sys.argv)
    widget = TestWidget()
    #widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
