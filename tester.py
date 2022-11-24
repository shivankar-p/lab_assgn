#!/usr/bin/python3

import unittest
from substring import check
from palindrome import palindrome

class Calculator(unittest.TestCase):

    def is_substr(self):
        str = "abcd"
        sub_str = "abc"
        result = check(str, sub_str)
        self.assertEqual(result, 1)
    
    def not_substr(self):
        str = "abcd"
        sub_str = "cda"
        result = check(str, sub_str)
        self.assertEqual(result, -1)
    
    def pal(self):
        str = "aba"
        result = palindrome(str)
        self.assertEqual(result, True)
    def not_pal(self):
        str = "abc"
        result = palindrome(str)
        self.assertEqual(result, False)

    

if __name__ == '__main__':
    unittest.main()