"""
global configurations
"""

# grid-size
size = 16

# number of blocks
total = size*size

# game's name and title for main window
name = 'Game'

# array of colors in pallete
colors = ['ross', 'rachel', 'monica', 'joey', 'phoebe', 'chandler']

# css file path for button's color pallete
css = 'assets/pallete.css'

class Config:
	def __init__(self):
		self.size = size
		self.total = total
		self.name = name
		self.colors = colors
		self.css = css

