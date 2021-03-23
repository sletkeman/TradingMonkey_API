"""
    Define miscellaneous functions to be used across the application
"""

from os import environ
import pyodbc

class MSSQL(object):
    """Wrapper for handling the MSSQL connection"""
    def __init__(self):
        driver = 'ODBC Driver 17 for SQL Server'
        svr = environ['MSSQL_SERVER']
        db = environ['MSSQL_DB']
        uid = environ['MSSQL_UID']
        pwd = environ['MSSQL_PWD']

        self.connection_str = f'DRIVER={driver};SERVER={svr};DATABASE={db};UID={uid};PWD={pwd}'
        self.connection = pyodbc.connect(self.connection_str)

    def __enter__(self):
        return self

    def __exit__(self, exctype, excinst, exctb):
        self.commit()
        self.connection.close()

    def commit(self):
        """executes a commit"""
        return self.execute('commit')

    def cursor(self):
        """gets a cursor"""
        return self.connection.cursor()

    def execute(self, query, params=()):
        '''Executes a query'''
        return self.cursor().execute(query, params)

    def query(self, query, params=()):
        '''Executes a query and returns the results'''
        cursor = self.execute(query, params)
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def query_one(self, query, params=()):
        '''Executes a query and returns a result'''
        cursor = self.execute(query, params)
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, cursor.fetchone()))

    def get_connection(self):
        '''returns the connection object'''
        return self.connection
