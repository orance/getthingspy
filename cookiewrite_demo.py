import urllib2
import cookielib
filename  = 'cookie.txt'
cookie  = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
url = 'https://www.v2ex.com'
response = opener.open(url)
for item in cookie:
    print 'Name = ' +item.name
    print 'Value = ' +item.value
cookie.save(ignore_discard=True,ignore_expires=True)
