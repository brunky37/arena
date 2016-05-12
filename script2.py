#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This program creates a quit
button. When we press the button,
the application terminates. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
import subprocess
import os

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):   
      
	windowHeight=400
	windowWidth=1200
      
        lstAgenda = QtGui.QListWidget(self)
        lstAgenda.setWindowTitle('Hola')
        lstAgenda.setFixedSize(windowWidth-150,370)
        lstAgenda.move(16,16)
        
        output=subprocess.Popen(["curl", "www.arenavision.in/agenda"], stdout=subprocess.PIPE).communicate()
	output=output[0]
	output=output[output.find('CET Time'):]
	output=output[output.find('<p>')+3:]
	output=output[:output.find('All schedule events')-5]
	while output.find('<br/>')!=-1:
	  line=output[1:output.find('<br/>')]
	  output=output[output.find('<br/>')+5:]	
	  lstAgenda.addItem(line)
	del output 
	del line
       
        btnEngine = QtGui.QPushButton('Engine', self)
        btnEngine.clicked.connect(engine_start)
        btnEngine.resize(102,32)
        btnEngine.move(windowWidth-110, 16)            
        
        btnAV1 = QtGui.QPushButton('AV1', self)
        btnAV2 = QtGui.QPushButton('AV2', self)
        btnAV3 = QtGui.QPushButton('AV3', self)
        btnAV4 = QtGui.QPushButton('AV4', self)
        btnAV5 = QtGui.QPushButton('AV5', self)
        btnAV6 = QtGui.QPushButton('AV6', self)
        btnAV7 = QtGui.QPushButton('AV7', self)
        btnAV8 = QtGui.QPushButton('AV8', self)
        btnAV9 = QtGui.QPushButton('AV9', self)
        btnAV10 = QtGui.QPushButton('AV10', self)
        btnAV11 = QtGui.QPushButton('AV11', self)
        btnAV12 = QtGui.QPushButton('AV12', self)
        btnAV13 = QtGui.QPushButton('AV13', self)
        btnAV14 = QtGui.QPushButton('AV14', self)
        btnAV15 = QtGui.QPushButton('AV15', self)
        btnAV16 = QtGui.QPushButton('AV16', self)
        btnAV17 = QtGui.QPushButton('AV17', self)
        btnAV18 = QtGui.QPushButton('AV18', self)
        btnAV19 = QtGui.QPushButton('AV19', self)
        btnAV20 = QtGui.QPushButton('AV20', self)
        
        btnAV1.clicked.connect(curl_av1)
	btnAV1.resize(48,32)
        btnAV1.move(windowWidth-110, windowHeight-334)       
        
        btnAV2.clicked.connect(curl_av2)
	btnAV2.resize(48,32)
        btnAV2.move(windowWidth-55, windowHeight-334)    
        
        btnAV3.clicked.connect(curl_av3)
	btnAV3.resize(48,32)
        btnAV3.move(windowWidth-110, windowHeight-302) 

        btnAV4.clicked.connect(curl_av4)
	btnAV4.resize(48,32)
        btnAV4.move(windowWidth-55, windowHeight-302)    
        
        btnAV5.clicked.connect(curl_av5)
	btnAV5.resize(48,32)
        btnAV5.move(windowWidth-110, windowHeight-270) 

        btnAV6.clicked.connect(curl_av6)
	btnAV6.resize(48,32)
        btnAV6.move(windowWidth-55, windowHeight-270) 

        btnAV7.clicked.connect(curl_av7)
	btnAV7.resize(48,32)
        btnAV7.move(windowWidth-110, windowHeight-238) 

        btnAV8.clicked.connect(curl_av8)
	btnAV8.resize(48,32)
        btnAV8.move(windowWidth-55, windowHeight-238) 
        
        btnAV9.clicked.connect(curl_av9)
	btnAV9.resize(48,32)
        btnAV9.move(windowWidth-110, windowHeight-206) 

        btnAV10.clicked.connect(curl_av10)
	btnAV10.resize(48,32)
        btnAV10.move(windowWidth-55, windowHeight-206)
                 
        btnAV11.clicked.connect(curl_av11)
	btnAV11.resize(48,32)
        btnAV11.move(windowWidth-110, windowHeight-174)       
        
        btnAV12.clicked.connect(curl_av12)
	btnAV12.resize(48,32)
        btnAV12.move(windowWidth-55, windowHeight-174)    
        
        btnAV13.clicked.connect(curl_av13)
	btnAV13.resize(48,32)
        btnAV13.move(windowWidth-110, windowHeight-142) 

        btnAV14.clicked.connect(curl_av14)
	btnAV14.resize(48,32)
        btnAV14.move(windowWidth-55, windowHeight-142)    
        
        btnAV15.clicked.connect(curl_av15)
	btnAV15.resize(48,32)
        btnAV15.move(windowWidth-110, windowHeight-110) 

        btnAV16.clicked.connect(curl_av16)
	btnAV16.resize(48,32)
        btnAV16.move(windowWidth-55, windowHeight-110) 

        btnAV17.clicked.connect(curl_av17)
	btnAV17.resize(48,32)
        btnAV17.move(windowWidth-110, windowHeight-78) 

        btnAV18.clicked.connect(curl_av18)
	btnAV18.resize(48,32)
        btnAV18.move(windowWidth-55, windowHeight-78) 
        
        btnAV19.clicked.connect(curl_av19)
	btnAV19.resize(48,32)
        btnAV19.move(windowWidth-110, windowHeight-46) 

        btnAV20.clicked.connect(curl_av20)
	btnAV20.resize(48,32)
        btnAV20.move(windowWidth-55, windowHeight-46)     
        
        
        self.setGeometry(40, 360, 470, 350)
        self.setFixedSize(windowWidth,windowHeight)
        self.setWindowTitle('Arenavision Links')    
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    


