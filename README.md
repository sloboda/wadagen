# wadagen  (Wandering Damage Generator)#

## 1. Identification ##

Wadagen is a set of tools to create opponents
for player characters within the Pathfinder Role Playing Game.

What distinguises wadagen from other tools?  The player character data 
is used as input for generating opponents.


Wadagen is made up of three separate tools:

1.  Take Player Character data as input and produce 
Average Party Level (APL) as output.  (This tool is called 
*nots* because it gets the Number Of Trouble Seekers.)

2.  Given an APL, suggest opponents for the Player Characters (PCs).  
(This tool is called *wadage*  to distinguish it from 
the set of tools. The set is called wadagen.)

3.  Generate Non-Player Characters (NPCs).  (This tool is called 
*suffering* because in English it is an aphorism that 
"Suffering Builds Character.")


## 2. Prerequisites ##

This set of tools requires python 2.7.  

It has only been tested on Linux (Ubuntu 10.04).

## 3. How to Use ##

1. cd into the wadagen directory
2. in the file wadagen/bin/setup.sh edit the line 
PROJECTDIR="/home/account/wadagen" .  
Change it the correct path to wadagen on your system.

3. set up $PATH and $PYTHONPATH environment variables with the command 

    . ./bin/setup.sh


3. ./bin/nots.py -h will display a help message



## 4. Legal ##

The software in this package is copyright (c) 2012, sloboda.
All rights reserved, and is stated in each source code file.
See the file "LICENSE" for licensing information, terms and conditions for
usage, and a DISCLAIMER OF ALL WARRANTIES.

This softare package also includes Open Game Content.  See the file "OGL" for
a copy of the Open Game License and list of Open Game Content used by this
software.

All trademarks referenced herein are property of their respective holders.

Suggestions and assistance are appreciated.  
The email contact address is wadagen dot beta at gmail dot com.



