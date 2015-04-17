import json
import urllib, urllib2

from keys import BING_API_KEY

def run_query(search_terms):
	
	# Prepares for connecting to Bing by preparing the URL that we will be requesting.

	root_url = 'https://api.datamarket.azure.com/Bing/Search/'
	source = 'Web'
	results_per_page = 10
	offset = 0

	query = "'{0}'".format(search_terms)
	query = urllib.quote(query)

	search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
		root_url,
		source,
		results_per_page,
		offset,
		query)

	# Prepares authentication

	username = ''
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None, search_url, username, BING_API_KEY)

	results = []

	# Connect to the Bing API 

	try:
		handler = urllib2.HTTPBasicAuthHandler(password_mgr)
		opener = urllib2.build_opener(handler)
		urllib2.install_opener(opener)

		# The results from the server are read and saved as a string.
		response = urllib2.urlopen(search_url).read()

		# The string is then parsed into a Python dictionary object.
		json_response = json.loads(response)
		print json_response

		# We loop through each of the returned results, populating a results dictionary. 
		for result in json_response['d']['results']:
			results.append({
				'title': result['Title'],
				'link': result['Url'],
				'summary': result['Description']})
	
	except urllib2.URLError, e:
		print "Error when querying bing API: ", e

	return results