# -*- coding: cp936 -*-
import sys
from PyQt4 import QtCore,QtGui
#关键字
kw = ["auto","break","case","char","const","continue","default",
      "do","double","else","enum","extern","float","for","goto",
      "if","int","long","register","return","short","signed","sizeof",
      "static","struct","switch","typedef","union","unsigned","void",
      "volatile","while","inline","restrict"]
#保留类
rc = ["include","define","printf","scanf"]
class MyHighlighter( QtGui.QSyntaxHighlighter ):
    def __init__( self, parent, theme ):
        QtGui.QSyntaxHighlighter.__init__( self, parent )
        self.parent = parent
        #关键字keyword蓝色
        keyword = QtGui.QTextCharFormat()
        kwcolor = QtCore.Qt.blue
        #保留类reservedClasses深紫
        reservedClasses = QtGui.QTextCharFormat()
        rccolor = QtCore.Qt.darkMagenta
        #赋值assignmentOperator、界定符delimiter黑色
        assignmentOperator = QtGui.QTextCharFormat()
        delimiter = QtGui.QTextCharFormat()
        orcolor = QtCore.Qt.black
        #常量（特殊常数，布尔常数，数字）深青
        specialConstant = QtGui.QTextCharFormat()
        boolean = QtGui.QTextCharFormat()
        number = QtGui.QTextCharFormat()
        cstcolor = QtCore.Qt.darkCyan
        #注释comment红色
        comment = QtGui.QTextCharFormat()
        ctcolor = QtCore.Qt.red
        #字符串string深绿色
        string = QtGui.QTextCharFormat()
        singleQuotedString = QtGui.QTextCharFormat()
        strcolor = QtCore.Qt.darkGreen
        #类名、函数名
        follow = QtGui.QTextCharFormat()
        fwcolor = QtCore.Qt.darkYellow
        #规则列表
        self.highlightingRules = []
        #===========================================
        #关键字keyword
        brush = QtGui.QBrush( kwcolor, QtCore.Qt.SolidPattern )
        keyword.setForeground( brush )
        #keyword.setFontWeight( QtGui.QFont.Bold )
        keywords = QtCore.QStringList(kw) #keywords
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, keyword )
            self.highlightingRules.append( rule )
        #===============================================
        #保留类reservedClasses
        brush = QtGui.QBrush( rccolor, QtCore.Qt.SolidPattern )
        reservedClasses.setForeground( brush )
        reservedClasses.setFontWeight( QtGui.QFont.Bold )
        keywords = QtCore.QStringList(rc)      
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, reservedClasses )
            self.highlightingRules.append( rule )
        #=====================================
        #赋值操作符assignmentOperator
        brush = QtGui.QBrush(orcolor, QtCore.Qt.SolidPattern )
        pattern = QtCore.QRegExp( "(<){1,2}-" )
        assignmentOperator.setForeground( brush )
        assignmentOperator.setFontWeight( QtGui.QFont.Bold )
        rule = HighlightingRule( pattern, assignmentOperator )
        self.highlightingRules.append( rule )
        #定界符delimiter
        pattern = QtCore.QRegExp( "[\)\(]+|[\{\}]+|[][]+" )
        delimiter.setForeground( brush )
        delimiter.setFontWeight( QtGui.QFont.Bold )
        rule = HighlightingRule( pattern, delimiter )
        self.highlightingRules.append( rule )
        #=====================================
        #特殊常量specialConstant
        brush = QtGui.QBrush(cstcolor, QtCore.Qt.SolidPattern )
        specialConstant.setForeground( brush )
        keywords = QtCore.QStringList( [ "None" ] )
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, specialConstant )
            self.highlightingRules.append( rule )
        #布尔常量boolean
        boolean.setForeground( brush )
        keywords = QtCore.QStringList( [ "True", "False" ] )
        for word in keywords:
            pattern = QtCore.QRegExp("\\b" + word + "\\b")
            rule = HighlightingRule( pattern, boolean )
            self.highlightingRules.append( rule )
        #数字number
        pattern = QtCore.QRegExp( "[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?" )
        pattern.setMinimal( True )
        number.setForeground( brush )
        rule = HighlightingRule( pattern, number )
        self.highlightingRules.append( rule )
        #=====================================
        #注释comment
        brush = QtGui.QBrush( ctcolor, QtCore.Qt.SolidPattern )
        pattern = QtCore.QRegExp( "//[^\n]*" )
        comment.setForeground( brush )
        rule = HighlightingRule( pattern, comment )
        self.highlightingRules.append( rule )
        #=====================================
        #字符串string
        brush =QtGui.QBrush( strcolor, QtCore.Qt.SolidPattern )
        pattern = QtCore.QRegExp( "\".*\"" )
        pattern.setMinimal( True )
        string.setForeground( brush )
        rule = HighlightingRule( pattern, string )
        self.highlightingRules.append( rule )
        #单引号字符串singleQuotedString
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
