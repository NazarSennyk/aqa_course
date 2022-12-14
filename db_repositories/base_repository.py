import psycopg2


class BaseRepo:
    def __init__(self):
        self._connection = psycopg2.connection(user='postgres', password='123', host='127.0.0.1', port='5432',
                                                database='mydb')
        self._cursor = self._connection.cursor()
        self._connection.set_session(autocommit=True)
        self._cursor = self._connection.cursor()
        self.table_name = ''

    def get_all(self):
        self._cursor.execute(f"select * from '{self.table_name}';")
        return self._cursor.fetchall()

    def __del__(self):
        if self._connection:
            if self._cursor:
                self._cursor.close()
            self._connection.close()