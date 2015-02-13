# -*- coding: utf-8 -*- 
#!/usr/bin/pyton
#main.py

import SaveTopic
import SearchTopic
import sys
import Tkinter
import tkMessageBox



if __name__ == "__main__" :
    reload(sys)
    sys.setdefaultencoding("utf-8")
    #SaveTopic.save_topic (
    master = Tkinter.Tk ()  #创建主窗体
    Tkinter.Label(master, text = "topic").pack()
    e1 = Tkinter.Entry (master, width = 30, textvariable = Tkinter.StringVar())
    e1.pack ()
    Tkinter.Label(master, text = "output dir").pack()
    e2 = Tkinter.Entry (master, width = 30, textvariable = Tkinter.StringVar())
    e2.pack ()
    e2.insert (0, "io")
    topic = ""
    def fun () :
        topic = e1.get ().encode ('utf-8')
        topic_dic = SearchTopic.search_topic (topic)

        if len (topic_dic) == 0 :
            tkMessageBox.showwarning("search", "found no topic")
        for key in topic_dic :
            print key
            SaveTopic.save_topic (key, topic_dic[key].url, e2.get ().encode ('utf-8'))
            print "finish topic %s" % key
    Tkinter.Button (master, width = 20, text=" search ", command=fun).pack ()
    master.mainloop() 



