from dJango_conf.h__CONF import _APP_SET, _APP_SET_READWRITE, _APP_SET_WRITEONLY

class MultiDBRouter(object):
	"""
	A router to control all database operations on models in the
	auth and contenttypes applications.
	"""
	route_app_labels = _APP_SET
	route_app_label_readwrite = _APP_SET_READWRITE # storeapp
	route_app_label_writeonly = _APP_SET_WRITEONLY # collectapp

	def db_for_read(self, model, **hints):
		"""
		Attempts to read auth and contenttypes models go to auth_db.
		"""
		if model._meta.app_label in self.route_app_label_readwrite:
			return 'db_store'
		return None

	def db_for_write(self, model, **hints):
		"""
		Attempts to write auth and contenttypes models go to auth_db.
		"""
		if model._meta.app_label in self.route_app_labels:
			if model._meta.app_label in self.route_app_label_writeonly:
				return 'db_collect'
			elif model._meta.app_label in self.route_app_label_readwrite:
				return 'db_store'
		return None

	def allow_relation(self, obj1, obj2, **hints):
		"""
		Allow relations if a model in the auth or contenttypes apps is
		involved.
		"""
		if (
				obj1._meta.app_label in self.route_app_labels or
				obj2._meta.app_label in self.route_app_labels
		):
			return True
		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		"""
		Make sure the auth and contenttypes apps only appear in the
		'auth_db' database.
		"""
		# print(f'app_label : {app_label}')
		# print(f'db : {db}')

		# if app_label in self.route_app_labels:
		# 	# if app_label in self.route_app_label_readwrite:
		# 	# 	return db == 'db_store'
		# 	# elif db == 'default': # db diction 1 lv key 명칭인듯
		# 	# 	return True
		#
		# 	if app_label in self.route_app_label_writeonly:
		# 		return db == 'db_collect'
		#
		# 	elif app_label in self.route_app_label_readwrite:
		# 		return db == 'db_store'
		#
		# 	elif db == 'default' or db == 'db_store': # db diction 1 lv key 명칭인듯
		# 		return True
		# return None


		# if app_label in self.route_app_label_writeonly:
		# 	return False
		# return True
		if app_label in self.route_app_labels:
			if app_label in self.route_app_label_readwrite:
				return db == 'db_store'
		else: # default db
			if db == 'default':
				return True

		return None