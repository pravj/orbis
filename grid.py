#!/usr/bin/python

from gi.repository import Gtk
from config import Config


class Grid(Gtk.Window):

	def __init__(self):
		# global configurations
		self.cfg = Config()

		# array of all blocks in grid
		self.Blocks = []

		# create a window and table
		Gtk.Window.__init__(self, title=self.cfg.name)
		self.table = Gtk.Table(self.cfg.size, self.cfg.size, True)

		# add generated table to window
		self.add(self.table)
		self.generateTable()
		self.addPallete()

	"""
	return n'th number block
	( n = cfg.size*x + y )
	where (x,y) shows indeces in multi-dimension array
	"""
	def block(self, n):
		return Gtk.Button(label='%d' % (n))

	"""
	helps to arrange each block in table
	according to its indeces in multi-dimension array
	"""
	def arrangment(self, x, y):
		"""
		returns a tuple object showing position in table
		ex. (a,a+1,b,b+1) => element in a'th column and b'th row
		"""
		return (y, y+1, x, x+1)

	"""
	generates elements in table
	"""
	def generateTable(self):
		# prepare array of blocks
		for i in range(0, self.cfg.total):
			self.Blocks.append(self.block(i+1))

		# attach/arrange blocks in table
		for j in range(0, self.cfg.total):
			pos = self.arrangment(j/(self.cfg.size), j % (self.cfg.size))
			self.table.attach(self.Blocks[j], pos[0], pos[1], pos[2], pos[3])

	"""
	adds color pallete
	"""
	def addPallete(self):
		self.table.attach(Gtk.Button(label='1'), 2,4,16,18)
		self.table.attach(Gtk.Button(label='2'), 4,6,16,18)
		self.table.attach(Gtk.Button(label='3'), 6,8,16,18)
		self.table.attach(Gtk.Button(label='4'), 8,10,16,18)
		self.table.attach(Gtk.Button(label='5'), 10,12,16,18)
		self.table.attach(Gtk.Button(label='6'), 12,14,16,18)

grid = Grid()
grid.connect('delete-event', Gtk.main_quit)
grid.show_all()
Gtk.main()
