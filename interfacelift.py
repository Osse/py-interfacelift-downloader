#!/usr/bin/env python
# encoding: utf-8

import sys
from urllib2 import urlopen, Request
from re      import findall
from time    import sleep
from os.path import expanduser, isfile

useragent     = 'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
directory     = expanduser('~')+'/Pictures/Interfacelift-citylights'
interfacelift = 'http://interfacelift.com/wallpaper/'
urlspec       = 'tags/1426/scene/city_lights/'
resolution    = '1920x1080'
pattern       = '(?<=previews/)\d{5}_\w+\.jpg'
indices       = 3

def determineRandomPart():
    print "Attempting to determine random part of the URLs"
    data = urlopen(interfacelift + "downloads/date/hdtv/1080p/index1.html").read()
    temp = findall('(?<=<a href="/wallpaper/)([^/]+)(?=/.*1920x1080\.jpg">)', data)
    if len(temp) == 10 and temp.count(temp[0]) == 10:
        print "Random part is", temp[0]
        return temp[0]+'/'
    else:
        print "Couldn't determine the random part"
        exit()

def findPicURLs(random):
    pictures = []
    for count in range(1, indices + 1):
        data = urlopen(interfacelift + urlspec + "index" + str(count) + ".html").read()
        print "Searching index", str(count), "of", str(indices)
        temp = findall(pattern, data)
        pictures += [interfacelift + random + i[:-4]+ '_' + resolution + i[-4:] for i in temp]
    return pictures

def downloadPictures(pictures):
    if len(pictures) > 0:
        print "Attempting to download", len(pictures), "files..."
        for pic in pictures:
            if downloadPicture(pic): sleep(5)
        print "Complete."
    else:
        print "No pictures to download."

def downloadPicture(pic):
    reqobj = Request(pic, useragent)
    filename = directory + '/' + pic.rpartition('/')[2]
    if not isfile(filename):
        print "Downloading", pic.rpartition('/')[2]+"... ",
        sys.stdout.flush()
        f = open(filename, "w")
        data = urlopen(reqobj).read()
        f.write(data)
        f.close()
        print "Done."
        return True
    else: 
        print "Hadde bildet fra før"
    return False

print "Hello"
random = determineRandomPart()
pictures = findPicURLs(random)
downloadPictures(pictures)
print "Good bye"
                
# vim:sw=4:et:sts=4
