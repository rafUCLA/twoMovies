#! /usr/bin/env python3

#from tinydb import TinyDB, Query
import json
import webhoseio

webhoseio.config(token='11a5bf53-12f6-440d-a84f-e42c18c7c38d')
output = webhoseio.query("filterWebContent", 
	{"q": "Global Warming",
	"sort": "relevancy"})
print ("URL: " + output['posts'][0]['url']) # Print the text of the first post
print ("title: " + output['posts'][0]['title']) # Print the text of the first post
print ("published: " + output['posts'][0]['published']) # Print the text of the first post publication date

output = webhoseio.get_next()
print ("URL: " + output['posts'][0]['url']) # Print the text of the first post
print ("title: " + output['posts'][0]['title']) # Print the text of the first post
print ("published: " + output['posts'][0]['published']) # Print the text of the first post publication date

# try:
# 	response = urlopen(request)
# 	data = response.read()
# 	parsed_json = json.loads(data)
# except URLError, e:
#    print 'API call not working. Got an error code:', e
# else:
# 	print parsed_json[0]