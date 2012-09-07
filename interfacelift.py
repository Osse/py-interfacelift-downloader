#!/usr/bin/env python
# encoding: utf-8

import sys
from urllib2 import urlopen, Request, HTTPError
from re      import findall
from time    import sleep
from os.path import expanduser, isfile, isdir

useragent     = 'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
directory     = expanduser('~')+'/Pictures/Interfacelift-test'
interfacelift = 'http://interfacelift.com/wallpaper/'
urlspec       = 'tags/1426/scene/city_lights/'
resolution    = '640x480'
pattern       = '(?<=previews/)\d{5}_\w+\.jpg'
indices       = 1

def determineRandomPart():
    print "Attempting to determine random part of the URLs",
    sys.stdout.flush()
    data = urlopen(interfacelift + "downloads/date/hdtv/1080p/index1.html").read()
    temp = findall('(?<=<a href="/wallpaper/)([^/]+)(?=/.*1920x1080\.jpg">)', data)
    if len(temp) == 10 and temp.count(temp[0]) == 10:
        print "It is", temp[0]+"."
        return temp[0]+'/'
    else:
        print "Couldn't be determined."
        exit()

def findPicURLs(random):
    pictures = []
    for count in range(1, indices + 1):
        data = urlopen(interfacelift + urlspec + "index" + str(count) + ".html").read()
        print "Searching index", str(count), "of", str(indices)
        temp = findall(pattern, data)
        pictures.append(interfacelift + random)
        pictures += [interfacelift + random + i[:-4]+ '_' + resolution + i[-4:] for i in temp]
    return pictures

def downloadPictures(pictures):
    if len(pictures) == 0:
        return
    leftovers = []
    print "Attempting to download", len(pictures), "files..."
    for pic in pictures:
        filename = directory + '/' + pic.rpartition('/')[2]
        if not isfile(filename):
            if downloadPicture(pic): sleep(5)
            else: leftovers.append(pic)
        else:
            print "The picture is already downloaded"
    if len(leftovers):
        print "Attempting one more time to download the 404s"
        for pic in leftovers:
            if downloadPicture(pic): sleep(5)
    print "Complete."

def downloadPicture(pic):
    reqobj = Request(pic, useragent)
    print "Downloading", pic.rpartition('/')[2]+"...",
    sys.stdout.flush()
    try:
        data = urlopen(reqobj).read()
        f = open(directory + '/' + pic.rpartition('/')[2], "w")
        f.write(data)
        f.close()
        print "Done."
        return True
    except HTTPError as e:
        print e.code
        return False

print "Hello!"

if __name__ == 'main':
    if not isdir(directory):
        print directory, "doesn't exist!"
        exit()
    random = determineRandomPart()
    pictures = findPicURLs(random)
    downloadPictures(pictures)

print "Good bye!"

# vim:sw=4:et:sts=4
