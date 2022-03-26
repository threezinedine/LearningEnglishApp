from data import ReviewRule
import unittest
from utilities import get_k_previous_date


class ReviewRuleTest(unittest.TestCase):
    def test_generate_reviewed_dates(self):
        folder_names = ReviewRule().get_reviewed_dates()  
        print(f"Current date folder: {get_k_previous_date()}")
        print(f"The result: \n\t{', '.join(folder_names)}")
