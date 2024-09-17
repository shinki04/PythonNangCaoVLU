import mysql
import mysql.connector

import mysql.connector
import GuiDBConfig as guiConf # Này là của file ko phải module bên ngoài

conn = mysql.connector.connect(**guiConf.dbConfig)

cursor = conn.cursor()


cursor.execute("SHOW DATABASES")  
# fetchall kiểu lấy theo hàng , all là hết , many thì nhập size vào 
print(cursor.fetchall())
    
# Này phải là table cụ thể
# print(cursor.fetchmany(size=4))
conn.close()
