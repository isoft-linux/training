#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("delete-event", gtk.main_quit)
window.set_size_request(300, 200)
   
label = gtk.Label("Hello World")
window.add(label)
    
window.show_all()

gtk.main()

