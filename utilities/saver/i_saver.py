from abc import ABC, abstractclassmethod


class ISaver(ABC):
    @abstractclassmethod
    def save(cls, word):
        pass
