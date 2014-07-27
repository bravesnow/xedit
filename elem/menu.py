# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui
class Menu(QtGui.QMenuBar):
    def __init__(self,parent):
        #parent是QMainWindow类，其方法产生菜单栏
        menubar=parent.menuBar()
        #==============================
        #菜单File及项
        file=menubar.addMenu('File')
        self.open=file.addAction('Open')
        self.save=file.addAction('Save')
        self.close=file.addAction('Close')
        #file.addSeparator()#分隔线
        #==============================
        #菜单Edit及项
        edit=menubar.addMenu('Edit')
        self.trans=edit.addAction('Trans')
        self.untrans=edit.addAction('Untrans')
        edit.addAction('Copy')

if __name__ == '__main__':
    pass
