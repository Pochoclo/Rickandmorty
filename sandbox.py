__author__ = 'NicoS'


from PyQt4 import QtCore, QtGui
import os


class Midget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 600)
        self.l1 = QtGui.QLabel(self)
        self.l1.setGeometry(10, 0, 50, 50)
        pixmap = QtGui.QPixmap(os.getcwd() + '/assets/aqua_boss.png')
        self.l1.setPixmap(pixmap)
        self.l1.show()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    w = Midget()
    w.show()
    app.exec_()

    a = 0
    b = property(fget=None, fset=None, fdel=None, doc='jeje soy una property')