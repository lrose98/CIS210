'''
CIS 210 Project 4-2: Decimal to Binary to Decimal

Author: Lillie Rose

Credits: Joey Valko
'''

import unittest
import p42_binary
from p42_binary import dtob, btod

class TestDtoB(unittest.TestCase):
    """ Test cases for dtob """
    def test_dtob1(self):
        self.assertEqual(dtob(17), '0b10001')

    def test_dtob2(self):
        self.assertEqual(dtob(311), '0b100110111')

class TestBtoD(unittest.TestCase):
    """ Test cases for btod """
    def test_btod1(self):
        print(bin(298))
        self.assertEqual(btod('100101010'), 298)

    def test_btod2(self):
        self.assertEqual(btod('110010101'), 405)

if __name__ == '__main__':
    unittest.main()
