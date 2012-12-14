#!/usr/bin/env bash

# setup.sh
# PURPOSE
# set environment variables to include the bin and library directories 
# for the wadagen program.
#
# USAGE
# Edit this file to put the full path to wadagen in PROJECTDIR
#   then, run as follows:
# cd {whatever path you put in PROJECTDIR}
# . ./bin/setup.sh
# That source (.) command loads the environment variables 
#
# LAST MODIFIED
# Thu Dec 13 15:53:25 PST 2012
# 
# Copyright 2012, sloboda
#
# This program is free software, and is provided "as is" 
# without warranty of any kind, express or implied, 
# to the extent permitted by applicable law.
# See the full license in the file 'LICENSE'.
#
# This software includes Open Game Content.  
# See the file 'OGL' for more information.
#


# replace this with the full path to wadagen on your system
PROJECTDIR="/opt/W/wadagen"

PATH=$PATH:$PROJECTDIR/bin
PYTHONPATH=$PYTHONPATH:$PROJECTDIR/wadage

export PATH
export PYTHONPATH

# Do not put an exit statement in script, or the shell will terminate.
#exit 0

