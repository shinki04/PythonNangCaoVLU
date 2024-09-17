import mysql
import mysql.connector

import mysql.connector
import GuiDBConfig as guiConf # Này là của file ko phải module bên ngoài

GUIDB = 'GuiDB'

# unpack dictionary credentials
conn = mysql.connector.connect(**guiConf.dbConfig)  
cursor = conn.cursor()
try:
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(GUIDB)) # Tạo table tên GuiDB vs set utf-8
except mysql.connector.Error as err:  
    print("Failed to create DB: {}".format(err))

conn.close()
