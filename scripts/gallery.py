#!/usr/bin/python

print '<div id="gallery">'


thumbs_directory = '../images/thumbs'
orig_directory = '../images/gallery'

MAX_HEIGHT = 120
MAX_WIDTH = 200

files = os.readdir(orig_directory)

############################

i=1
for f in files:
    if f in ['.', '..']: continue

    top=rand(50, 60);
    rot = rand(-20,20);

    print """<div id="pic-%d" class="pic" style="top:%dpx;left:%dpx;"><a class="p1" rel="imageGallery[home_gal]" href="%s/%s" target="_blank"><img src="%s/%s" style=" -moz-transform:rotate(%ddeg); -webkit-transform:rotate(%ddeg); -o-transform:rotate(%ddeg); -ms-transform:rotate(%ddeg); transform:rotate(%ddeg);">
</a></div>""" % (i, top, left, orig_directory, f, thumbs_directory, f, rot, rot, rot, rot, rot)
    i += 1

    left = left + rand(50,110);

print '</div>'
