# -*- coding: utf-8 -*- 
#!/usr/bin/pyton
#main.py

import SaveTopic
import SearchTopic
import sys
import Tkinter
import tkMessageBox
import os



if __name__ == "__main__" :
    reload(sys)
    sys.setdefaultencoding("utf-8")
    #SaveTopic.save_topic (
    master = Tkinter.Tk ()  #创建主窗体
    Tkinter.Label(master, text = "topic").pack()
    e1 = Tkinter.Entry (master, width = 30, textvariable = Tkinter.StringVar())
    e1.place (relx = 1, x = 10, y = -10)
    e1.pack ()
    Tkinter.Label (master, text = "output dir").pack ()
    e2 = Tkinter.Entry (master, width = 30, textvariable = Tkinter.StringVar())
    e2.pack ()
    e2.insert (0, "io")
    Tkinter.Label (master, text = "topic questions").pack ()
    e3 = Tkinter.Entry (master, width = 30, textvariable = Tkinter.StringVar())
    e3.pack ()
    e3.insert (0, 0)
    Tkinter.Label (master, text = "topic followers").pack ()
    e4 = Tkinter.Entry (master, width = 30, textvariable = Tkinter.StringVar())
    e4.pack ()
    e4.insert (0, 0)
    def fun () :
        topic_dic = SearchTopic.search_topic (topic = e1.get ().encode ('utf-8'), followers = int (e4.get ()), questions = int (e3.get ()))
        if len (topic_dic) == 0 :
            tkMessageBox.showwarning("search", "found no topic")
        for key in topic_dic :
            print key
	    apath = os.path.join (e2.get ().encode ('utf-8'), e1.get ().encode ('utf-8'))
            SaveTopic.save_topic (key, topic_dic[key].url, apath)
            print "finish topic %s" % key
    Tkinter.Button (master, height = 3, width = 20, text=" search ", command=fun).pack ()
    master.mainloop() 



