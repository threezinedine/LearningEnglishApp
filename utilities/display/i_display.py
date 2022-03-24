from abc import abstractclassmethod, ABC


class IDisplay(ABC):
    @abstractclassmethod
    def show(cls, word):
        pass
