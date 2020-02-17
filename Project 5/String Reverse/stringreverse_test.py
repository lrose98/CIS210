'''
CIS 210 Project 4-2: Decimal to Binary to Decimal

Author: Lillie Rose

Credits: Joey Valko
'''
import unittest
import p52_stringreverse
from p52_stringreverse import stringReverseR, stringReverseI

class StringReverseR_test(unittest.TestCase):
    """ Test cases for StringReverseR """
    def test_strR1(self):
        self.assertTrue(stringReverseR('main'), 'niam')
    def test_strR1(self):
        self.assertTrue(stringReverseR('asdf'), 'fdsa')
    def test_strR1(self):
        self.assertTrue(stringReverseR('a'), 'a')

class StringReverseI_test(unittest.TestCase):
    """test cases for StringReverseI"""
    def test_strR1(self):
        self.assertTrue(stringReverseR('niam'), 'main')
    def test_strR1(self):
        self.assertTrue(stringReverseR('fdsa'), 'asdf')
    def test_strR1(self):
        self.assertTrue(stringReverseR('a'), 'a')