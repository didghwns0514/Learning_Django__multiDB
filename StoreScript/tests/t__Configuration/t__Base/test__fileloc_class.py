"""
	fileloc_class 테스트
	~~~~~~~~~~~~~~~~~~~
"""

from StoreScript.Configuration.Base.fileloc_class import Fileloc

def test__Fileloc():
	tmp_cls = Fileloc()

	print(f'tmp_cls.JSON : {tmp_cls.JSON}')
	print(f'tmp_cls.PATH : {tmp_cls.PATH}')
	print(f'type(tmp_cls.PATH) : {type(tmp_cls.PATH)}')

	assert tmp_cls.getloc("TEST", "TEST.py", 'dummy') == 'is dummy'
	assert tmp_cls.getloc("TEST", "_TEST.py", 'dummy') == 'null'
	assert tmp_cls.getloc("_TEST", "_TEST.py", 'dummy') == 'null'
