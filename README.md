# SQL_Python_tshark

# Author: Maciej Godula
# GitHub repository: https://github.com/godulam/SQL_Python_tshark

use run.sh bash script with root privileges to run a ip collection (tshark part)
command : $sudo bash /path_to_file/run.sh

to run a statistics script (with ping)
command : $sudo python3 /path_to_file/test.py
or place it in crontab to make it run every 3 minutes:
command: $crontab -e */3 * * * * /path_to_file/test.py

to run a report (shortest and longest response times)
command: $sudo python3 reports.py
