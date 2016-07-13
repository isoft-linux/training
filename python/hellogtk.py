#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

def destroy(widget, data=None):
    gtk.main_quit()

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("destroy", destroy)
window.set_size_request(300, 200)
   
label = gtk.Label("Hello World")
label.show()
window.add(label)
    
window.show()

gtk.main()

