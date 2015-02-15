# -*- coding: utf-8 -*- 
#!/usr/bin/python

import urllib2
#import bs4
#import re
from bs4 import BeautifulSoup

class ZhihuTopic :
    name = ""
    followers= 0
    questions = 0
    url = ""
    def __init__ (self, name="", followers=0, questions=0, url="") :
        self.name = name
        self.followers = followers
        self.questions = questions
        self.url = url

    def __repr__ (self) :
        return self.name


def search_topic (topic = "", followers = 0, questions = 0) :
    topic_dic = {}
    t_topic = repr (topic).replace ('\\x', '%').upper ()
    #view-source:http://www.zhihu.com/search?q=%E5%96%B5&type=topic
    url1 = "http://www.zhihu.com/search?type=topic&q=" + t_topic[1:len (t_topic)-1]
    print "visiting page ", url1
    req = urllib2.Request (url1)
    try :
        response = urllib2.urlopen (req)
    except urllib2.HTTPError, e:
        print 'The server couldn\'t fulfill the request.','Error code: ', e.code
        return topic_dic 
    except urllib2.URLError, e:
        print 'We failed to reach a server.', 'Reason: ', e.reason
        return topic_dic
    outfile = open ('tmp.txt', 'w')
    html1 = response.read ()
    soup = BeautifulSoup (html1) 
    #outfile.write (soup.prettify ().encode ('utf8'))
    topic = ZhihuTopic ()
    for link in soup.find_all ('a') :
        cl =  link.get ('class')
        if cl and cl[0] == 'name-link':
            topic.url = "http://www.zhihu.com" + str (link.get ('href')) + "/questions"
            topic.name = link.string
        if cl and cl[0] == "questions":
            topic.questions = int (link.get_text ().split (' ')[0])
        if cl and cl[0] == "followers" :
            topic.followers = int (link.get_text ().split (' ')[0])
            if topic.followers > followers and topic.questions > questions :
                topic_dic [topic.name] = topic
                print topic_dic [topic.name]
            topic = ZhihuTopic ()
    outfile.close ()
    return topic_dic
