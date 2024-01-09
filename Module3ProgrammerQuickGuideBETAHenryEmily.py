#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#/Users/emily/Desktop/CS 4910 - Senior Project/Module3_ProgrammerQuickGuideAlpha_Henry,Emily.py
"""
Emily Henry
CS 4910 Senior Project - Alpha Version Programmer's QuickGuide
September 16,2022
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QCompleter,QLineEdit,QToolButton,QMainWindow,QWidget,QLabel,QApplication,QPushButton,QGridLayout,QComboBox,QVBoxLayout,QHBoxLayout
from typing import List
HomeIconPath = '/Users/emily/Desktop/CS 4910 - Senior Project/home.jpeg'

            
            
class Language():
    CurrentLanguage = " "
    KeywordBank = []
    LanguageBank=[]
    KeywordData =[]
    
    TopicBank =[]
    
    def Language(self):
        
        self.KeywordBank = list()
        self.LanguageBank= list()
        self.KeywordData = list()
        self.TopicBank = list()
        
    def checkBankSize(language):
        if len(language.KeywordBank) == 0:
            return True
        elif len(language.KeywordBank) >=1000:
            print("Keyword Bank is Full")
            return False
        else:
            return True
        
    # add a new word to the keywordbank    
    def addKeyword(Keyword,language):
            if language.checkBankSize() == True:
                
                language.KeywordBank.append(Keyword)
                language.KeywordBank.sort()
    # put language in the bank
    def addLanguage(self,language):
        self.LanguageBank.append(language)
        
    # return language    
    def getLanguage():
        return Language
    
    # return the whole bank
    def getLanguageBank(self):
        return Language.LanguageBank
    
    def getKeywordBank(language):
        return language.KeywordBank
    
    def getTopicBank(Language):
        return Language.TopicBank
    
    def getTopic(Language,txt):
        for Topic in Language.TopicBank:
            if txt == Language.toString():
                return Topic
            else:
                break   
            
    def addTopic(topic):
        Language.TopicBank.append(topic)
    
class Topic():
    TopicInformation =" "

    def setInformation(self,s):
        self.TopicInformation = s   
class Keyword():
    word =" " 
    Description =" "
    Examples = " "
    KeyLanguage=" "
    
    def setKeywordData(Keyword,description,examples,language):
        if isinstance(Keyword,str):
            word = Keyword
        else:
            Keyword.word = Keyword.toString()
            
        Description = description
        Examples = examples
        KeyLanguage = language
        
    def getKeyword(keyword):
        i = -1
        for k in KeywordBank:
            i = i + 1
            if k == keyword:
                return KeywordBank[i]
            else:
                continue
            
            
    def getDescription(Keyword):
       return Keyword.Description
   
    def getExamples(Keyword):
        return Keyword.Examples
    
    def getKeywordData(Keyword):
        
        i = KeywordData.index(Keyword)
        KData = {KeywordData[i],KeywordData[i+1],KeywordData[i+2]}
        return KData
    
    def setKeywordData():
        Language.KeywordData.extend([Keyword.word,Keyword.getDescription(Keyword),Keyword.getExamples(Keyword)])
        
        
        
    
class GUI(Language):
    
    HomeWindow = QMainWindow()
    KeyWordWindow =QMainWindow()
    TopicWindow = QMainWindow()
    HomeIcon = QIcon(HomeIconPath)
    HomeButton = QPushButton(HomeWindow)
    LoginWindow =QMainWindow()
    SearchBar = QLineEdit(parent=HomeWindow)
    
    TopicCombo = QComboBox(parent = HomeWindow)
    LanguageCombo = QComboBox(parent = HomeWindow)
    KeywordCombo = QComboBox(parent = HomeWindow)
    
    KTopicCombo = QComboBox(parent= KeyWordWindow)
    KLanguageCombo = QComboBox(parent=KeyWordWindow)
    KKeywordCombo = QComboBox( parent=KeyWordWindow)
    
    TTopicCombo = QComboBox(parent= TopicWindow)
    TLanguageCombo = QComboBox(parent=TopicWindow)
    TKeywordCombo = QComboBox( parent=TopicWindow)
    
    def initGUI(self):
        G = GUI()
        G.createHomeWindow().show()
        
        self.KTopicCombo.currentTextChanged[str].connect(lambda:self.getTopicWindow())
        self.KLanguageCombo.currentIndexChanged[str].connect(lambda:self.getHomeWindow())
        self.TTopicCombo.currentIndexChanged[str].connect(lambda:self.getTopicWindow())
        self.TopicCombo.currentIndexChanged[str].connect(lambda:self.getTopicWindow())
        self.LanguageCombo.currentIndexChanged[str].connect(lambda:self.getHomeWindow())
        self.KeywordCombo.currentIndexChanged[str].connect(lambda:self.getKeyWindow())
        self.TLanguageCombo.currentIndexChanged[str].connect(lambda:self.getHomeWindow())
        self.TKeywordCombo.currentIndexChanged[str].connect(lambda:self.getKeyWindow())
        self.KKeywordCombo.currentIndexChanged[str].connect(lambda:self.getKeyWindow())
       
        
    def getHomeWindow(self):
        self.createHomeWindow().show()
        
        if self.KeyWordWindow.isVisible():
            self.KeyWordWindow.close()
        elif self.TopicWindow.isVisible():
                self.TopicWindow.close()
    def getKeyWindow(self):
        self.createKeywordWindow().show()
        if self.HomeWindow.isVisible():
            self.HomeWindow.close()
        elif self.TopicWindow.isVisible():
            self.TopicWindow.close()
            
    def getTopicWindow(self):
        self.createTopicWindow().show()
        if self.HomeWindow.isVisible():
            self.HomeWindow.close()
        elif self.KeywordWindow.isVisible():
                self.TopicWindow.close()            
   
        
    

    def runLoginWindow(self):
        
        self.LoginWindow.setWindowTitle("Login or Signup")
        self.LoginWindow.setGeometry(650,40,400,200)
        LinBut = QPushButton("Login",parent=self.LoginWindow)
        LinBut.adjustSize()
        LinBut.move(100,100)
        SignUpBut= QPushButton("Sign Up",parent = self.LoginWindow)
        SignUpBut.adjustSize()
        SignUpBut.move(200,100)
        self.LoginWindow.show()
        
    def getLanguage(self,language,txt):
        return language.getLanguage(txt)
        
    
    def generateMainComboBox(self) :

        self.TopicCombo.addItems(self.TopicBank)
        self.LanguageCombo.addItems(self.LanguageBank)
        #for la in self.LanguageBank:
         #  self.LanguageCombo.addItems(la)
        for item in self.KeywordBank:
           self.KeywordCombo.addItems(item)
            
       
    def generateKeywrdWindowComboBox(self) :
        
        self.KTopicCombo.addItems(self.TopicBank)
        self.KLanguageCombo.addItems(self.LanguageBank)
        self.KeywordBank.sort()
        for item in self.KeywordBank:
            if len(item) >0:
                self.KKeywordCombo.addItems(item)
            else:
                continue
    def generateTopicWindowComboBox(self):
        self.TTopicCombo.addItems(self.TopicBank)
        self.TLanguageCombo.addItems(self.LanguageBank)
        
        for item in self.KeywordBank:
            if len(item) >0:
                self.TKeywordCombo.addItems(item)
            else:
                continue
    def searchHome(self):
        x =self.SearchBar.text()
        self.KeywordBinarySearchBar(x)
        self.createKeywordWindow().show()
        
        
    def createHomeWindow(self):
        
        searchCompleter = QCompleter(Language.KeywordBank.pop())
        searchCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        searchLabel = QLabel("Search Keyword",parent=self.HomeWindow)
        searchLabel.move(900, 7)
        self.SearchBar.setFixedSize(200, 20)
        self.SearchBar.move(1000,10)
        self.SearchBar.setCompleter(searchCompleter)
        #self.SearchBar.textChanged[str].connect(self.searchHome())
        
        
        self.HomeWindow.setWindowTitle("Programmer's QuickGuide Application")
        self.HomeWindow.setGeometry(100, 100, 2000, 1400)
        
        self.Header = QLabel("<h1>A Programmer's QuickGuide </h1>", parent=self.HomeWindow)
        self.Header.move(120, 10)
        self.Header.adjustSize()
        
        self.Header2 =QLabel("<h1> HOME </h1>", parent = self.HomeWindow)
        self.Header2.move(650,40)
        self.LoginButton = QPushButton("Login", parent = self.HomeWindow)
        self.LoginButton.move(0,100)
       
        self.LoginButton.clicked.connect(lambda:self.runLoginWindow())
       
        
        self.LogOutButton = QPushButton("Log Out",parent =self.HomeWindow)
        self.LogOutButton.move(0,1000)
        
        self.HomeButton = QPushButton(self.HomeWindow)
        self.HomeButton.resize(60,60)
        self.HomeButton.setIconSize(QSize(60,60))
        self.HomeButton.setIcon(self.HomeIcon)
        self.HomeButton.move(20,30)
       
        
        TopicLabel = QLabel("Topics",parent=self.TopicCombo)
        LanguageLabel = QLabel("Select A Language",parent = self.LanguageCombo)
        KeywordLabel = QLabel("Keywords A-Z",parent = self.KeywordCombo)
        
        Label = QLabel("Language:",parent=self.HomeWindow)
        Label.move(450,300)
        Label.adjustSize()
        
        
        
        self.generateMainComboBox()
        
        
        self.TopicCombo.setItemText(0,"SELECT A TOPIC")
      
        self.LanguageCombo.setItemText(0,"SELECT A LANGUAGE")
     
        self.KeywordCombo.setItemText(0,"SELECT A KEYWORD")
        
        self.TopicCombo.setGeometry(11, 300, 150, 70)
      
        self.LanguageCombo.setGeometry(11, 500, 150, 70)
     
        self.KeywordCombo.setGeometry(13, 400, 150, 70)
        
        
        
        
        return self.HomeWindow
   

 
    
    def createAppGUI(self):
        
        self.createHomeWindow().show()
        self.createKeywordWindow().show()
        self.createTopicWindow().show
        
        
    def createTopicWindow(self):
           
        self.TopicWindow.setWindowTitle("Programmer's QuickGuide Application")
        self.TopicWindow.setGeometry(100, 100, 2000, 1400)
        
        self.Header = QLabel("<h1>A Programmer's QuickGuide </h1>", parent=self.TopicWindow)
        self.Header.move(120, 20)
        self.Header.adjustSize()
        self.Header2 =QLabel("<h1> TOPICS </h1>", parent = self.TopicWindow)
        self.Header2.move(650,40)
        
        self.LoginButton = QPushButton("Login", parent = self.TopicWindow)
        self.LoginButton.move(0,100)
        
        self.NewUserButton = QPushButton("New User",parent =self.TopicWindow)
        self.NewUserButton.move(700,1000)
        
        self.LogOutButton = QPushButton("Log Out",parent =self.TopicWindow)
        self.LogOutButton.move(0,1000)
        
        self.HomeButton = QPushButton(self.TopicWindow)
        self.HomeButton.resize(60,60)
        self.HomeButton.setIconSize(QSize(60,60))
        self.HomeButton.setIcon(self.HomeIcon)
        self.HomeButton.move(20,30)
       
        
        TTopicLabel = QLabel("Topics",parent=self.TTopicCombo)
        TLanguageLabel = QLabel("Select A Language",parent = self.TLanguageCombo)
        TKeywordLabel = QLabel("Keywords A-Z",parent = self.TKeywordCombo)
        
        Topic1 = QLabel("Topic:",parent=self.TopicWindow)
        Topic1.move(450,300)
        Topic1.adjustSize()
        TopicL = QLabel(Topic.TopicInformation,parent = self.TopicWindow)
        
        
        self.generateTopicWindowComboBox()
        
        
        self.TTopicCombo.setItemText(0,"SELECT A TOPIC")
   
        self.TLanguageCombo.setItemText(0,"SELECT A LANGUAGE")
  
        self.TKeywordCombo.setItemText(0,"SELECT A KEYWORD")
     
        self.TTopicCombo.setGeometry(10, 300, 150, 70)
   
        self.TLanguageCombo.setGeometry(10, 500, 150, 70)
  
        self.TKeywordCombo.setGeometry(10, 400, 150, 70)
        
        
        TC = self.TopicCombo.currentText()
        LC =self.LanguageCombo.currentText()
        KC =self.KeywordCombo.currentText()
        
        
    
        
        return self.TopicWindow
    
    def createKeywordWindow(self):
        
        self.KeyWordWindow.setWindowTitle("Programmer's QuickGuide Application")
        self.KeyWordWindow.setGeometry(100, 100, 2000, 1400)
        
        self.Header = QLabel("<h1>A Programmer's QuickGuide </h1>", parent=self.KeyWordWindow)
        self.Header.move(120, 10)
        self.Header.adjustSize()
        
        self.Header2 =QLabel("<h1> KEYWORDS </h1>", parent = self.KeyWordWindow)
        self.Header2.move(650,40)
        
        KeywordLabel = QLabel('Keyword:',parent = self.KeyWordWindow)
        KeywordL = QLabel(Keyword.word, parent = self.KeyWordWindow)
        KeywordLabel.move(450,150)
        KeywordLabel.adjustSize()
        
        DescriptionLabel = QLabel("Description:",parent = self.KeyWordWindow)
        Description = QLabel(Keyword.Description,parent = DescriptionLabel)
        DescriptionLabel.move(450,285)
        Description.move(450,230)
        DescriptionLabel.adjustSize()
        Description.adjustSize()
        
        ExampleLabel = QLabel("Examples: ", parent = self.KeyWordWindow)
        Example = QLabel(Keyword.Examples,parent = ExampleLabel)
        ExampleLabel.move(450,385)
        Example.move(450,330)
        ExampleLabel.adjustSize()
        Example.adjustSize()
        self.LoginButton = QPushButton("Login", parent = self.KeyWordWindow)
        self.LoginButton.move(0,100)
        
        self.NewUserButton = QPushButton("New User",parent =self.KeyWordWindow)
        self.NewUserButton.move(700,1000)
        
        self.LogOutButton = QPushButton("Log Out",parent =self.KeyWordWindow)
        self.LogOutButton.move(0,1000)
        
        self.HomeButton = QPushButton(self.KeyWordWindow)
        self.HomeButton.resize(60,60)
        self.HomeButton.setIconSize(QSize(60,60))
        self.HomeButton.setIcon(self.HomeIcon)
        self.HomeButton.move(20,30)
        
        TopicLabel = QLabel("Topics",parent=self.KTopicCombo)
        LanguageLabel = QLabel("Select A Language",parent = self.KLanguageCombo)
        KeywordLabel = QLabel("Keywords A-Z",parent = self.KKeywordCombo)
    
        
        
        
        self.generateKeywrdWindowComboBox()
     
        self.KTopicCombo.setItemText(0,"SELECT A TOPIC")
      
        self.KLanguageCombo.setItemText(0,"SELECT A LANGUAGE")
     
        self.KKeywordCombo.setItemText(0,"SELECT A KEYWORD")
        
        self.KTopicCombo.setGeometry(10, 300, 150, 70)
      
        self.KLanguageCombo.setGeometry(10, 500, 150, 70)
     
        self.KKeywordCombo.setGeometry(10, 400, 150, 70)
        
        
        return self.KeyWordWindow
     
  
    
    def KeywordBinarySearchBar(self,keyword):
        self.KeywordBank.pop().sort()
        n = len(self.KeywordBank)
        x = 0 
        y = n - 1
        while(x <= y):
            m = x + (y - x)/2
            
            # find middle element in list
            if self.KeywordBank[x] == keyword:
                
                return self.KeywordBank[x]
            
            #if x is alhabetically greater than the next word
            elif self.KeywordBank[x] > self.KeywordBank[x+1]:
                #ignore left half of the list
                x = m + x
            else:
                y = m - x
        print(keyword,"Not Found")  

    


def main():
    
    
    
    Python = Language()
    
    Language.addLanguage(Python,"Python")
    
    file = open('/Users/emily/Desktop/CS 4910 - Senior Project/KeywordsDoc.txt')
    
    for line in file.readlines():
        fname = line.rstrip().split(',') #using rstrip to remove the \n
        Language.addKeyword(fname,Python)
    
    
    file2 = open('/Users/emily/Desktop/CS 4910 - Senior Project/languages.txt')
    for line1 in file2.readlines():
       xname = line1.rstrip().split('\n') #using rstrip to remove the \n
        
       newLang = Language()
       Language.addLanguage(newLang,xname.pop())
    
    file3 = open('/Users/emily/Desktop/CS 4910 - Senior Project/Topics.txt')
    for line2 in file2.readlines():
       Tname = line2.rstrip().split('\n') #using rstrip to remove the \n
       Language.addTopic(Tname)
      
        
    app = QApplication(sys.argv)
    
    mainGui = GUI()
    mainGui.initGUI()
    
    
    homewindow = mainGui.createHomeWindow()
    #wordWindow = mainGui.createKeywordWindow()
    tWindow = mainGui.createTopicWindow()
    #wordWindow.show()
    homewindow.show()
    tWindow.show()
    sys.exit(app.exec_())
    
    file.close()
    file2.close()
if __name__ == '__main__':
    main()        
           
   
           
           
           
           