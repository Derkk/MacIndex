import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="goby",
  passwd="goby13"
)

mycursor = mydb.cursor()



