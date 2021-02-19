"""
	GUI main
	~~~~~~~~~
"""
import tkinter as tk
import time
import datetime
import asyncio
from queue import Queue

from thread_task import *
from Gui_sub_functions import *
from StoreScript.Configuration.Base.order import Order


class Gui(tk.Tk):
	"""
		Gui Main 띄우는 class
	"""
	def __init__(self, event_loop):
		"""class init 부분"""

		# parent class init : py2 compatible
		super(Gui, self).__init__() # tkinter.Tk.__init__()

		# set basic GUI params
		self.title("Pos-machine")
		self.geometry("400x400")


		# import queue
		self._tkQ = Queue()
		self._storeQ = Queue()

		# import thread for task
		#self._tkT = threadTask(self._tkQ) # shares memory of the Q

		# call build method
		self._buildAll()

		# acquire eventloop
		self._async_loop = event_loop
		#self._async_loop.run_until_complete(self.__main_async())
		threadAsync(self._async_loop, self.__main_async, self).start()


	async def __run_TkLoad(self):
		"""function to load tk root"""
		await asyncio.sleep(0.01)


	async def __run_TkUpdate(self):
		"""function to update Tk screen"""
		# update Tk. screeens
		while True:
			await asyncio.sleep(delay=0.5)
			print(f'you called __run_Tk : {datetime.datetime.now()}')


	async def __run_Store(self):
		"""function to run Store logic"""
		# run store logic
		while True:
			await asyncio.sleep(delay=1)
			print(f'you called __run_Store : {datetime.datetime.now()}')


	async def __main_async(self):
		"""function to schedule tasks"""
		self.async_t1 = asyncio.ensure_future(self.__run_TkUpdate())
		self.async_t2 = asyncio.ensure_future(self.__run_Store())

		await self.async_t1
		await self.async_t2

	def _loadThread(self, function):
		"""

		:param function: function to execute in thread
		:return: -
		"""
		def wrapper():
			self._tkQ.put(function)
			threadTask(self._tkQ).start()

		return wrapper


	def _buildAll(self):
		"""call other build functions for Tk"""

		# create button
		self._build_button()
		# create scrolldowns
		self._build_scrolldown()


	def _build_button(self):
		"""function to build buttons"""

		# 1)
		tk.Button(self, text="Add Order", command=self._loadThread(self.__f_add_order)).pack()


	def _build_scrolldown(self):
		"""function to build scrolldowns"""
		# 1)
		self._scroll__menu = tk.StringVar(self)
		self._scroll__menu.set(Order.OPTIONS[0])
		tk.OptionMenu(self, self._scroll__menu, *Order.OPTIONS).pack()


	def __f_add_order(self):
		print(f'reached add order!')
		self._storeQ.put(Order())
		print(f'check qsize in order! : {self._storeQ.qsize()}')


if __name__ == '__main__':
	main_lv_loop = asyncio.get_event_loop()
	root = Gui(main_lv_loop)
	root.mainloop()
