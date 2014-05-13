#!/usr/bin/python

from gi.repository import Gtk
from config import Config

class Grid(Gtk.Window):

	def __init__(self):
		# global configurations
		self.cfg = Config()

		# array of all blocks in grid
		self.Blocks = []
		
		# create a window, add generated table to window
		Gtk.Window.__init__(self, title=self.cfg.name)
		self.table = Gtk.Table(self.cfg.size, self.cfg.size, True)
		self.add(self.table)
		self.generateTable()

	"""
	generates elements in table
	"""
	def generateTable(self):
		# prepare array of blocks
                for i in range(0, self.cfg.total):
                        self.Blocks.append(self.block(i+1))

		# attach/arrange blocks in table
                for j in range(0, self.cfg.total):
                        res = self.arrangment(j/(self.cfg.size), j%(self.cfg.size))
                        self.table.attach(self.Blocks[j], res[0], res[1], res[2], res[3])

	"""
	return n'th number block
	( n = cfg.size*x + y )
	where (x,y) shows indeces in multi-dimension array
	"""
	def block(self, n):
		return Gtk.Button(label='%d'%(n))

	"""
	helps to arrange each block in table
	according to its indeces in multi-dimension array
	"""
	def arrangment(self, x, y):
		"""
		returns a tuple object showing position in table table
		ex. (a,a+1,b,b+1) => element in a'th column and b'th row
		"""
		return (y, y+1, x, x+1)


grid = Grid()
grid.connect('delete-event', Gtk.main_quit)
grid.show_all()
Gtk.main()

