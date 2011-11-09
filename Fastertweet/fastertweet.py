#!/usr/bin/python
import gtk.gdk
import pynotify
import sys
import tweepy 
from PyQt4 import QtGui, QtCore 
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout,QSystemTrayIcon
import os 

class Example(QtGui.QMainWindow):

    
	def __init__(self):
	        super(Example, self).__init__()
		

		self.path=sys.path[0]
		f=open('%s/ACCESS_KEY'% self.path,'r')
		f1=open('%s/ACCESS_SECRET'% self.path,'r')
		f2=open('%s/user_info'% self.path)
		self.user_name=f2.readline().strip('\n')
		self.user_id=f2.readline().strip('\n')
		self.a=f.readline().strip('\n')
		self.b=f1.readline().strip('\n')
		f.close()
		f1.close()
		f2.close()
		self.initUI()
		
	def initUI(self):   
		
		self.icon=QSystemTrayIcon()
		self.icon.isSystemTrayAvailable() 
		self.icon.setIcon( QtGui.QIcon('%s/web.png'% self.path) )
		self.icon.setToolTip ( 'dubbleclick to maximize')
		self.icon.show()
		self.icon.activated.connect(self.activate)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setGeometry(300, 300, 1500, 1000)
		frame = QtGui.QFrame(parent=self)
                frame.setStyleSheet("QFrame {background: rgba(0,0,0,50%)}")
		box=QtGui.QHBoxLayout()
		
		self.edit = QtGui.QLineEdit()
        	self.edit.setStyleSheet("background: rgba(0,0,0,100%); "" font-weight : bold;" "color:  rgb(250,250,250);""border:5px solid ")
		self.edit.setToolTip('please  <b>Enter your tweet here </b> ')
		self.edit.returnPressed.connect(self.returnPressed)
                box.addWidget(self.edit)	
		
		frame.setLayout(box)
	

		qbtn1 = QtGui.QPushButton('quit', self)
	        qbtn1.clicked.connect(self.close)
		qbtn1.setStyleSheet( "background: rgba(0,0,0,100%); "" font-weight : bold;" "color:  rgb(250,250,250);""border:5px solid ")
	        box.addWidget(qbtn1)
		self.statusBar().setStyleSheet("background: rgba(0,0,0,100%);"" font-weight : bold;" "color:  rgb(250,250,250)")
		self.statusBar().showMessage('Press Enter to send Tweet and press ESC to minimize to tray ')

		
		self.setCentralWidget(frame)  
		self.setWindowIcon(QtGui.QIcon('%s/web.png' % self. path)) 
		

	        self.setWindowTitle('Tweet Fast ')
		self.center()    
	        self.show()
		self.twitter_auth()
		
	def twitter_auth(self):
		
		CONSUMER_KEY = 'VQLDtkDTlbAmT95m5cMsYQ'
		CONSUMER_SECRET = 'bAC0BF69qiEVARJlfFJZZCDQ9mrcqofq16ilQ4OjU'      
		ACCESS_KEY=self.a
		ACCESS_SECRET=self.b
		self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	        

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Escape:
			print 'Escape wass pressed '
			self.icon.show()
			
                        self.hide()
	def activate(self,reason ):
			print reason 
			if reason==2:
				self.show()
	
	def center(self):
        
	        qr = self.frameGeometry()
	        cp = QtGui.QDesktopWidget().availableGeometry().center()
	        qr.moveCenter(cp)
	        self.move(qr.topLeft())

	def returnPressed(self):
		path=sys.path[0]
		tweet = self.edit.text()
		api = tweepy.API(self.auth)
		self.statusBar().showMessage('Sending... ')
		api.update_status(tweet) 
		self.statusBar().showMessage('Your Tweet was send ')
		n = pynotify.Notification(" @ %s "% self.user_name , "your tweet was send ","%s/%s.jpg" % (path,self.user_id))
                n.set_hint('x', 200)
                n.set_hint('y', 400)
                pynotify.init('n')		
                n.show()
		self.statusBar().showMessage('Press Enter to send Tweet and press ESC to minimize to tray ')
		self.edit.clear()
        
	

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

