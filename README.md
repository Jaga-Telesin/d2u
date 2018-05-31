
D2U (Deluge to uTorrent)
========================
- Created by u/JagaTelesin (reddit) - John B.
- Inspired by older scripts from alphagamm on reddit
- Uses the Deluge Framework (included in D2U already) https://github.com/BackSlasher/deluge_framework (GNU 2.0 license)

v1.1, March 30, 2018
====================
- Syntax corrections for delay in loop
- Added optional command line argument for minimum ratio (min_ratio)
   Usage:  python -u d2y.py 0.8    (as an example to only move torrents at or above a 0.8 ratio)
- Added additional information from script when output variable is 'True'


Note:  The D2U_v1.1.zip file in this repository has all scripts and empty folders required for a server installation.


Why to use D2U, Deluge and uTorrent
===================================
- Deluge is much faster downloading and uploading torrents due to it's aggressiveness, but worse for long-term seeing or when you have a large number active.  It is advantageous to grab a torrent early with Deluge, seed during the initial swarm, and then later move the torrent into uTorrent for long-term seeding.  D2U does the moving for you (on the same server only), is configurable, and can be run on a cron job for scheduling.
- You can also setup autodl-irssi so that uTorrent snatches torrents from an announce channel link and places them in the Deluge watch folder for immediate addition.  However, you can grab torrents and have them added into Deluge any way you want, so autodl-irssi is completely optional.

Features
========
- Moves only finished torrents from Deluge to uTorrent
- Won't move torrents still downloading, being checked, or with errors
- Configurable minimum seed amount before moving
- Min seed amount can be passed with command line argument (ex: python d2u.py 0.8
- Duplicate torrents stored in a trash folder
- uTorrent hash-checks files after receiving them
- Detailed info when using output=True variable

Requirements
============
- Deluge, uTorrent and Python
- A medium to fast server.  Running Deluge aggressively and uTorrent (with many torrents) on a cheap or inexpensive Seedbox will push the server hard, especially for bandwidth.  If you want to reduce load when using this configuration and a slower server, don't snatch more than 1-2 torrents per hour total.

Recommendations
===============
- Install the 'ltconfig' plug-in in Deluge, go to configure it in the plug-ins area, select the 'High Performance Seed' profile, hit the 'Load Preset' button, then Apply and OK.  After that restart Deluge on your server.  This will configure Deluge's settings to help with speeds during initial torrent snatching when the swarm is still busy.



Installing/Configuring
======================

Step 1 - Customize
- Extract .zip files/folders to a folder named 'd2u' (all lowercase).
- Open the variables.py file with a text editor.
- Edit the variables to suit your server and directory structure.  Note:  you will need to find out what port your Deluge uses for console communications (it's Daemon port) and enter it next to the variable 'deluge_port'.  To find out your port open the Deluge GUI interface, go into Preferences, click 'Daemon' on the left side, and note the port being used.  Be sure 'Allow Remote Connections' is enabled on that panel.
- For first-time installations, it is recommended to set the 'output' variable to 'True', so you can see feedback from your manual test run(s).
- Save and exit the variables.py file when done editing.


Step 2 - Upload
- Connect to your server with a FTP program.
- Upload the 'd2u' folder and all contents to your '/home/user/downloads' folder (or whatever root folder your uTorrent/Deluge clients can watch for auto-adding).
- Navigate into the new 'd2u/deluge_scripts' folder and set permissions on all files to 755 (execute enabled permissions).
- Alternately, if you want to use a SSH shell to change file permissions, use 'chmod +x filename' on all the files in the /deluge_scripts directory.


Step 3 - Configure clients
- Set Deluge's watch directory to the '/d2u/deluge_watch' folder on the server and enable the feature in Deluge.
- Using the AutoTools (uTorrent plug-in) autowatch feature, set uTorrent's watch directory to the '/d2u/utorrent_watch' folder on the server and enable.
- Test Deluge's auto-add by either manually uploading a .torrent file to the '/d2u/deluge_watch' folder, or by configuring and using uTorrent's autodl-irssi (a separate setup/process) to snatch and place the torrent file in that folder automatically.  Search the web if you need help setting up autodl-irssi, since there are several steps involved and not all trackers support it.
- Recommended:  use Deluge's preferences to copy the .torrent (when added to Deluge) to a folder on your server, like '/home/user/downloads/deluge/torrents'.  That way you have a good original copy of all .torrent files if something happens to one during the move process and you need it.  After the script runs you can clean up files in that folder whenever you like.


Step 4 - Manually running D2U
- Remember that any torrents Deluge has finished downloading and which meet your ratio minimum set in the variables.py file, will have their .torrent removed from Deluge and moved to your uTorrent watch folder.  There is no confirmation of the move - the script was set to run and complete quietly.
- SSH to your server, and navigate to your 'd2u/deluge_scripts directory' (ex: /home/user/downloads/d2u/deluge_scripts).
- Run the following command: python -u d2u.py
- Optionally, you can add the required minimum ratio on the command line, like:  python -u d2u.py 0.8
- The -u is necessary for script timing (delays between each move)
- Note any output or errors.  See the 'Troubleshooting' section below if you run into problems.


Step 5 - Automating D2U  (optional)
- You can use a cron job to automate the D2U script.  From a SSH shell, run 'crontab -e' and add a new line for the job (Search the web for more information on setting up a cron job if needed).  I prefer to have it run every 24 hours at 3am, but shorter or longer is fine too.  An example line in the crontab editor for a 24-hour schedule looks like this:
 0 3 * * * python -u /home/user/downloads/d2u/deluge_scripts/d2u.py
- Be sure to replace the path with one appropriate to your server and your folder configuration!
- When you are satisfied your cron job is setup correctly, edit your '/d2u/deluge_scripts/variables.py' file, change the output setting to 'False' and add # before the two debug lines.  This will suppress any messages when the cron job runs.



Troubleshooting
================

To find out why the script might be having issues on your server, edit the '/d2u/deluge_scripts/variables.py' file, change output to 'True', then remove the comment #'s from the beginning of the two lines under 'Debugging' and save the file.  Then SSH into your server, navigate to the '/d2u/deluge_scripts' folder, and run the script using 'python -u d2u.py'.  All info will be output to the console to help with diagnosis.



D2U License
===========

MIT License (https://opensource.org/licenses/MIT)
Copyright <2018> <John B. (u/JagaTelesin)>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Attribution must be included in any distribution of this package.

