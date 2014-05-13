"""
global configurations
"""

# grid-size
size = 16

# number of blocks
total = size*size

# game's name and title for main window
name = 'Game'

class Config:
	def __init__(self):
		self.size = size
		self.total = total
		self.name = name

