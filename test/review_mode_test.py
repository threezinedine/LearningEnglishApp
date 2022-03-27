from utilities.database import Database
import os
from utilities.display import WordDisplayer
from search_engine import OxfordDictionary
from utilities import get_k_previous_date, get_list_file_paths
import unittest


class ReviewModeTest(unittest.TestCase):
    word = "velocity"

    def test_save_word_in_review(self):
        print(f"Search for {self.word}")

        words = OxfordDictionary().search_word(self.word)

        if words is not None:
            Database().save(words[0], review=True)

        print("Review loadede test:")

        today_file = get_k_previous_date()
        word = Database().load_review_word("velocity_noun")
        WordDisplayer().show(word)
