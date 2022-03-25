import unittest
import json
import os
from data import Word, WordType, Sound
from utilities.display import WordDisplayer
from utilities.database import Database
from utilities import get_k_previous_date


class WordTest(unittest.TestCase):
    def initial_sense(self, definition, example):
        print(f"\tDefinition: {definition}\n\tExample: {example}")
        return {"definition": definition, "example": example, "my_example": ""}

    def initial_senses(self):
        definition_1 = "The definition 1"
        use_1 = "This is first use."

        definition_2 = "The definition 2"
        use_2 = "This is second use."
        senses = [self.initial_sense(definition_1, use_1), self.initial_sense(definition_2, use_2)]
        return senses

    def initial_word(self):
        senses = self.initial_senses()

        word = "hello"
        ipa = ""
        sound_url = "https://zalo.test"
        word_type = WordType.Noun
        
        print(f"Initial word: \n\tWord: {word}\n\tWord Type: {word_type.value}\n\tIpa: {ipa}")
        properties = {
                "word": word, 
                "word_type": word_type.value,
                "ipa": ipa,
                "sound": sound_url,
                "senses": senses
                }
        word = Word(properties)
        return word

    def test_save_load(self):
        word = self.initial_word()
        Database().save(word)

        words = Database().load(get_k_previous_date())

        print("Print loaded words: ")
        for word in words:
            WordDisplayer().show(word)

    def test_diplayer(self):
        word = self.initial_word()

        WordDisplayer().show(word)
