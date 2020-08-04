import sqlite3


class DataBases():
    def __init__(self,db_name):
        self.db = sqlite3.connect(db_name)
        self.cur = self.db.cursor()


    def get_name(self):
        with self.db:
            return self.cur.execute('SELECT *  FROM author').fetchall()
    def set_name(self,name,year):
        with self.db:
            return self.cur.execute('INSERT INTO author VALUES(?,?)',(name,year))



db = DataBases('db.db')
db.set_name('Слава',2003)
names = db.get_name()
print(names)
