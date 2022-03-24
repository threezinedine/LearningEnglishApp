from abc import abstractstaticmethod, ABC


class IDisplay(ABC):
    @abstractstaticmethod
    def show(word):
        pass
