import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='electrogs001'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE pexellar")

print("All Done!")
