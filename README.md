# Boring-routines
 This project was a inspiration from a instagram post https://www.instagram.com/p/CYbJ7drrqz_/?utm_source=ig_web_copy_link were a build engineer automated his boring time consuming tasks which all programmers deal everyday.
 ![alt text](https://github.com/aravind-tronix/Boring-routines/blob/main/static/271346159_612678286690680_2181000804045233389_n.jpg)
 
 ## Installation
 
 clone the repo and install requirements by running the command from requirements folder
 
 ``pip install -r requirements.txt``
 
 edit the file supervisord.conf according to your system path. Supervisor is a client/server system that allows its users to control a number of processes on UNIX-like operating systems.(same as cron). Supervisor has been tested and is known to run on Linux (Ubuntu 18.04), Mac OS X (10.4/10.5/10.6), and Solaris (10 for Intel) and FreeBSD 6.1. It will likely work fine on most UNIX systems.

Supervisor will not run at all under any version of Windows.
For more, refer http://supervisord.org/introduction.html
 
 ## Usage
 start supervisor by
 ``supervisord``
 start process by
 ``supervisorctl``
 
