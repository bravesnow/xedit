# -*- coding: utf-8 -*-
import os,sys,subprocess
from PyQt4 import QtCore,QtGui
sys.path.append("..")
from core import highlight
class Edit(QtGui.QTextEdit):
    def __init__(self,parent):
        QtGui.QTextEdit.__init__(self,parent)
        self.setFont(self.editfont())#设置字体
        highlight.MyHighlighter(self,"Classic")#设置文本框语法高亮     
    def editfont(self):
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily( "Courier" )
        font.setFixedPitch( True )
        font.setPointSize(10)
        return font
    
class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)#父类初始化
        self.setWindowTitle('xedit')#主窗口标题
        self.resize(800,600)#窗口初始大小
        #==================================================
        #分割窗口及其中的文本框
        mainSplitter=QtGui.QSplitter(QtCore.Qt.Horizontal,self)#主窗口        
        self.textedit=Edit(mainSplitter)#主窗口绑定Markdown源框
        rightSplitter=QtGui.QSplitter(QtCore.Qt.Vertical,mainSplitter)#次窗口附着于主窗口
        self.dis_textedit=Edit(rightSplitter)#次窗口绑定HTML显示框
        self.setCentralWidget(mainSplitter)#添加主窗口到窗体
        #=============================
        #默认的文件
        self.filename ="tmp/tmp.c"
                        
    def onopen(self):
        self.filename=QtGui.QFileDialog.getOpenFileName(self,'open')
        if not self.filename.isEmpty():
            file=open(self.filename,'r')
            self.textedit.setText(file.read().decode('utf8'))
            file.close()
    def ontrans(self):
        objfile = str(self.filename)
        noextension = objfile.split('.')[0]#(objfile.split("/")[-1]).split('.')[0]
        cmd = 'gcc -o ' + noextension + ' ' + objfile
        p=subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)        
        retstr = p.stdout.read().decode('cp936')#编码注意
        if len(retstr):
            self.dis_textedit.setText(retstr)
        else:
            cmd = noextension + '.exe'
            ep=subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            
            self.dis_textedit.setText(ep.stdout.read().decode('cp936'))
        
    def onsave(self):
        f=open(self.filename,'w')
        strstr = unicode(self.textedit.toPlainText())
        f.write(strstr.encode('utf8'))
        f.close()
    def onclose(self):
        self.close()
