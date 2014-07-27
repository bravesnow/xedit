# -*- coding: utf-8 -*-
import sys 
from PyQt4 import QtCore,QtGui     
from elem import menu,tbar,window

def main():
    app=QtGui.QApplication(sys.argv)#应用程序实例化
    objwin = window.Window()#窗口实例化
    objmenu = menu.Menu(objwin)#菜单类实例化
    objtbar = tbar.Toolbar(objwin)#工具栏实例化
    #菜单信槽绑定
    QtCore.QObject.connect(objmenu.open,QtCore.SIGNAL('triggered()'),objwin.onopen)
    QtCore.QObject.connect(objmenu.save,QtCore.SIGNAL('triggered()'),objwin.onsave)
    QtCore.QObject.connect(objmenu.trans,QtCore.SIGNAL('triggered()'),objwin.ontrans)
    QtCore.QObject.connect(objmenu.close,QtCore.SIGNAL('triggered()'),objwin.onclose)
    #工具栏信槽绑定
    QtCore.QObject.connect(objtbar.openfileAction, QtCore.SIGNAL('triggered()'),objwin.onopen)
    QtCore.QObject.connect(objtbar.transAction, QtCore.SIGNAL('triggered()'),objwin.ontrans)
    QtCore.QObject.connect(objtbar.saveAction, QtCore.SIGNAL('triggered()'),objwin.onsave)    

    objwin.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
