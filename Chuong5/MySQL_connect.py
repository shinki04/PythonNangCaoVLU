import mysql
import mysql.connector
conn = mysql.connector.connect(user = "root", password = "123456", host = "127.0.0.1")
print(conn)
conn.close()
