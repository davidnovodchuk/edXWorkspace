import csv
import MySQLdb as mdb

emailsNotToRemove = []

with open('emails_no_remove.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        emailsNotToRemove.append(row[0])

f.close()

# connecting to the database:
con = mdb.connect( user = "root", db = "edxapp", passwd = "dnedx14");

emailsFromDatabase = []
# Executing MySQL queries:
with con:

	cur = con.cursor()

	cur.execute(""" SELECT email 
                    FROM auth_user """)

	# getting student_id from the query result:
	rows = cur.fetchall()

	for row in rows:
		emailsFromDatabase.append(row[0])

# Closing the db connection:        
con.close()

emailsToRemove = []

for emailDB in emailsFromDatabase:

	toRemove = True
	for emailCSV in emailsNotToRemove:
		if emailDB == emailCSV:
			toRemove = False

	if toRemove == True:
		emailsToRemove.append(emailDB)

for emailToRemove in emailsToRemove:
	print emailToRemove
