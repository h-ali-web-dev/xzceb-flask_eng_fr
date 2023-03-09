from translator import english_to_french,french_to_english
import unittest

class test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assetEqual(french_to_english('Hello'),'Bonjour')
        self.assetEqual(french_to_english(),'')

class test_EnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assetEqual(english_to_french('Bonjour'),'Hello')
        self.assetEqual(english_to_french(),'')
