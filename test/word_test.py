import unittest
from data import Word, WordType, Sound, Sense
from utilities.display import WordDisplayer


class WordTest(unittest.TestCase):
    def initial_senses(self):
        definition_1 = "The definition 1"
        use_1 = "This is first use."

        definition_2 = "The definition 2"
        use_2 = "This is second use."
        print(f"Initial two senses: \n\tDefinition: {definition_1}\n\tUse: {use_1}")
        print(f"\n\n\tDefinition: {definition_1}\n\tUse: {use_2}")
        senses = [Sense(definition_1, use_1), Sense(definition_2, use_2)]
        return senses

    def initial_word(self):
        senses = self.initial_senses()

        word_id = 1
        word = "hello"
        ipa = ""
        sound_url = "https://zalo.test"
        word_type = WordType.Noun
        
        print(f"Initial word: \n\tId: {word_id}\n\tWord: {word}\n\tIpa: {ipa}")
        word = Word(word_id=word_id, word=word, word_type=word_type, ipa=ipa, sound=sound_url, senses=senses)
        return word

    def test_add_example(self):
        word = self.initial_word()
        
        my_example = "My example"
        print(f"Add new example in first sense ({my_example})")
        word.senses[0].add_new_example(my_example)

        print("Result")
        WordDisplayer.show(word)        
