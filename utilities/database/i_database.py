from abc import ABC, abstractclassmethod, abstractproperty


class IDatabase(ABC):
    @abstractclassmethod
    def load(cls, date):
        pass

    @abstractclassmethod
    def save(cls, word):
        pass

    @abstractclassmethod
    def save_to_review(cls, word):
        pass

    @abstractclassmethod
    def save_today_info(cls, today_file):
        pass
