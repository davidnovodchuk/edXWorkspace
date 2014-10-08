import json
from six import iteritems

jsonString = '{"Student Name":"David","list three programming languages":["C++","Java","Python"],"Do you use Python?":true,"2 + 2 = ":4}'

jdata = json.loads(jsonString)

for item in jdata:
	print str(item)


for key, value in jdata.iteritems():
	if isinstance(value, list):
		print (key + ": ")
		for index, item in enumerate(value):
			print ("  " + str(item))
	else:
		print (key + ": " + str(value))
