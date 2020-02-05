import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="x",
  passwd="x",
  database="MacDB"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")



