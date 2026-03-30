import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="ajayvehiclerental"
)

cursor = conn.cursor()