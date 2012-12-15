"""nots: number of trouble seekers

The methods and functions in this module
are designed to get the number of the trouble seekers.
This does not  mean the count of the player characters.
This means the Average Party Level (APL) according to the 
   Core Rules of the Pathfinder Role Playing Game.

These methods are broken out from the Command Line Interface
   ./bin/nots.py 
so that the methods can be tested via unit tests.

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

"""

def calculate_apl_from_file(file, verbose):
    """calculate the Average Party Level (apl) from a file
    """
    result = 0 
    from wadage.calculate_apl_from_ini import get_apl_from_configfile
    (apl, count) = get_apl_from_configfile(file)
    return  (apl, count)


def calculate_cr(apl, number_of_party_members):
    """given apl and count, calculate cr

    The typical adventuring party has 4 or 5 members.

    The average party level (APL) of 6 PCs all at level 10 is 10
    The CR of this party is 11.

    The average party level (APL) of 3 PCs all at level 3 is 3
    The CR of this party is 2.

    This script returns integers (0) not CR strings ('1/2')
    A second method converts integers to strings.
    """
    result = 0
    if number_of_party_members < 4:
        result = apl - 1
    if number_of_party_members > 5:
        result = apl + 1
    return int(result)
 


def calculate_apl_from_dir(directory, verbose):
    """calculate the Average Party Level (apl) from a directory

    It is assumed the directory contains .pcg files
    """
    result = 0 
    import os
    import re
    import sys
    all_levels = 0
    pcg_files = []
    pcg_pc_files = []
    if os.path.isdir(directory):
        if verbose: 
            print "%s is a directory" % (str(directory))
        count = 0
        if verbose:
            print "There are %d files in the directory %s" % (
                int(len([name for name in os.listdir(directory) 
                    if os.path.isfile(os.path.join(directory,name))]) ),
                str(directory)
                )
        for fname in os.listdir(directory):
            pname = os.path.join(directory,fname)
            extension = os.path.splitext(pname)[1]
            extension = str(extension.lower())
            if extension == ".pcg":
                count=count + 1 # increment counter
                pcg_files.append(pname)
            else:
                if verbose:
                    print "%s is not a pcgen file" % str(pname)
        if verbose:
            print "%d of them are pcgen files" % (int(count))
        # figure out which are PCs and which are companions to PCs
                #  open entire file and parse contents
        for pname in pcg_files:
                companion = False
                f = open(pname)
                contents = f.readlines()
                for line in contents:
                     matchcount =  re.findall("^MASTER:", line, flags=0)
                     if len(matchcount) > 0:
                         companion = True
                if companion:
                     if verbose:
                         print "%s is a companion" % (str(pname))
                else:
                     pcg_pc_files.append(pname)
        # reset the int variable "count" to include only pcg files
        #    that are PCs.  No mounts, familiars, animal companions
        count = len(pcg_pc_files) 
        for pname in pcg_pc_files:
                f = open(pname)
                contents = f.readlines()
                for line in contents:
                     matchcount =  re.findall("^CLASSABILITIESLEVEL:", line, flags=0)
                     if len(matchcount) > 0:
                         all_levels += 1
        if verbose:
            print "All character levels = %d" % (int(all_levels))
        apl = 0
        # next line explicitly returns a float here, for python3
        apl = ( (all_levels)*1.0 / (count) )  
        apl = round(apl)     # round the float to zero decimal points
        result = apl
        result = int(result) # coerce type to int. We really want zero decimal points
        if verbose:
           print "Average is %d / %d  = [%d]" % (all_levels, count, apl)
    else:
        if verbose:
           print "Error: %s is NOT a directory" % (str(directory))
    return (result, count)
    

def print_result(result, verbose, type="Average Party Level"):
    """given a result, print it to standard output
    """
    if verbose:
        print "%s is %s" % (str(type), str(result))
    else:
        print "%s" % (str(result))
    return 0


def print_range(result, verbose):
    """given a result, print a range of CRs to standard output

    The default is to print the Average Party Level (APL)
    of the Player Characters.

    The "range" option prints the range 
    of Easy, Average, Challenging, Hard, Epic
    where the Challenge Rating is based off of the APL.
    Easy means CR = APL - 1
    Average means CR = APL
    and
    Epic means CR = APL + 3

    The "verbose" flag prints the headings
    """
    range_list = {}
    difficulty_levels = [ "Easy", "Average", 
      "Challenging", "Hard", "Epic" ]
    for dl in difficulty_levels:
       if dl == "Easy":
           range_list[dl] =  (result - 1)
       if dl == "Average":
           range_list[dl] =  result
       if dl == "Challenging":
           range_list[dl] =  (result + 1)
       if dl == "Hard":
           range_list[dl] =  (result + 2)
       if dl == "Epic":
           range_list[dl] =  (result + 3)
    for cr_name in difficulty_levels: 
        display_name = cr_int_to_cr_display(range_list[cr_name])
        if verbose:
            print "%s here is CR %s" % (str(cr_name), 
               str(display_name) )
        else:
            print "%d" % ( int(range_list[cr_name]) )
    return 0

def cr_int_to_cr_display(cr_int):
    """for Challenge Rating: turn integer into display names
  
    It's easier to calculate math on integers when
       adding or subtracting challenge ratings.
    The rules speak of monsters having challenge ratings of
       1/2 or 1/3 or 1/4   
    This script converts integers into strings.
    Example: convert CR "0" into "1/2" 
    """
    result = ""
    from wadage.pathf.cr import challenge_ratings
    #  get the value from the cr_int key
    result = challenge_ratings.ratings[cr_int]
    return result


