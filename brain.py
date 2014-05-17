#!/usr/bin/python


class Brain:

	def __init__(self, Array):

		# array, that is being used in all the process
		# here, it'll be a 2D array representing Game Grid
		self.Array = Array

	def floodfill(self, node, target, replace):
		# using recursion for now

		if (node.get_name() != target):
			return
		else:
			# changes its color
			node.set_name(replace)

			for nodes in self.neighbors(node):
				self.floodfill(nodes, target, replace)
	
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
			neighbors.append(grid[x+1][y])
		if (y+1 < N):
			neighbors.append(grid[x][y+1])
		if (y != 0):
			neighbors.append(grid[x][y-1])
		if (x != 0):
			neighbors.append(grid[x-1][y])

		return neighbors
