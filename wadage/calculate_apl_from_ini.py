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


import ConfigParser
import re

def get_apl_from_configfile(configfile):
    """given a config file in ini syntax,
    return the Average Party Level (APL) 
    for the party members described in the file 

    APL is for the most part an average of the character levels
    if the party has four of five characters.
    For a party of three or fewer characters, subtract one.
    For a party of six or more characters, add one.

    Sample party lists in config (.INI) format are found
      in the /tests/Testdata/party-*-configfile/ directories
    """
    result = 0 # the APL returned
    total = 0  # the total number of character levels
    config = ConfigParser.RawConfigParser()
    config.read(configfile)
    ### intent of regex pattern here 
    ###    is to catch one or more digits after a text level
    ###  Changed the regex from .*(\d+) to just (\d+)
    ###    to remove need for contortions required 
    ###    in order to split on spaces 
    ###    yet handle "eldritch knight 3" as a class level
    pattern = re.compile(r'''
    (\d+)
    ''',
    re.VERBOSE|re.DOTALL)  # end of regex pattern
    for c in config.sections():  # each character given a section
        working_list = config.items(c)
        # The characters and levels can be expressed in at least
        # three different ways.
        for (attribute, item) in working_list:
            if attribute == "level":  # most straightforward way,
                 # level: 4
                 total = total + int(item)
            elif attribute == "class":
                 # this can be one of the following
                 # class:fighter (no level indicated; the level is a distinct entry)
                 # class:fighter 1 (level indicated after single class)
                 # or
                 # class:fighter 1, wizard1, rogue1 
                 #  (i.e. multiclass characters)
                 #  For the last two methods, we build a list and parse each item. 
                 #print "\nItem here is %s" % (str(item))
                 classlist = []
                 if ',' in item:
                      classlist = item.split(',')
                 else:
                      classlist.append(item)
                 for cl_item in classlist:
                      res = re.search(pattern, cl_item)
                      if res:
                         term = res.group(0)
                         level = int(term)
                         total = total + int(level)
                      else:
                         pass
    number_of_party_members =  len(config.sections())
    # next line redone for python 3
    result = divmod(total, number_of_party_members)[0]
### next for lines moved to a separate function
#    if number_of_party_members < 4:
#        result = result - 1
#    if number_of_party_members > 5:
#        result = result + 1
    return  (result, number_of_party_members)

