# -*- coding: utf-8 -*- 
#!/usr/bin/python

import urllib2
import bs4
import re
from bs4 import BeautifulSoup

def search_topic (topic = "") :
    topic_dic = {}
    topic = repr(topic).replace ('\\x', '%').upper ()
    #view-source:http://www.zhihu.com/search?q=%E5%96%B5&type=topic
    url1 = "http://www.zhihu.com/search?type=topic&q=" + topic[1:len (topic)-1]
    print url1
    req = urllib2.Request (url1)
    try :
        response = urllib2.urlopen (req)
    except urllib2.HTTPError, e:
        print 'The server couldn\'t fulfill the request.','Error code: ', e.code
        return topic_dic 
    except urllib2.URLError, e:
        print 'We failed to reach a server.', 'Reason: ', e.reason
        return topic_dic
    #outfile = open ('tmp.txt', 'w')
    html1 = response.read ()
    soup = BeautifulSoup (html1) 
    #outfile.write (soup.prettify ().encode ('utf8'))
    for link in soup.find_all ('a') :
        cl =  link.get ('class')
        if cl and cl[0] == 'name-link':
            topic_url = "http://www.zhihu.com" + str (link.get ('href')) + "/questions"
            topic_dic [link.string] = topic_url
        #m = re.match (r'.*/topic/\d+', liink.get ('href'))
        #if m:
         #   print m.group ()
    #outfile.close ()
    return topic_dic
