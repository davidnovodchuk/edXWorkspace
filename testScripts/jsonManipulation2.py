import json
from six import iteritems

jsonString = '{"name":"David","course":"Programming with JAVA","position":2,"answers":{"write a line of code that outputs Hello World!":"System.out.print(Hello World!);","what extention do you need to add to a file in order to specify that the file contains java source code?":".java"}}'

jdata = json.loads(jsonString)
"""
for item in jdata:
	print str(item)

"""
for key, value in jdata.iteritems():
	if key == 'answers':
		print (key + ": ")
		for k, v in value.iteritems():
			print ("  " + k)			
			print ("    " + str(v))
	else:
		print (key + ": " + str(value))
