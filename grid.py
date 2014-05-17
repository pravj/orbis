#!/usr/bin/python

try:
	from gi.repository import Gtk, Gdk
except ImportError:
	raise Exception('unable to import required module')

from brain import Brain
from config import Config
from pallete import Pallete

import random


class Grid(Gtk.Window):

	def __init__(self):
		# global configurations
		self.cfg = Config()

		# 2D-array having all blocks in grid
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

		# brain instance
		self.brain = Brain(self.Blocks)

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
		
		# top-left corner block clicked
		if (n==1):
			button.connect('clicked', self.right_block_click)
		# other blocks clicked
		else:
			button.connect('clicked', self.wrong_block_click)

		# row and column indeces for multi-dimension array
		button.x, button.y = (n-1)/self.cfg.size, (n-1) % self.cfg.size

		# color associated with block/button
		button.color = button.get_name()

		return button

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
	
	"""
	game moves ahead, only when player clicks top-left corner block
	"""
	def right_block_click(self, button):
		if (self.pallete.active != None):
			self.brain.floodfill(button, button.get_name(), self.pallete.active)
			print self.brain.filled
		else:
			pass

	"""
	when player clicks other then top-left corner block
	"""
	def wrong_block_click(self, button):
		pass

