import mysql.connector
from mysql.connector import Error

class MySQL:
    # Class constructor to store database credentials
    def __init__(self, user, password, host):
        self.user = user
        self.password = password
        self.host = host

    # Connect to MySQL
    def connect(self, database=None):
        try:
            # Connect using stored credentials
            conn = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=database  # Optional, for operations within a specific DB
            )
            if conn.is_connected():
                print("Connected to MySQL")
                # Create cursor
                cursor = conn.cursor()
                return conn, cursor
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None, None

    # Close connection and cursor
    def close(self, cursor, conn):
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("MySQL connection closed")

    # Show databases
    def showDBs(self):
        conn, cursor = self.connect()
        if conn is None or cursor is None:
            return

        try:
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            for db in databases:
                print(db)
        except Error as e:
            print(f"Error while showing databases: {e}")
        finally:
            self.close(cursor, conn)

    # Create a new database
    def createDB(self, dbname):
        conn, cursor = self.connect()
        if conn is None or cursor is None:
            return

        try:
            cursor.execute(f"CREATE DATABASE {dbname} DEFAULT CHARACTER SET 'utf8'")
            print(f"Database '{dbname}' created successfully")
        except Error as e:
            print(f"Failed to create DB '{dbname}': {e}")
        finally:
            self.close(cursor, conn)

    # Delete a database
    def deleteDB(self, dbname):
        conn, cursor = self.connect()
        if conn is None or cursor is None:
            return

        try:
            cursor.execute(f"DROP DATABASE {dbname}")
            print(f"Database '{dbname}' deleted successfully")
        except Error as e:
            print(f"Failed to delete DB '{dbname}': {e}")
        finally:
            self.close(cursor, conn)

    # Show tables in a specific database
    def showTables(self, dbname):
        conn, cursor = self.connect(database=dbname)
        if conn is None or cursor is None:
            return

        try:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for table in tables:
                print(table)
        except Error as e:
            print(f"Error while showing tables: {e}")
        finally:
            self.close(cursor, conn)

    # Create a new table
    def createTable(self, dbname, table_name, schema):
        conn, cursor = self.connect(database=dbname)
        if conn is None or cursor is None:
            return

        try:
            cursor.execute(f"CREATE TABLE {table_name} ({schema})")
            print(f"Table '{table_name}' created successfully in database '{dbname}'")
        except Error as e:
            print(f"Failed to create table '{table_name}': {e}")
        finally:
            self.close(cursor, conn)

    # Delete a table
    def deleteTable(self, dbname, table_name):
        conn, cursor = self.connect(database=dbname)
        if conn is None or cursor is None:
            return

        try:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            print(f"Table '{table_name}' deleted successfully")
        except Error as e:
            print(f"Failed to delete table '{table_name}': {e}")
        finally:
            self.close(cursor, conn)

    # Insert data into a table
    def insertData(self, dbname, table_name, columns, values):
        conn, cursor = self.connect(database=dbname)
        if conn is None or cursor is None:
            return

        try:
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            cursor.execute(sql)
            conn.commit()
            print("Data inserted successfully")
        except Error as e:
            print(f"Failed to insert data: {e}")
        finally:
            self.close(cursor, conn)

    # Delete data from a table
    def deleteData(self, dbname, table_name, condition):
        conn, cursor = self.connect(database=dbname)
        if conn is None or cursor is None:
            return

        try:
            sql = f"DELETE FROM {table_name} WHERE {condition}"
            cursor.execute(sql)
            conn.commit()
            print("Data deleted successfully")
        except Error as e:
            print(f"Failed to delete data: {e}")
        finally:
            self.close(cursor, conn)
