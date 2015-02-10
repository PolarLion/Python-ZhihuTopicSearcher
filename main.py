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
    master = Tkinter.Tk()  #创建主窗体
    e = Tkinter.Entry (master, textvariable = Tkinter.StringVar())
    e.pack()

    topic = ""
    def fun () :
        topic = e.get ().encode ('utf-8')
        topic_dic = SearchTopic.search_topic (topic)
        if len (topic_dic) == 0 :
            tkMessageBox.showwarning("search", "found no topic")
        for key in topic_dic :
            SaveTopic.save_topic (key, topic_dic[key], "io/")
    print topic
    Tkinter.Button (master, text="search", command=fun).pack ()
    master.mainloop() 



