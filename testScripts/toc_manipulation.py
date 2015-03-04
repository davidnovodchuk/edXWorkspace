import json
from six import iteritems

toc = [{'active': True, 'sections': [{'url_name': u'edx_introduction', 'display_name': u'Demo Course Overview', 'graded': False, 'format': '', 'due': None, 'active': False}], 'url_name': u'd8a6192ade314473a78242dfeedfbf5b', 'display_name': u'Introduction'}, {'active': False, 'sections': [{'url_name': u'19a30717eff543078a5d94ae9d6c18a5', 'display_name': u'Lesson 1 - Getting Started', 'graded': False, 'format': '', 'due': None, 'active': False}, {'url_name': u'basic_questions', 'display_name': u'Homework - Question Styles', 'graded': True, 'format': u'Homework', 'due': None, 'active': False}], 'url_name': u'interactive_demonstrations', 'display_name': u'Example Week 1: Getting Started'}, {'active': False, 'sections': [{'url_name': u'simulations', 'display_name': u"Lesson 2 - Let's Get Interactive!", 'graded': False, 'format': '', 'due': None, 'active': False}, {'url_name': u'graded_simulations', 'display_name': u'Homework - Labs and Demos', 'graded': True, 'format': u'Homework', 'due': None, 'active': False}, {'url_name': u'175e76c4951144a29d46211361266e0e', 'display_name': u'Homework - Essays', 'graded': False, 'format': '', 'due': None, 'active': False}], 'url_name': u'graded_interactions', 'display_name': u'Example Week 2: Get Interactive'}, {'active': False, 'sections': [{'url_name': u'48ecb924d7fe4b66a230137626bfa93e', 'display_name': u'Lesson 3 - Be Social', 'graded': False, 'format': '', 'due': None, 'active': False}, {'url_name': u'dbe8fc027bcb4fe9afb744d2e8415855', 'display_name': u'Homework - Find Your Study Buddy', 'graded': False, 'format': '', 'due': None, 'active': False}, {'url_name': u'6ab9c442501d472c8ed200e367b4edfa', 'display_name': u'More Ways to Connect', 'graded': False, 'format': '', 'due': None, 'active': False}], 'url_name': u'social_integration', 'display_name': u'Example Week 3: Be Social'}, {'active': False, 'sections': [{'url_name': u'workflow', 'display_name': u'edX Exams', 'graded': True, 'format': u'Exam', 'due': None, 'active': False}], 'url_name': u'1414ffd5143b4b508f739b563ab468b7', 'display_name': u'About Exams and Certificates'}]

'''
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
'''
jdata = json.dumps(toc)

for item in toc:	
	for key, value in item.iteritems():
		if key == ''
