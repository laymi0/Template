import sqlite3 as sql

class dbwork:
    
    def __init__(self, database) -> None:
        self.conn = sql.connect(database)
        self.cur = self.conn.cursor()