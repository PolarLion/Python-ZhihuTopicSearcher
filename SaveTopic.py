# -*- coding: utf-8 -*- 
#!/usr/bin/python



import urllib2
import bs4
import re
import time
import datetime
import os
from bs4 import BeautifulSoup


def save_topic (topic = "doctor", url = "http://www.zhihu.com/topic/19565943/questions", outdir = "") :
    if not os.path.exists (outdir) :
        os.mkdir (outdir)
    outfilename = os.path.join (outdir, topic)
    outfile = open (outfilename + ".xml", 'w')
    outtext = open (outfilename + ".txt", 'w')
    outtext.write ("number\ttitle\tanswer number\tdate time\turl\n")
    response = urllib2.urlopen (url)  
    html = response.read () 
    soup = BeautifulSoup (html)
    #outfile.write (soup.prettify ().encode ('utf8'))
    #outfile.write (html)
    maxpage = 1
    for link in soup.find_all('a'):
        #print str(link.get ('href'))
        m = re.match (r'.*?page=\d+', str (link.get ('href')))
        if m :
            num = int (re.findall (r'\d+', m.group ())[0])
            if num > maxpage :
                maxpage = num
    #print maxpage
    #maxpage = 1
    count_question = 0
    for i in range (1, maxpage+1) :
        pageurl = "http://www.zhihu.com/topic/19565943/questions?page="+str (i)
        print "\r%s processing page %d of %d" % (topic, i, maxpage), 
        req = urllib2.Request(pageurl)  
        try:  
            response = urllib2.urlopen(req)  
        except urllib2.HTTPError, e:  
            print 'The server couldn\'t fulfill the request.'  
            print 'Error code: ', e.code  
        except urllib2.URLError, e:  
            print 'We failed to reach a server.'  
            print 'Reason: ', e.reason  
        page = response.read ()
        soup = BeautifulSoup (page)
        for title in soup.find_all ('a') :
            #print title
            question_id = title.get ('href')
            if  re.match (r'/question/\d+', str (title.get ('href'))) :
                count_question += 1
                t = "question_" + str (count_question)
                question_url = "http://www.zhihu.com" + question_id
                strtitle = title.string.encode ('utf-8')
                stranswer = title.parent.parent.meta.get('content')
                dt = time.localtime (int (title.parent.span.get('data-timestamp')) / 1000)
                strtime = str (datetime.datetime (dt[0], dt[1], dt[2], dt[3], dt[4], dt[5]))
                outfile.write ("<" + t + ">\n")
                outfile.write ("  <question_title>" + strtitle + "</question_title>\n" )
                outfile.write ("  <question_answer>" + stranswer + "</question_answer>\n")
                outfile.write ("  <question_time>" + strtime  + "/<question_time>\n")
                outfile.write ("  <question_url>" + question_url + "</question_url>\n")
                outfile.write ("</" + t + ">\n")
                outtext.write (str (count_question)+"\t"+strtitle+'\t'+stranswer+'\t'+strtime+'\t'+question_url+'\n') 
    print ""
    outfile.close ()
    outtext.close ()



