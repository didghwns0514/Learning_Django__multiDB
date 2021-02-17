"""
	Flask app.py 테스트
	~~~~~~~~~~~~~~~~~~~
"""

from StoreScript.Scripts.Flask.app import clsFlask

def test__clsFlask():
	"""
	to test class definition in clsFlask
	:return: -
	"""

	# @ check static
	tmp_cls = clsFlask()
	tmp_cls._runProcess(module=False)