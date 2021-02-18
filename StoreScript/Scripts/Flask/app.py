"""
	Flask 로그인 인증 및 sqlite3 db 저장
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from oauth2client.contrib.flask_util import UserOAuth2
from flask import Flask
from StoreScript.Scripts.Sqlite.SqliteOP import SQlite
from StoreScript.Configuration.Base.fileloc_class import Fileloc
from StoreScript.Configuration.Base.cnfclass import cFlask

class clsFlask:

	APP = Flask(__name__)
	OAUTH2 = None
	LOGGED = False if cFlask.Option == True else True

	def __init__(self): pass

	@staticmethod
	def _runProcess(module=True):
		"""
		check db for existing user-name / key
		:param module: to check if function is called under a module, if standalone, get inputs for test
		:return: -
		"""

		if not module and not clsFlask.LOGGED:
			# _id = input('input client id : ')
			# _pass = input('input client pass : ')
			# clsFlask._get_auth_by_flask(_id, _pass)
			clsFlask._get_auth_by_flask()

	@staticmethod
	def _get_auth_by_flask(clientID:str=None, clientSECRET:str=None):
		"""
		to connect to google api
		:param clientID: client id input
		:param clientSECRET: client pswd input
		:return:
		"""


		# SingleTone
		if clsFlask.OAUTH2 == None:

			clsFlask.APP.config['SECRET_KEY'] = 'knowhowfactory'

			# API 사용을 위해서 아래와 같이 관련 정보를 담은 json 파일(개발자 페이지에서 받을 수 있다)을 사용할 수 있고,
			clsFlask.APP.config['GOOGLE_OAUTH2_CLIENT_SECRETS_FILE'] = Fileloc.getloc('Flask', 'app.py', 'json_client_secret')

			# 이렇게 코드에 직접 넣을 수도 있다.
			# clsFlask.APP.config['GOOGLE_OAUTH2_CLIENT_ID'] = str(clientID)
			# clsFlask.APP.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = str(clientSECRET)

			clsFlask.OAUTH2 = UserOAuth2(clsFlask.APP)


	@APP.route('/optional')
	def optional(self):
		if hasattr(clsFlask.OAUTH2, 'has_credentials'):
			if clsFlask.OAUTH2.has_credentials():
				return '로그인!'
			else:
				return '로그인 하세여!'


	@staticmethod
	def _SQlite_check():
		pass


