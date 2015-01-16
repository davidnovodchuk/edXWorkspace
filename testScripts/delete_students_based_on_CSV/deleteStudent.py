#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
from six import iteritems

# connecting to the database:
con = mdb.connect( user = "root", db = "edxapp", passwd = "dnedx14");

# Executing MySQL queries:
with con:

	email = 'dnovodchuk@myseneca.ca'

	cur = con.cursor()

	cur.execute(""" SELECT id 
                    FROM auth_user
					WHERE email = %s """, [email])

	# getting student_id from the query result:
	student_id = int(cur.fetchall()[0][0])
	
	# deleting rows from all tables where there are foreign keys of student_id
	
	# auth_registration table:
	cur.execute(""" DELETE FROM auth_registration 
			WHERE user_id = %s """, [student_id])

	# auth_userprofile table:
	cur.execute(""" DELETE FROM auth_userprofile 
			WHERE user_id = %s """, [student_id])

	# courseware_studentmodule table:
	cur.execute(""" DELETE FROM courseware_studentmodule 
			WHERE student_id = %s """, [student_id])

	# django_comment_client_role_users table:
	cur.execute(""" DELETE FROM django_comment_client_role_users 
			WHERE user_id = %s """, [student_id])

	# student_courseenrollment table:
	cur.execute(""" DELETE FROM student_courseenrollment 
			WHERE user_id = %s """, [student_id])

	# user_api_userpreference table:
	cur.execute(""" DELETE FROM user_api_userpreference 
			WHERE user_id = %s """, [student_id])

	# auth_user table:
	cur.execute(""" DELETE FROM auth_user 
			WHERE id = %s """, [student_id])

	print "User " + email + " was successfully removed"

# Closing the db connection:        
con.close()