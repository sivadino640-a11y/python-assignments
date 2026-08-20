class Database:
    def connect(self):
        pass
    def insert(self):
        pass
    def close(self):
        pass
class MySQL(Database):
    def connect(self):
        print("MySQL connected")
    def insert(self):
        print("Data inserted")
    def close(self):
        print("MySQL closed")
class MongoDB(Database):
    def connect(self):
        print("MongoDB connected")
    def insert(self):
        print("Data inserted")
    def close(self):
        print("MongoDB closed")
db = MySQL()
db.connect()
db.insert()
db.close()