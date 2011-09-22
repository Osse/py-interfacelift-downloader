#!/usr/bin/env python
# encoding: utf-8

from urllib2 import urlopen, Request
from re import findall
from time import sleep
# from subprocess import call
from os.path import expanduser

# Modify the two strings below to your preferences
urlspec = 'rating/widescreen/1920x1200/'
urlspec = 'tags/60/location/canada/'
random  = '7yz4ma1/'

resolution = '1920x1200'
directory = expanduser('~')+'/Pictures/Interfacelift-test'
rate = '100K'

urlbase   = 'http://interfacelift.com/wallpaper/'
pattern   = '(?<=previews/)\d{5}_\w+\.jpg'
useragent = 'User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)'
uapixels = 'UA-pixels: '+resolution
url       = urlbase+urlspec
# wgetcmd   = [ 'wget', '--user-agent='+useragent, '--directory-prefix='+directory, '--no-clobber', '--wait=5',
              # '--random-wait', '--limit-rate='+rate, '--retry-connrefused', '--referer='+urlbase ]
pictures = []

for count in range(2,3):
        data = urlopen(url + "index" + str(count) + ".html").read()
        # print data
        # exit()
        temp = findall(pattern, data)
        pictures += [urlbase+random+i.replace('.jpg', '_'+resolution+'.jpg') for i in temp]
if len(pictures) > 0:
        print "Attempting to download", len(pictures), "files without wget..."
        # print '\n'.join(pictures)
        # exit()
        for pic in pictures:
                sleep(5)
                reqobj = Request(pic, useragent)
                filename = pic.rpartition('/')[2]
                print "Laster ned", pic
                f = open(directory+'/'+filename, "w")
                data = urlopen(reqobj).read()
                f.write(data)
                f.close()
                print "Ferdig"
        print "Complete."
else:
        print "No pictures to download. Either the range is zero in length or the regex needs to be refined."

# vim:sw=8:ts=8:et:sts=8
