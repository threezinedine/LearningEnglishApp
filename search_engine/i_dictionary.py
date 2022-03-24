from abc import ABC, abstractclassmethod


class IDictionary(ABC):
    @abstractclassmethod
    def search_word(cls, word):
        pass
