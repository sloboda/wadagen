Examples of how to use the tools included with wadagen

# Set up of $PYTHONPATH and other environment variables #

    $ ./bin/nots.py -h
    Traceback (most recent call last):
      File "./bin/nots.py", line 33, in <module>
        from wadage import nots
    ImportError: No module named wadage
    $ echo $PYTHONPATH
            
    $ . ./bin/setup.sh
    $ echo $PYTHONPATH
    :/opt/W/wadagen/wadage
    $

Now that the PYTHONPATH is set, 
nots.py shows a usage message

    $ ./bin/nots.py -h
    Usage: nots.py [options]

    Options:
      -h, --help            show this help message and exit
      -q, --quiet           quiet mode.  Just display APL
      -v, --verbose         verbose mode.   Display how APL was calculated
      -f INPUT_FILE, --file=INPUT_FILE
                            path to file in configparser INI format
      -d INPUT_DIRECTORY, --directory=INPUT_DIRECTORY
                            path to directory containing files ending in .pcg
      -r, --range           display range of challenges from Easy to Epic
      -c, --challenge-rating
                            display CR of party (not same as APL, varies by count)
    $


# nots (Number Of Trouble Seekers) usage #

    $ ./bin/nots.py -h
    Usage: nots.py [options]
     
    Options:
      -h, --help            show this help message and exit
      -q, --quiet           quiet mode.  Just display APL
      -v, --verbose         verbose mode.   Display how APL was calculated
      -f INPUT_FILE, --file=INPUT_FILE
                            path to file in configparser INI format
      -d INPUT_DIRECTORY, --directory=INPUT_DIRECTORY
                            path to directory containing files ending in .pcg
      -r, --range           display range of challenges from Easy to Epic
      -c, --challenge-rating
                            display CR of party (not same as APL, varies by count)
    $

# use nots.py to find the number of trouble seekers #

Turn data on your player characters into data you may use.

Example number One:  a set of files in a directory, ending in .pcg

One of the files is a wizard's familiar. 

    $ ls -l  ./tests/Testdata/party_l1/
    total 32
    -rw-r--r-- 1 user group 6304 2012-12-12 21:22 Ariel_familiar.pcg
    -rw-r--r-- 1 user group 7604 2012-12-12 21:22 Coriolanus_ftr1.pcg
    -rw-r--r-- 1 user group 7058 2012-12-12 21:22 Friar_Francis_clr1.pcg
    -rw-r--r-- 1 user group 7577 2012-12-12 21:22 Prospero_wiz1.pcg
    $

Find the average party level of the characters in that directory

    $ ./bin/nots.py -d ./tests/Testdata/party_l1/
    1
    $
 
Find the challenge rating of the party represented by the characters in that directory

    $ ./bin/nots.py -d ./tests/Testdata/party_l1/ --challenge-rating
    1/2
    $ 


Find the average party level of the characters in that directory.  
Be verbose about how that is done.

    $ ./bin/nots.py -d ./tests/Testdata/party_l1/  -v
    ./tests/Testdata/party_l1/ is a directory
    There are 4 files in the directory ./tests/Testdata/party_l1/
    4 of them are pcgen files
    ./tests/Testdata/party_l1/Ariel_familiar.pcg is a companion
    All character levels = 3
    Average is 3 / 3  = [1]
    Average Party Level is 1
    $


Find the challenge rating of the party represented by the characters in that directory
Be verbose about how that is done.

    $ ./bin/nots.py -d ./tests/Testdata/party_l1/ --challenge-rating -v
    ./tests/Testdata/party_l1/ is a directory
    There are 4 files in the directory ./tests/Testdata/party_l1/
    4 of them are pcgen files
    ./tests/Testdata/party_l1/Ariel_familiar.pcg is a companion
    All character levels = 3
    Average is 3 / 3  = [1]
    Challenge Rating is 1/2
    $ 

