from .sound import Sound


class Word:
    """
        The class stores all information of the word (include ipa, ...)

        Parameters
        ----------
            id: int 
                The id of the word
            
            word: string 
                The word 

            ipa: string 
                The pronunciation with ipa format

            sound: Sound 
                The sound object that store sound of the word

            senses: Sense[*]
                The sense object that how people use the word
    """
    def __init__(self, word_id, word, word_type, ipa,
            sound, senses):
        self.__id = word_id
        self.__word = word
        self.__word_type = word_type
        self.__ipa = ipa
        self.__sound = Sound(sound)
        self.__senses = senses

    @property
    def id(self):
        return self.__id 

    @property
    def word(self):
        return self.__word

    @property
    def word_type(self):
        return self.__word_type

    @property
    def ipa(self):
        return self.__ipa

    @property
    def sound(self):
        return self.__sound

    @property
    def senses(self):
        return self.__senses
