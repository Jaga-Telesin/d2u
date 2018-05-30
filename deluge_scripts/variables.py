#!/usr/bin/python
# Created by u/JagaTelesin (reddit) - John B.

min_ratio    = 1.0                         # Don't move torrents until they reach or exceed a ratio of X
                                           # NOTE: min_ratio is able to be passed to the script as a command line parameter
                                           #   ex:  python d2u.py 0.8
deluge_port  = 21000                       # Server daemon port (integer)
output       = True                       # Set to 'False' for cron jobs. Set to 'True' to see output in a shell.
step_delay   = 1                           # If your server has problems with the script speed, increase this value
home_dir     = '/home/user/'               # Replace with your home directory. Should be similar to '/home/user/'
auto_dir     = 'downloads/d2u/'            # Location of d2u folder structure (under your home directory)
trash_dir    = home_dir+auto_dir+'trash/'  # Duplicate torrents end up here
from_dir     = home_dir+auto_dir+'deluge_torrents/'
to_dir       = home_dir+auto_dir+'utorrent_watch/'

# Debugging - uncomment (#) the following lines to enable debug output:
#import logging, sys
#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
