# -*- coding: utf-8 -*- 
#!/usr/bin/pyton
#main.py

import SaveTopic
import SearchTopic
import sys
import Tkinter
import tkMessageBox
import os
import thread
import logging

if __name__ == "__main__" :
    reload(sys)
    sys.setdefaultencoding("utf-8")
    logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.INFO, filemode = 'w', format = '%(asctime)s - %(levelname)s: %(message)s') 
    logger = logging.getLogger('root.test')  
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
            return
        def funn () :
            if not os.path.exists (e2.get ().encode ('utf-8')) :
                os.mkdir (e2.get ().encode ('utf-8'))
            for key in topic_dic :
	        apath = os.path.join (e2.get (), e1.get ())
                SaveTopic.save_topic (key, topic_dic[key].url, apath)
            thread.exit ()
        #Tkinter.Entry (tk, width = 20, text = e1.get (), validate = "focusout", validatecommand = funn).pack ()
        tk = Tkinter.Tk ()
        thread.start_new (funn, ())
        tk.mainloop ()
        tk.destroy ()
    Tkinter.Button (master, height = 3, width = 20, text=" search ", command=fun).pack ()
    master.mainloop() 


