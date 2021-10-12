import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class HuoShuSql(object):
	"""docstring for HuoShuSql"""
	def __init__(self, db_info):
		super(HuoShuSql, self).__init__()
		self.db_info = db_info
		self._conn = self._connect()
		self._cursor = self._conn.cursor()

	'''
	some methods for opening, executing and closing the postgresql
	'''
	def _connect(self):
		return psycopg2.connect(
			database = self.db_info['db'],
			user = self.db_info['user'],
			password = self.db_info['pwd'],
			host = self.db_info['host'],
			port = self.db_info['port'])

	def common(self, sqlCode):
		try:
			self._cursor.execute(sqlCode)
		except Exception as e:
			print(e)
			self._conn.rollback()
			self._cursor.execute(sqlCode)
		self._conn.commit()	

	def close(self):
		self._cursor.close()
		self._conn.close()
		
	def __del__(self):
		self.close()


'''
	implement the transformation between DataFrame and Sql so that we can process and feed the machine learning or operational reasearch models easily with pandas and numpy
'''

class DataFrameToSql(HuoShuSql):
	"""docstring for DataFrameToSql"""
	def __init__(self, db_info):
		super(DataFrameToSql, self).__init__(db_info)
			


class SqlToDataFrame(HuoShuSql):
	"""docstring for SqlToDataFrame"""
	def __init__(self, db_info):
		super(SqlToDataFrame, self).__init__(db_info)

	def fit(self, sqlCode):		
		result = self.select(sqlCode)
		return pd.DataFrame(list(result.get('data')),columns=result.get('head'))

	def select(self, sqlCode):
		self.common(sqlCode)
		col_names = []
		result = {}
		column_count = len(self._cursor.description)
		for i in range(column_count):
			desc = self._cursor.description[i]
			col_names.append(desc[0])
		data = self._cursor.fetchall()
		result['head'] = col_names
		result['data'] = data
		return result		

