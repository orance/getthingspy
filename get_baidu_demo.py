import urllib2
request = urllib2.Request("https://readhub.me")
response = urllib2.urlopen(request)
print response.read()
