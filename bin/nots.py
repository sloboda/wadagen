#!/usr/bin/env python

"""nots.py Number Of Trouble Seekers

Given information about a set of Player Characters (PCs),
determine the Average Party Level (APL) of the PCs.
That is,
get the number (the APL) of the PCs.
The Player Characters are the Trouble Seekers.

As input, takes a file in "Microsoft Windows INI file" format
  which can be read by the python module
  configparser 
  http://docs.python.org/library/configparser.html

Alternately, as input, take a directory which contains 
one or more text files ending in .pcg 
   (PCGen character files)

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

from wadage import nots

def main():
    """where it all gets done
    """
    from optparse import OptionParser
    
    parser = OptionParser()
    parser.add_option("-q", "--quiet", 
       help="quiet mode.  Just display APL", 
       action="store_false", dest="verbose", default=True)
    parser.add_option("-v", "--verbose", 
       help="verbose mode.   Display how APL was calculated", 
       action="store_true", dest="verbose", default=False)
    parser.add_option("-f", "--file", 
       help="path to file in configparser INI format", dest="input_file", default="")
    parser.add_option("-d", "--directory", 
       help="path to directory containing files ending in .pcg", dest="input_directory", default="")
    parser.add_option("-r", "--range", 
       help="display range of challenges from Easy to Epic", 
       action="store_true", dest="range", default=False)
    parser.add_option("-c", "--challenge-rating", 
       help="display CR of party (not same as APL, varies by count)", 
       action="store_true", dest="cr", default=False)
    (options, args) = parser.parse_args()
    
    result = 0    
    cr = ""
    
    if options.input_file:
        (apl, count) = nots.calculate_apl_from_file(options.input_file, options.verbose)
    if options.input_directory:
        (apl, count) = nots.calculate_apl_from_dir(options.input_directory, options.verbose)
    if options.cr:
        cr = nots.calculate_cr(apl, count)
        cr = nots.cr_int_to_cr_display(cr)
    if cr:
        result = cr
    else:
        result = apl
    if options.range:
        nots.print_range(result, options.verbose)
    else:
        if options.cr:
            type="Challenge Rating"
        else:
            type="Average Party Level"
        nots.print_result(result, options.verbose, type)


if __name__ == "__main__":
    main() 
