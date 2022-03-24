from utilities.loader import WordLoader
import os 
from utilities.saver import WordSaver
import unittest
from search_engine import OxfordDictionary
from utilities.display import WordDisplayer
from utilities import get_k_previous_date


class SaveLoadTest(unittest.TestCase):
    def search_a_word(self):
        word = "roughly"
        print(f"Search for \"{word}\" (get only the first result)")

        results = OxfordDictionary().search_word(word)
        return results[0]

    def test_save_load(self):
        word = self.search_a_word()

        print("Save the word ...")
        WordSaver().save(word)

        print("Load the word ...")
        date = get_k_previous_date(k=0)
        words = WordLoader().load(date)

        for word in words:
            WordDisplayer.show(word)
            print("------------------")
