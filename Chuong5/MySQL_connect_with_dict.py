import mysql
import mysql.connector


# create dictionary to hold connection info
dbConfig = {
    'user': "root",  # use your admin name

    'password': "123456",  # use your real password

    'host': '127.0.0.1',  # IP address of localhost

}

# unpack dictionary credentials
conn = mysql.connector.connect(**dbConfig)
print(conn)
