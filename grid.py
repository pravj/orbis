#!/usr/bin/python

try:
	from gi.repository import Gtk, Gdk
except ImportError:
	raise Exception('unable to import required module')

from config import Config
from pallete import Pallete

import random


class Grid(Gtk.Window):

	def __init__(self):
		# global configurations
		self.cfg = Config()

		# array of all blocks in grid
		self.Blocks = []

		# array of colors in pallete
		self.colors = self.cfg.colors		

		# create a window and table
		Gtk.Window.__init__(self, title=self.cfg.name)
		self.table = Gtk.Table(self.cfg.size, self.cfg.size, True)
		
		# pallete element to be added
		self.pallete = Pallete()
		
		# add generated table to window
		self.add(self.table)
		self.generate_table()
		self.add_pallete()

		# activate stylesheet
		self.add_style()

	"""
	return n'th number block
	( n = cfg.size*x + y )
	where (x,y) shows indeces in multi-dimension array
	"""
	def block(self, n):
		button = Gtk.Button(label='---')
		button.set_name('%s' % (random.choice(self.colors)))
		button.connect('clicked', self.block_click)
		# row and column indeces for multi-dimension array
		button.r, button.c = (n-1)/self.cfg.size, (n-1) % self.cfg.size
		return button

	def block_click(self, button):
		print button.get_name()
		print button.r
		print button.c

	"""
	helps to arrange each block in table
	according to its indeces in 2D-array
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
	def generate_table(self):
		# prepare 2D-array of blocks
		for i in range(0, self.cfg.size):
			temp = []
			for j in range(0, self.cfg.size):
				temp.append(self.block(i * self.cfg.size + j + 1))
			self.Blocks.append(temp)

		# attach/arrange blocks in table
		for k in range(0, self.cfg.total):
			x,y = k/(self.cfg.size), k % (self.cfg.size)
			pos = self.arrangment(x, y)
			self.table.attach(self.Blocks[x][y], pos[0], pos[1], pos[2], pos[3])

	"""
	adds color pallete to grid's table layout
	"""
	def add_pallete(self):
		self.pallete.attach_pallete(self.table)

	"""
	adds stylesheet for appropriete elements
	"""
	def add_style(self):
		style = Gtk.CssProvider()

		with open('assets/pallete.css', 'r') as f:
			css = f.read()
			f.close()
		
		style.load_from_data(css)
		sppa = Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
		Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), style, sppa)