@pyqtSlot()
def engine_start():
    subprocess.Popen(["acestreamengine", "--client-gtk"])
    
 
@pyqtSlot()
def curl_av1():
    output=subprocess.Popen(["curl", "www.arenavision.in/av1"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]    
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av2():
    output=subprocess.Popen(["curl", "www.arenavision.in/av2"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av3():
    output=subprocess.Popen(["curl", "www.arenavision.in/av3"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av4():
    output=subprocess.Popen(["curl", "www.arenavision.in/av4"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av5():
    output=subprocess.Popen(["curl", "www.arenavision.in/av5"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av6():
    output=subprocess.Popen(["curl", "www.arenavision.in/av6"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av7():
    output=subprocess.Popen(["curl", "www.arenavision.in/av7"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av8():
    output=subprocess.Popen(["curl", "www.arenavision.in/av8"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av9():
    output=subprocess.Popen(["curl", "www.arenavision.in/av9"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av10():
    output=subprocess.Popen(["curl", "www.arenavision.in/av10"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av11():
    output=subprocess.Popen(["curl", "www.arenavision.in/av11"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av12():
    output=subprocess.Popen(["curl", "www.arenavision.in/av12"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av13():
    output=subprocess.Popen(["curl", "www.arenavision.in/av13"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av14():
    output=subprocess.Popen(["curl", "www.arenavision.in/av14"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av15():
    output=subprocess.Popen(["curl", "www.arenavision.in/av15"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av16():
    output=subprocess.Popen(["curl", "www.arenavision.in/av16"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av17():
    output=subprocess.Popen(["curl", "www.arenavision.in/av17"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av18():
    output=subprocess.Popen(["curl", "www.arenavision.in/av18"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
    
 
@pyqtSlot()
def curl_av19():
    output=subprocess.Popen(["curl", "www.arenavision.in/av19"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 
@pyqtSlot()
def curl_av20():
    output=subprocess.Popen(["curl", "www.arenavision.in/av20"], stdout=subprocess.PIPE).communicate()
    output=output[0]
    output=output[output.find('acestream:'):]
    output=output[:output.find('"')]
    subprocess.Popen(["acestreamplayer", output], stdout=subprocess.PIPE).communicate()
    del output
 

  

if __name__ == '__main__':
    main()
