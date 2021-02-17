"""
	파일 로케이션 관리 class
	~~~~~~~~~~~~~~~~~~~~~~
"""

import os
import pathlib


class Fileloc:
	"""
	파일 로케이션 관리 부분
	"""
	PATH = pathlib.Path(__file__).parent.absolute().parents[2] ## root of RoboChicken_new

	JSON ={

		"Sqlite":{
			"SqliteOP.py" : {
				'db_auth' : os.path.join(PATH, 'DB.auth.sqlite3'),
				'db_store' : os.path.join(PATH, 'DB.store.sqlite3')
			}
		},

		"Flask":{
			"app.py" :{
				'json_client_secret' : os.path.join(PATH, 'StoreScript', 'Scripts', 'Flask', 'client_secret.json')
			}
		},

		"TEST" : {
			"TEST.py" : {
				'dummy' : 'is dummy'
			}
		}


	}


	@staticmethod
	def getloc(module_type:str, py_file_name:str, tag:str):
		"""
		JSON에서 location 위치를 돌려주는 method
		:param module_type: first key as module Folder name
		:param py_file_name: second key as python file name
		:param tag: third key as file location
		:return: return path
		"""

		try:
			return Fileloc.JSON[module_type][py_file_name][tag]

		except KeyError:
			return 'null'





