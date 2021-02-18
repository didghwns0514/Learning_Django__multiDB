"""
	SQlite 클래스
	~~~~~~~~~~~~
"""
import sqlite3
import os
from StoreScript.Configuration.Base.fileloc_class import Fileloc
from StoreScript.Configuration.Base.cnfclass import cSqlite


class Sqlite(object):
	"""Sqlite handle class"""
	FOLDER = 'Sqlite'
	FILE = "SqliteOP.py"

	@staticmethod
	def _get_fileloc(_type:str)-> str:
		"""
		returns db location from configuration file
		:param _type:
		:return:
		"""
		return Fileloc.getloc(Sqlite.FOLDER, Sqlite.FILE, _type)

	@staticmethod
	def _check_existance(_type:str)-> bool:
		"""
		returns if db exists
		:param _type: type of db using
		:return: boolean
		"""

		if _type == 'db_auth':
			targ_file = Sqlite._get_fileloc(_type)

		elif _type == 'db_store':
			targ_file = Sqlite._get_fileloc(_type)

		else:
			raise ValueError('Wrong type of db chosen in SqliteOP')

		if os.path.isfile(targ_file):
			return True
		else:
			return False


	def _access_db(self, _type:str, query_list:list)-> list:
		"""
		load db and execute sqlite query
		:param _type: type of db using
		:param query_list: list of queries included
		:return: return_container
		"""
		return_container = []


		with sqlite3.connect(Sqlite._get_fileloc(_type),
							 isolation_level=cSqlite.isolation_lv.value)\
				as conn:

			# cursor variable
			cur = conn.cursor()

			for query in query_list:
				result = conn.execute(query)
				return_container.append(result)

		return return_container