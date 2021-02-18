from StoreScript.Configuration.Base.cnfclass import cSqlite


def test__cSqlite():
	"""cSqlite test"""
	tmp_cls = cSqlite()
	tmp_container = []

	tmp_container.append(tmp_cls._choose_op('db_store', ('create', 'table')))
	tmp_container.append(tmp_cls._choose_op('db_store', ('destory', 'table')))
	tmp_container.append(tmp_cls._choose_op('db_store', ('add', 'table')))
	tmp_container.append(tmp_cls._choose_op('db_store', ('check', 'table'), queryLi=['dummy1', 'dummy2']))

	tmp_container.append(tmp_cls._choose_op('db_auth', ('create', 'table')))
	tmp_container.append(tmp_cls._choose_op('db_auth', ('destory', 'table')))
	tmp_container.append(tmp_cls._choose_op('db_auth', ('add', 'table')))
	tmp_container.append(tmp_cls._choose_op('db_auth', ('check', 'table'), queryLi=['dummy1', 'dummy2']))

	print('')
	for n, res in enumerate(tmp_container):

		if n  %  4 == 0:
			print('\n')
		assert res != None
		assert isinstance(res, str)
		print(res)