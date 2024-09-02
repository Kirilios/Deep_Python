import sqlite3

# connection = sqlite3.connect('sqlite.db')
# cursor = connection.cursor()
# cursor.execute("""create table if not exists Users(name, age);""")
# cursor.execute("""insert into Users values ('Something', 66);""")
# connection.commit()
# connection.close()

class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None

db = DB('sqlite1.db')
with db as cur:
    cur.execute("""create table if not exists Users(name, age);""")
    cur.execute("""insert into Users values ('Something', 66);""")


