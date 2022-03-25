from abc import ABC, abstractclassmethod, abstractproperty


class IDatabase(ABC):
    @abstractclassmethod
    def load(cls, date):
        pass

    @abstractclassmethod
    def save(cls, word):
        pass
