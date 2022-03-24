from abc import ABC, abstractclassmethod


class ILoader(ABC):
    @abstractclassmethod
    def load(cls, date):
        pass
