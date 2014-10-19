import mysql.connector
a = []

config = {
	'user': 'bdddb6df4683a5',
	'password': 'fe4a4628',
	'host': 'us-cdbr-azure-central-a.cloudapp.net',
	'database': 'ni42mysql'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)

query = "SELECT * FROM names WHERE subtype='place'"

try:
	cursor.execute(query)
except:
	print "Such crap, much fail"
	cursor.close()
	cnx.close()
	exit(-1)

for (word) in cursor:
	a.append(word)

print a

cursor.close()
cnx.close()