#!/usr/bin/python
# Created by u/JagaTelesin (reddit) - John B.
# Inspired by older scripts from alphagamm on reddit

from variables import *
import shutil
import time
import sys
from os import listdir, path
import os.path
from deluge_framework import filter_torrents

if len(sys.argv) > 1:    # If min ratio found as argument, (re)set it
    min_ratio = float(sys.argv[1])
if output:
    print "Min ratio for moving is: ",min_ratio

def torrentAction(torrent_id,torrent_info):
    if output:
        print torrent_info['name'],torrent_info['progress'],torrent_info['ratio'],torrent_info['state']
    if torrent_info['progress'] == 100.0 and torrent_info['ratio'] >= min_ratio and torrent_info['state'] not in ['Checking', 'Error']:
        shutil.copy(home_dir+'.config/deluge/state/'+torrent_id+'.torrent', to_dir)
        if output:
            print "  --->  Moving: ",torrent_info['name']
        return 'd'
    else:
        if output:
            print "  ****  Requirements not met for movement"
        return ''

# Main block
filter_torrents({},['name','progress','ratio','state'],torrentAction)
for i in listdir(from_dir):
    if os.path.isfile(to_dir+i):
        shutil.move(from_dir+i,trash_dir)
    else:
        shutil.move(from_dir+i,to_dir)
    time.sleep(step_delay)
