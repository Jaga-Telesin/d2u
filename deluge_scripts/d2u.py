#!/usr/bin/python
# Created by u/JagaTelesin (reddit)
# Inspired by older scripts from alphagamm on reddit

from variables import *
import shutil
import time
from os import listdir, path
import os.path
from deluge_framework import filter_torrents

def torrentAction(torrent_id,torrent_info):
    if torrent_info['progress'] == 100 and torrent_info['ratio'] >= min_ratio and torrent_info['state'] not in ['checking', 'error']:
        shutil.copy(home_dir+'.config/deluge/state/'+torrent_id+'.torrent', to_dir)
        return 'd'
    return ''

# Main block
filter_torrents({},['name','progress','ratio','state'],torrentAction)
for i in listdir(from_dir):
    if os.path.isfile(to_dir+i):
	    shutil.move(from_dir+i,trash_dir)
    else:
        shutil.move(from_dir+i,to_dir)
        sleep(step_delay)
