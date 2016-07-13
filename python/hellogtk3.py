#!/usr/bin/python
# -*- encoding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.set_size_request(300, 200)
window.connect("delete-event", Gtk.main_quit)

label = Gtk.Label("Hello World")
window.add(label)

window.show_all()

Gtk.main()

