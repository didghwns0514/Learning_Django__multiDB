"""
    주문 / DB 기본값 관리
    ~~~~~~~~~~~~~~~~~~~
"""
from enum import Enum



class DBcnf:
    """
    DB 기본값 선언 부분
    """
    maxCharLen = int(200)
    orderNumber = int(1)
    orderStateIndex = int(1)
    robotStateIndex = int(1)
    
class cSqlite: # Enum
    """
    sqlite 관련 부분
    참조:
        >>> http://hleecaster.com/python-sqlite3/

    """
    table_create = "CREATE TABLE IF NOT EXISTS " #tbl name
    table_destroy = "DROP TABLE IF EXISTS " #tbl name
    table_search = "SELECT * FROM "
    table_add = "INSERT INTO "

    table_auth_col = "(id integer PRIMARY KEY, username VARCHAR UNIQUE, hashed_password VARCHAR, email text)"
    table_store_col = "(storekey VARCHAR UNIQUE,  )"
    auth_col_dict = {
                        1:"(username, hashed_password, email)",
                        2:"(?, ?, ?)"
                    }
    store_col_dict = {
                         1:"(storekey)",
                         2:"(?,)"
                    }

    table_auth_name = "auth"
    table_store_name = "order"

    isolation_lv = 0 # commit 없이 바로 반영(자동 commit)


    @staticmethod
    def _choose_op(_type:str, action:tuple, uniqkey:str=None, queryLi:list=None)->str:
        """
        choosing operation in _Sqlite
        :param _type: type of db using
        :param action: action in tuple
        :param uniqkey: key used to identify the store
        :param queryLi: list of items to search as query
        :return: string type of sql query
        """
        # local values used
        table_name, table_col, column_dict = None, None, None

        if _type == 'db_auth':
            table_name = cSqlite.table_auth_name
            table_col = cSqlite.table_auth_col
            column_dict = cSqlite.auth_col_dict

        elif _type == 'db_store':
            #assert uniqkey != None
            table_name = cSqlite.table_store_name
            table_col = cSqlite.table_store_col
            column_dict = cSqlite.table_store_name

        else:
            raise ValueError('wrong db type chosen')

        if action == ('create', 'table'):
            return cSqlite.table_create + table_name + table_col

        elif action == ('destory', 'table'):
            return cSqlite.table_destroy + table_name

        elif action == ('add', 'table'):
            return cSqlite.table_add + table_name + ' ' + column_dict[1] + ' ' + \
                    'VALUES' + ' ' + column_dict[2]

        elif action == ('check', 'table'):
            assert queryLi != None
            conv = ' AND '.join(list(map(lambda x: x + ' = ?' ,queryLi)))
            return cSqlite.table_search + table_name + ' ' + 'WHERE' + ' ' + conv

        else:
            raise ValueError('wrong action input')



class cFlask:
    """
    flask 로그인 체크 여부
    """
    Option = False