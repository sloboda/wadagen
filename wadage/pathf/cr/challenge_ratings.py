### The idea here is to build a scale of Challenge Ratings
### (CR) values for monsters that makes it easier on the math. :-)
###
### According to the Pathfinder Bestiary, 
###    a Raven has a Challenge Rating of "1/6"
### This scale will help calculate that three first-level Player Characters (CR 0)
###    have an Easy encounter at CR 1/2
###    Better yet, this scale will allow a program to calculate that
###    value for the Easy encounter.
### It will also allow quantity 4 ravens (add +4 to CR)
###     move from CR 1/6 to CR1

### format of challenging rating scale is
###    'scale number':'display CR' 
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

ratings = { 
	25 : "25",
	24 : "24",
	23 : "23",
	22 : "22",
	21 : "21",
	20 : "20",
	19 : "19",
	18 : "18",
	17 : "17",
	16 : "16",
	15 : "15",
	14 : "14",
	13 : "13",
	12 : "12",
	11 : "11",
	10 : "10",
	9 : "9",
	8 : "8",
	7 : "7",
	6 : "6",
	5 : "5",
	4 : "4",
	3 : "3",
	2 : "2",
	1 : "1",
	0  : "1/2",
	-1 : "1/3",
	-2 : "1/4",
	-3 : "1/6",
	-4 : "1/8",
 }
