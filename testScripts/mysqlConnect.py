import MySQLdb

conn = MySQLdb.connect (host = "localhost", 
	user = "root", 
 	passwd = "dnedx14", 
 	db = "edxapp")

cursor = conn.cursor ()

# execute SQL select statement
cursor.execute("SELECT * FROM student_courseenrollment")

# commit your changes
conn.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

# get and display one row at a time.
for x in range(0,numrows):
    row = cursor.fetchone()
    print row[0], "-->", row[1], "-->", row[2], "-->", row[2], "-->", row[4]

""" cursor.execute ("select cnum, cname from course where credits = 3")
row = cursor.fetchone ()

while row != None:
	print "Course Number:", row[0], "\tCourse Names", row[1]
	row = cursor.fetchone ()
"""

cursor.close ()
conn.close ()
