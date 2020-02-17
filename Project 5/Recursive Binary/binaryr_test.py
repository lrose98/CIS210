import unittest
import p51_binaryr
from p51_binaryr import dtobr, btodr

class TestDtoBr(unittest.TestCase):
    """ Test cases for dtob """
    def test_dtobr1(self):
        self.assertEqual(dtobr(298), '100101010')

    def test_dtobr2(self):
        self.assertEqual(dtobr(8), '1000')

class TestBtoDr(unittest.TestCase):
    """ Test cases for btod """
    def test_btod1(self):
        self.assertEqual(btodr('0000'), 0)

    def test_btod2(self):
        self.assertEqual(btodr('111111'), 63)

if __name__ == '__main__':
    unittest.main()
