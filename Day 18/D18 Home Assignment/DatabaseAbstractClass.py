'''8.	Create an abstract class Database:
o	Abstract methods:
	connect()
	disconnect()
	execute_query(query)
o	Create concrete classes:
	MySQLDatabase
	PostgreSQLDatabase
	SQLiteDatabase'''
from abc import ABC,abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):  
        pass
    @abstractmethod
    def disconnect(self):
        pass
    @abstractmethod
    def execute_query(self, query):
        pass
class MySQLDatabase(Database):
    def connect(self):
        print("MySQLDatabase is Connected.")
    def disconnect(self):
        print("MySQLDatabase is Disconnected.")
    def execute_query(self, query):
        print(f"Query is going to be executed : {query}")
class PostgreSQLDatabase(Database):
    def connect(self):
        print("PostgreSQLDatabase is Connected.")
    def disconnect(self):
        print("PostgreSQLDatabase is Disconnected.")
    def execute_query(self, query):
        print(f"Query is going to be executed : {query}")
class SQLiteDatabase(Database):
    def connect(self):
        print("SQLiteDatabase is Connected.")
    def disconnect(self):
        print("SQLiteDatabase is Disconnected.")
    def execute_query(self, query):
        print(f"Query is going to be executed : {query}")

mysql_db = MySQLDatabase()
mysql_db.connect()
mysql_db.execute_query("SELECT * FROM users")
mysql_db.disconnect()

postgres_db = PostgreSQLDatabase()
postgres_db.connect()
postgres_db.execute_query("SELECT * FROM customers")
postgres_db.disconnect()

sqlite_db = SQLiteDatabase()
sqlite_db.connect()
sqlite_db.execute_query("SELECT * FROM products")
sqlite_db.disconnect()
