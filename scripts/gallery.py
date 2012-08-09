#!/usr/bin/python

import random
import os
from PIL import Image

print '<div id="gallery">'


thumbs_directory = '../images/thumbs'
orig_directory = '../images/gallery'

MAX_HEIGHT = 90
MAX_WIDTH = 120

files = os.listdir(orig_directory)
def scale_down(img):
    full_scale = Image.open(orig_directory + '/' + img)

    o_w, o_h = full_scale.size

    def isInt(h): return h != 'auto'

    if o_w < o_h: w, h = 'auto', MAX_HEIGHT
    if o_w > o_h: w, h = MAX_WIDTH, 'auto'

    if w == 'auto' and isInt(h):
        w = int(int(h) * o_w / o_h);
    if h == 'auto' and isInt(w):
        h = int(int(w) * o_h / o_w);
    if h == 'auto' and w == 'auto':
        # bone-head-ness
        raise "both height and width cannot be auto"

    w, h = int(w), int(h)

    scaled_name = thumbs_directory + '/' + img

    scaled_file = open(scaled_name, 'w')
                # resample and resize
    scaled_data = full_scale.resize((w, h), 1)
    scaled_data.save(scaled_file, 'JPEG', quality=80)
    return scaled_name

############################

i=1
left=0
for f in sorted(files):
    if f in ['.', '..']: continue

    top=random.randrange(50, 61);
    rot = random.randrange(-20,21);

    print """<div id="pic-%d" class="pic" style="top:%dpx;left:%dpx;"><a class="p1" rel="imageGallery[home_gal]" href="%s/%s" target="_blank"><img src="%s" style=" -moz-transform:rotate(%ddeg); -webkit-transform:rotate(%ddeg); -o-transform:rotate(%ddeg); -ms-transform:rotate(%ddeg); transform:rotate(%ddeg);">
</a></div>""" % (i, top, left, orig_directory.replace('../', ''), f, scale_down(f).replace("../", ""), rot, rot, rot, rot, rot)
    i += 1

    left = left + random.randrange(50,60);

print '</div>'
