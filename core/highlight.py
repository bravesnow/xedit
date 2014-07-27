# -*- coding: cp936 -*-
import sys
from PyQt4 import QtCore,QtGui
#�ؼ���
kw = ["auto","break","case","char","const","continue","default",
      "do","double","else","enum","extern","float","for","goto",
      "if","int","long","register","return","short","signed","sizeof",
      "static","struct","switch","typedef","union","unsigned","void",
      "volatile","while","inline","restrict"]
#������
rc = ["include","define","printf","scanf"]
class MyHighlighter( QtGui.QSyntaxHighlighter ):
    def __init__( self, parent, theme ):
        QtGui.QSyntaxHighlighter.__init__( self, parent )
        self.parent = parent
        #�ؼ���keyword��ɫ
        keyword = QtGui.QTextCharFormat()
        kwcolor = QtCore.Qt.blue
        #������reservedClasses����
        reservedClasses = QtGui.QTextCharFormat()
        rccolor = QtCore.Qt.darkMagenta
        #��ֵassignmentOperator���綨��delimiter��ɫ
        assignmentOperator = QtGui.QTextCharFormat()
        delimiter = QtGui.QTextCharFormat()
        orcolor = QtCore.Qt.black
        #���������ⳣ�����������������֣�����
        specialConstant = QtGui.QTextCharFormat()
        boolean = QtGui.QTextCharFormat()
        number = QtGui.QTextCharFormat()
        cstcolor = QtCore.Qt.darkCyan
        #ע��comment��ɫ
        comment = QtGui.QTextCharFormat()
        ctcolor = QtCore.Qt.red
        #�ַ���string����ɫ
        string = QtGui.QTextCharFormat()
        singleQuotedString = QtGui.QTextCharFormat()
        strcolor = QtCore.Qt.darkGreen
        #������������
        follow = QtGui.QTextCharFormat()
        fwcolor = QtCore.Qt.darkYellow
        #�����б�
        self.highlightingRules = []
        #===========================================
        #�ؼ���keyword
        brush = QtGui.QBrush( kwcolor, QtCore.Qt.SolidPattern )
        keyword.setForeground( brush )
        #keyword.setFontWeight( QtGui.QFont.Bold )
        keywords = QtCore.QStringList(kw) #keywords
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, keyword )
            self.highlightingRules.append( rule )
        #===============================================
        #������reservedClasses
        brush = QtGui.QBrush( rccolor, QtCore.Qt.SolidPattern )
        reservedClasses.setForeground( brush )
        reservedClasses.setFontWeight( QtGui.QFont.Bold )
        keywords = QtCore.QStringList(rc)      
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, reservedClasses )
            self.highlightingRules.append( rule )
        #=====================================
        #��ֵ������assignmentOperator
        brush = QtGui.QBrush(orcolor, QtCore.Qt.SolidPattern )
        pattern = QtCore.QRegExp( "(<){1,2}-" )
        assignmentOperator.setForeground( brush )
        assignmentOperator.setFontWeight( QtGui.QFont.Bold )
        rule = HighlightingRule( pattern, assignmentOperator )
        self.highlightingRules.append( rule )
        #�����delimiter
        pattern = QtCore.QRegExp( "[\)\(]+|[\{\}]+|[][]+" )
        delimiter.setForeground( brush )
        delimiter.setFontWeight( QtGui.QFont.Bold )
        rule = HighlightingRule( pattern, delimiter )
        self.highlightingRules.append( rule )
        #=====================================
        #���ⳣ��specialConstant
        brush = QtGui.QBrush(cstcolor, QtCore.Qt.SolidPattern )
        specialConstant.setForeground( brush )
        keywords = QtCore.QStringList( [ "None" ] )
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, specialConstant )
            self.highlightingRules.append( rule )
        #��������boolean
        boolean.setForeground( brush )
        keywords = QtCore.QStringList( [ "True", "False" ] )
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, boolean )
            self.highlightingRules.append( rule )
        #����number
        pattern = QtCore.QRegExp( "[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?" )
        pattern.setMinimal( True )
        number.setForeground( brush )
        rule = HighlightingRule( pattern, number )
        self.highlightingRules.append( rule )
        #=====================================
        #ע��comment
        brush = QtGui.QBrush( ctcolor, QtCore.Qt.SolidPattern )
        pattern = QtCore.QRegExp( "//[^\n]*" )
        comment.setForeground( brush )
        rule = HighlightingRule( pattern, comment )
        self.highlightingRules.append( rule )
        #=====================================
        #�ַ���string
        brush =QtGui.QBrush( strcolor, QtCore.Qt.SolidPattern )
        pattern = QtCore.QRegExp( "\".*\"" )
        pattern.setMinimal( True )
        string.setForeground( brush )
        rule = HighlightingRule( pattern, string )
        self.highlightingRules.append( rule )
        #�������ַ���singleQuotedString
        pattern = QtCore.QRegExp( "\'.*\'" )
        pattern.setMinimal( True )
        singleQuotedString.setForeground( brush )
        rule = HighlightingRule( pattern, singleQuotedString )
        self.highlightingRules.append( rule )
        
    def highlightBlock( self, text ):
        for rule in self.highlightingRules:
            expression = QtCore.QRegExp( rule.pattern )
            index = expression.indexIn( text )
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat( index, length, rule.format )
                index = text.indexOf( expression, index + length )
        self.setCurrentBlockState( 0 )

class HighlightingRule():
    def __init__( self, pattern, format ):
        self.pattern = pattern
        self.format = format
