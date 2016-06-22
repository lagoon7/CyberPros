# Author: Nimish Doshi
# This program reads RSS feed entries from a file and sends its content to
# stdout. It uses feedparser from http://www.feedparser.org/

import feedparser
import sys
import time
import datetime
import calendar

currentday = datetime.datetime.now().strftime('%Y%m%d-%H%M')

f = open(sys.argv[1], 'r')
for line in f:
    if line[0] != '#':
        item = feedparser.parse(line)
        try:
            print "#####"
            feedstring =  "Feed title ->" + item.feed.title + " >> Number of feeds = " + str(len(item.entries))
            print feedstring
            print "#####"
        except:
            print "ERROR"
        
        for i in item.entries:
            try:
                print  currentday + " " + "feedDate=" + i.updated + " " + "title=" + "\"" + i.title + "\""
                print "link=" + i.link
#               print "description=" + "\"" + i.description + "\""
#            _feeddate = i.updated
#             _feedTitle = i.title
#            _feedLink = i.link
            except AttributeError:
                i.title = "NULL"
#            print i.title
        print "###########\n\n"        
f.close()


