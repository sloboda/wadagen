"""test of nots (number of trouble seekers)

Given a set of player character data, find the Average Party Level (APL)
of the characters.
With an APL of 4, an average encounter has a Challenge Rating (CR) of 4

# wadagen: wandering damage generator
#
# Copyright 2012, sloboda
#
# This program is free software, and is provided "as is", without warranty of
# any kind, express or implied, to the extent permitted by applicable law.
# See the full license in the file 'LICENSE'.
#
# This software includes Open Game Content.  See the file 'OGL' for more
# information.
#

"""

import os
import random
import sys
import unittest

from wadage import nots 

class number_of_trouble_seekers(unittest.TestCase):
    """ test nots """
 
    def setUp(self):
        """set up challenge rating"""
        self.challenge_rating = 0


#    def test_calculate_apl_from_dir(self):
#        """given a directory with 4 pcgen files at level 8, return apl 8, not verbose"""
#        expect= 8
#        result = 0
#        pcgen_directory = "./tests/Testdata/party-pcgen-level8/"
#        result = nots.calculate_apl_from_dir(pcgen_directory, False)
#        self.assertEqual(expect, result)          


    def test_adjust_cr_down_for_3_characters(self):
        """A party of three characters at level 7 is APL 6"""
        expect= 6
        result = 0
        result = nots.calculate_cr(7, 3)
        self.assertEqual(expect, result)
    

    def test_adjust_cr_up_for_6_characters(self):
        """A party of six characters at level 4 is APL 5"""
        expect= 5
        result = 0
        result = nots.calculate_cr(4, 6)
        self.assertEqual(expect, result)
   

    def test_return_correct_string_for_cr_int_0(self):
        """CR 0 returns a string of 1/2"""
        expect= '1/2'
        result = 0
        result = nots.cr_int_to_cr_display(0)
   

    def test_return_correct_string_for_cr_int_neg_1(self):
        """CR -1 returns a string of 1/3"""
        expect= '1/3'
        result = 0
        result = nots.cr_int_to_cr_display(-1)
        self.assertEqual(expect, result)

   
    def test_return_correct_string_for_cr_int_neg_2(self):
        """CR -2 returns a string of 1/4"""
        expect= '1/4'
        result = 0
        result = nots.cr_int_to_cr_display(-2)
        self.assertEqual(expect, result)


    def test_return_correct_string_for_cr_int_neg_3(self):
        """CR -3 returns a string of 1/6"""
        expect= '1/6'
        result = 0
        result = nots.cr_int_to_cr_display(-3)
        self.assertEqual(expect, result)


    def test_return_correct_string_for_cr_int_neg_4(self):
        """CR -4 returns a string of 1/8"""
        expect= '1/8'
        result = 0
        result = nots.cr_int_to_cr_display(-4)
        self.assertEqual(expect, result)


    def test_return_correct_string_for_cr_int_2(self):
        """CR 2 returns a string of 2"""
        expect= '2'
        result = 0
        result = nots.cr_int_to_cr_display(2)
        self.assertEqual(expect, result)


    def test_return_correct_string_for_cr_int_20(self):
        """CR 20 returns a string of 20"""
        expect= '20'
        result = 0
        result = nots.cr_int_to_cr_display(20)
        self.assertEqual(expect, result)


    def test_return_correct_string_for_cr_int_3(self):
        """CR 3 returns a string of 3"""
        expect= '3'
        result = 0
        result = nots.cr_int_to_cr_display(3)
        self.assertEqual(expect, result)


if __name__ == "__main__":
    unittest.main() 
