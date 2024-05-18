import mysql.connector
from mysql.connector import errorcode

def fconnect_db():
    print("conect db")
    config = {
        'user': 'root',
        'password': '1234',
        'host': '127.0.0.1',
        'database': 'hard_drive_heath_predict',
    }
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        return cnx, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None, None

def close_connection(cnx, cursor):
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()
    print("Connection closed.")