#!/usr/bin/python

import os
import sys


class Sound:

	def __init__(self):
		# determine system info on instance creation
		# and stores here to prevent process on each sound play
		self.arch = self.system()

	"""
	helps to play sound on different systems accordingly
	it checks the current operating system environment
	"""
	def system(self):
		# platform identifier
		arch = sys.platform

		if (arch.startswith('linux')):
			return 1
		elif (arch.startswith('win32')):
			return 2
		elif (arch.startswith('darwin')):
			return 3
		else:
			return 4

	"""
	plays soundfile according to system environments
	"""
	def play(self, soundfile):
		# linux systems
		if (self.arch == 1):
			try:
				os.system('aplay %s >> /dev/null 2>&1' % (soundfile))
			except:
				pass #silence

		# windows systems
		elif (self.arch == 2):
			try:
				os.system('powershell -c (New-Object Media.SoundPlayer %s).PlaySync();' % (soundfile))
			except:
				pass

		# mac systems
		elif (self.arch == 3):
			try:
				os.system('afplay %s' % (soundfile))
			except:
				pass
		
		# others, stay silent
		else:
			pass
