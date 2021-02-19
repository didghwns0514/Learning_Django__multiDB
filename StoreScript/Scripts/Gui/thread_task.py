"""
	Threading Class
	~~~~~~~~~~~~~~~~
"""
import threading


class threadTask(threading.Thread):
	"""threading 관리 class"""
	def __init__(self, qTh):
		"""
		class init 부분
		:param qTh: queue를 외부에서 받음
		"""

		# parent class init : py2 compatible
		super(threadTask, self).__init__()

		self.qTh = qTh


	def run(self):
		"""class method for executing start method in thread instance"""

		while not self.qTh.empty():
			try:
				tmp_funcObj = self.qTh.get()
				tmp_result = tmp_funcObj()
			except:
				pass
			finally:
				pass


class threadAsync(threading.Thread):
	"""single thread to run asyncio functions"""

	def __init__(self, event_loop, main_async, theWindow):
		"""

		:param event_loop: event loop from main of the program
		:param main_async: aync loop in Tk level
		:param theWindow: Tk class
		:return: -
		"""

		# inherit vars
		self.theWindow = theWindow
		self.loop = event_loop
		self.main_async_f = main_async


		# parent class init : py2 compatible
		super(threadAsync, self).__init__()


	def run(self):
		"""running thread using class method"""
		self.loop.run_until_complete(self.main_async_f())
