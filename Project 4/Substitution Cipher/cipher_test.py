'''
CIS 210 Project 4-1: Cipher text with a Password

Author: Lillie Rose

Credits: Joey Valko
'''
import unittest
import p41_cipher
from p41_cipher import substitutionEncrypt, substitutionDecrypt


class TestCipherEncrypt(unittest.TestCase):
    """ Test cases for substitutionEncrypt """
    def test_encrypt1(self):
        self.assertTrue(substitutionEncrypt('the quick brown fox', 'ajax'), 'qdznrexgjoltkblu')

    def test_encrypt2(self):
        self.assertTrue(substitutionEncrypt('hello world', 'october'), 'ueyydmdhyb')

class TestCipherDecrypt(unittest.TestCase):
    """ Test cases for substitutionDecrypt """
    def test_decrypt1(self):
        self.assertTrue(substitutionDecrypt('qdznrexgjoltkblu', 'ajax'), 'thequickbrownfox')

    def test_decrypt2(self):
        self.assertTrue(substitutionDecrypt('ueyydmdhyb', 'october'), 'helloworld')



if __name__ == '__main__':
    unittest.main()
