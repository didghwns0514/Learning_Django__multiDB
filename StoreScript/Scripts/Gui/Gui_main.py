"""
	GUI main
	~~~~~~~~~
"""
import tkinter as tk
import time
import threading
from thread_task import *
from Gui_sub_functions import *
from queue import Queue


class Gui(tk.Tk):
	"""
		Gui Main 띄우는 class
	"""
	def __init__(self):
		"""class init 부분"""

		# parent class init : py2 compatible
		super(Gui, self).__init__() # tkinter.Tk.__init__()

		# set basic GUI params
		self.geometry("400x400")

		# import queue
		self._tkQ = Queue()
		self._storeQ = Queue()

		# import thread for task
		#self._tkT = threadTask(self._tkQ) # shares memory of the Q

		# call build method
		self._build()


	def _loadThread(self, function):
		"""

		:param function: function to execute in thread
		:return: -
		"""
		def wrapper():
			self._tkQ.put(function)
			threadTask(self._tkQ).start()

		return wrapper

		#self._tkT.start()



	def _build(self):
		"""call other build functions for Tk"""

		# create button
		self._build_button()

	def _build_button(self):
		"""function to build button

		!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		important to match text and callback functions
		!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		"""

		# set callback and pack it to tk
		tk.Button(self, text="click me", command=self._loadThread(self.__f_add_order)).pack()


	def __f_add_order(self):
		print(f'reached add order!')
		self._storeQ.put('order')
		print(f'check qsize in order! : {self._storeQ.qsize()}')


if __name__ == '__main__':
	root = Gui()
	root.mainloop()
