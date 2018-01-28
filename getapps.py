#!/usr/bin/env python
#-*- coding: utf-8 -*-
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup as bsoup
import requests
br = mechanize.Browser()

# cookie jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Firefox/12.0')]

url = "https://play.google.com/store/apps/category/ART_AND_DESIGN/collection/topselling_free"

html = requests.get(url).text
soup = bsoup(html)

urlslist = soup.findAll("a", { "class" : "card-click-target" })
urls = []
#open the file to keep the list, as required
fo = open('url.txt', 'w')

#Url list
for a in urlslist:
    link = "https://play.google.com" + a['href']
    #print(link)
    urls.append(link)
url = urls[::4]
for item in url:
    item = item[46:] #list as package name
    #fo.write(''.join('"'+item+'"'+'\n'))
    fo.write("%s\n" % item)

fo.close()
