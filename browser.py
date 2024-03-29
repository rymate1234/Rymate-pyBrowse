#!/usr/bin/env python
import sys
import webkit
import gnome.ui
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)
	
APPNAME="Rymate pyBrowse"
APPVERSION="0.1"
	
class HelloWorldGTK:
	def __init__(self):
		gnome.init(APPNAME, APPVERSION)
		
		#Set the Glade file
		self.gladefile = "gui.glade"  
	        self.wTree = gtk.glade.XML(self.gladefile) 
	        
	        #woo testing!
	        self.view = webkit.WebView()
                self.wTree.get_widget("scroll").add(self.view)
                self.view.open("http://google.com")
		
		#Sets connections and stuff
		dic = { "on_btnGo_clicked" : self.btnGo_clicked }
                self.wTree.signal_autoconnect(dic)
		
		self.go = self.wTree.get_widget("button3")
		self.window = self.wTree.get_widget("Window")
		if (self.window):
			self.window.connect("destroy", gtk.main_quit)
		self.window.show_all()
		
	def btnGo_clicked(self, widget):
	        url = self.wTree.get_widget("entry1").get_text()
	        self.view.open(url)

if __name__ == "__main__":
	hwg = HelloWorldGTK()
	gtk.main()
			
