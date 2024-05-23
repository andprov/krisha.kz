import sqlite3


class DBConnection:
    def __init__(self, db_path: str):
        self._db_path = db_path
        self._connection = None

    def __enter__(self):
        self._connection = sqlite3.connect(self._db_path)
        return self._connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self._connection:
            self._connection.close()
