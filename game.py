#!/usr/bin/python

try:
	from gi.repository import Gtk, Gdk
except ImportError:
	raise Exception('unable to import required module')

from grid import Grid

grid = Grid()
grid.connect('delete-event', Gtk.main_quit)
grid.show_all()
Gtk.main()

