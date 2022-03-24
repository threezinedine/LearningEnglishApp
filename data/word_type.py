from enum import Enum, auto


class WordType(Enum):
    """
        The type of the word.
    """
    Noun = "noun"
    Verb = "verb"
    Adjective = "adjective"
    Adverb = "abverb"
    Empty = ""

    def return_type(type_str):
        type_str = type_str.lower()

        for word_type in WordType:
            if type_str == word_type.value:
                return word_type

        return WordType.Empty
