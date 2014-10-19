from datetime import date, datetime, timedelta
import mysql.connector
import csv

config = {
	'user': 'bdddb6df4683a5',
	'password': 'fe4a4628',
	'host': 'us-cdbr-azure-central-a.cloudapp.net',
	'database': 'ni42mysql'
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