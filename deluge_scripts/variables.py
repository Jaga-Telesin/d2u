#!/usr/bin/python
# Created by u/JagaTelesin (reddit)

deluge_port  = 21000                       # Server daemon port (integer)
min_ratio    = 1.0                         # Don't move torrents until they reach or exceed a ratio of X
output       = False                       # Set to 'False' for cron jobs. Set to 'True' to see output in a shell.
step_delay   = 5                           # If your server has problems with the script speed, increase this value
home_dir     = '/home/user/'               # Replace with your home directory. Should be similar to '/home/user/'
auto_dir     = 'downloads/d2u/'            # Location of d2u folder structure (under your home directory)
trash_dir    = home_dir+auto_dir+'trash/'  # Duplicate torrents end up here
from_dir     = home_dir+auto_dir+'deluge_torrents/'
to_dir       = home_dir+auto_dir+'utorrent_watch/'

# Debugging - uncomment (#) the following lines to enable debug output:
#import logging, sys
#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
