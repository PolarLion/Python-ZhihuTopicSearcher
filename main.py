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
import subprocess

class Display :
    def __init__ (self, e) :
        self.e = e

    def write (self, string) :
        if string.find ('\r') >= 0  and len (string) > 0:
            self.e.delete (1.0, Tkinter.END)
        self.e.insert (Tkinter.INSERT, string)
        self.e.see (Tkinter.END)

def funn (topic, followers, questions, outpath, logger, text) :
    sys.stdout = Display (text)
    topic_dic = SearchTopic.search_topic (topic = topic, followers = followers, questions = questions)
    if len (topic_dic) == 0 :
        return False
    if not os.path.exists (outpath) :
        os.mkdir (outpath)
    for key in topic_dic :
	apath = os.path.join (outpath, topic)
        SaveTopic.save_topic (topic = key, url = topic_dic[key].url, outdir = apath, log = logger)
    thread.exit ()


if __name__ == "__main__" :
    reload(sys)
    sys.setdefaultencoding("utf-8")
    #tmp_file = open (os.path.join (os.getcwd (), 'tmp.txt'), 'wb')
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
        e_topic = e1.get ().encode ('utf-8')
        tk = Tkinter.Tk ()
        text = Tkinter.Text (tk, width = 40)
        text.pack ()
        thread.start_new_thread (funn, (e_topic, int (e4.get ()), int (e3.get ()), e2.get ().encode ('utf-8'), logger, text))
        tk.mainloop ()
        tk.destroy ()
    Tkinter.Button (master, height = 3, width = 20, text=" search ", command=fun).pack ()
    master.mainloop() 


