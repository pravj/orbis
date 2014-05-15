#!/usr/bin/python

try:
	from gi.repository import Gtk
except ImportError:
	raise Exception('unable to import required module')

from config import Config


class Pallete:
	
	def __init__(self):
		# global configurations
		self.cfg = Config()
	
		# array of colors used in pallete
		self.colors = self.cfg.colors

		# pallete object : type 'Array'
		self.pallete = []

		# prepare the pallete
		self.prepare()

	"""
	prepare the color pallete to be added in grid
	"""
	def prepare(self):
		for i in range(6):
			button = Gtk.Button(label='---')
			button.set_name(self.colors[i])
			self.pallete.append(button)

	"""
	return the prepared pallete instance
	"""
	def instance(self):
		return self.pallete

	"""
	attach the pallete in grid's table layout
	"""
	def attach_pallete(self, table):
		pallete = self.instance()
		for i in range(6):
			table.attach(pallete[i], 2*(i+1), 2*(i+2), self.cfg.size, self.cfg.size+2)

