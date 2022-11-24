#!/usr/bin/python3

import unittest
from substring import check

class Calculator(unittest.TestCase):

    def is_substr(self):
        str = "abcd"
        sub_str = "abc"
        result = check(str, sub_str)
        self.assertEqual(result, 0)
    
    def not_substr(self):
        str = "abcd"
        sub_str = "cda"
        result = check(str, sub_str)
        self.assertEqual(result, -1)
    

if __name__ == '__main__':
    unittest.main()