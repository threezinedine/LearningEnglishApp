from abc import ABC, abstractclassmethod, abstractproperty


class IDatabase(ABC):
    @abstractproperty
    def folder(self):
        pass

    @abstractclassmethod
    def load(self, date):
        pass
