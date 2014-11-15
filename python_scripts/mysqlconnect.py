from datetime import date, datetime, timedelta
import mysql.connector
import csv

config = {
	'user': 'b3797a47b0872a',
	'password': 'aa6b40d9',
	'host': 'us-cdbr-iron-east-01.cleardb.net',
	'database': 'heroku_37b8a7deeb74751'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)
a = []

with open('time.csv', mode='r') as infile:
    reader = csv.reader(infile)
    reader.next()
    for row in reader:
    	a.append(tuple(row))

stmt = "INSERT INTO time (word) VALUES (%s)"

try:
	cursor.executemany(stmt, a)
	cnx.commit()
except:
	print("Something went wrong")
	cnx.rollback()
	cursor.close()
	cnx.close()

cursor.close()
cnx.close()	