import unittest
from search_engine import OxfordDictionary
from utilities.display import WordDisplayer


class OxfordDictionaryTest(unittest.TestCase):
    def search(self, word):
        dictionary = OxfordDictionary()
        results = dictionary.search_word(word)
        
        return results

    def test_search(self):
        word = "roughly"
        print(f"Search a word: {word}")
        results = self.search(word)
        print("\nResult")
        for result in results:
            WordDisplayer.show(result)

    def test_cannot_search(self):
        word = "auxilary"
        print(f"Search for non-existence: {word}")
        results = self.search(word)
        self.assertIsNone(results)
