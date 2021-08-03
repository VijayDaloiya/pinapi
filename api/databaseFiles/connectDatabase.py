import mysql.connector as connector
import pymysql
def DatabaseConnection():
    
  
    # To connect MySQL databas
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "oreo0008",
        db='practice',
        )
      
    cursor = conn.cursor()

    return cursor,conn
