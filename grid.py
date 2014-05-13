#!/usr/bin/python
from gi.repository import Gtk


# grid-dimension
width = 15
height = 15

class Grid(Gtk.Window):

	def __init__(self):
		self.w = width
		self.h = height
		self.total = self.w*self.h

		Gtk.Window.__init__(self, title='game')
		table = Gtk.Table(self.w, self.h, True)
		self.add(table)

		dots = []
		for i in range(0, self.total):
			dots.append(Gtk.Button(label='.'))

		for j in range(0, self.total):
			res = self.arrangment(j/self.w, j%(self.h))
			table.attach(dots[j], res[0], res[1], res[2], res[3])

	def arrangment(self, x, y):
		result = [0,0,0,0]
		result[0] = y
		result[1] = y+1
		result[2] = x
		result[3] = x+1
		return result
				

grid = Grid()
grid.connect('delete-event', Gtk.main_quit)
grid.show_all()
Gtk.main()

