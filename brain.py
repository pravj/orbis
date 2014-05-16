#!/usr/bin/python

from config import Config


class Brain:

	def __init__(self, Array):

		# array, that is being used in all the process
		# here, it'll be a 2D array representing Game Grid
		self.Array = Array

	def floodfill(self, node, target, replace):

		# using recursion for now
		pass
	
	"""
	returns an array of nodes in neighbor of a node inside an NxN grid
	"""
	def neighbors(self, node):

		# grid represented by Array
		grid = self.Array

		# grid size
		N = len(grid)

		# indeces of node in 2D array(grid)
		x,y = node.x, node.y

		# array representing neighbors, elements in adjacent 4 directions
		neighbors = []
		if (x+1 < N):
			neighbors.append(grid[x+1][y].color)
		if (y+1 < N):
			neighbors.append(grid[x][y+1].color)
		if (y!=0):
			neighbors.append(grid[x][y-1].color)
		if (x!=0):
			neighbors.append(grid[x-1][y].color)

		return neighbors

