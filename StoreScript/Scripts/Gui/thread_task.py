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