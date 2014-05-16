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

		# pallete object : 'Array'
		self.pallete = []

		# prepare the pallete
		self.prepare()

		# current active color in pallete
		self.active = None

	"""
	prepare the color pallete to be added in grid
	"""
	def prepare(self):
		for i in range(6):
			button = Gtk.Button(label='---')	
			button.set_name(self.colors[i])
			button.connect('clicked', self.pallete_click)
			self.pallete.append(button)

	"""
	return the prepared pallete instance
	"""
	def instance(self):
		return self.pallete

	"""
	attach the pallete in given grid's table layout
	"""
	def attach_pallete(self, table):
		pallete = self.instance()
		for i in range(6):
			table.attach(pallete[i], 2*(i+1), 2*(i+2), self.cfg.size, self.cfg.size+2)

	"""
	set active color on clicking pallete
	"""
	def pallete_click(self, button):
		# clicking same color in pallete again 
		if button.get_name() == self.active:
			pass

		else:
			self.active = button.get_name()

