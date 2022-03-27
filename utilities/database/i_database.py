from abc import ABC, abstractclassmethod, abstractproperty


class IDatabase(ABC):
    @abstractclassmethod
    def load(cls, date):
        pass

    @abstractclassmethod
    def save(cls, word):
        pass

    @abstractclassmethod
    def load_review_word(cls, word_str):
        pass

    @abstractclassmethod
    def save_today_info(cls, today_file):
        pass

    @abstractclassmethod
    def has_today_info(cls):
        pass

    @abstractclassmethod
    def load_today_file(cls):
        pass 
