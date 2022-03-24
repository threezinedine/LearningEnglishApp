import os
from .i_loader import ILoader
from ..date import convert_date_2_str
from ..file import get_list_file_paths
from data import Word, WordType, Sense


DIVIDER = ":;"
DATABASE = "database"


class WordLoader(ILoader):
    """
        Class loads word from the date_time
    """
    @classmethod
    def __load_word(cls, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read()

        rows = data.split('\n')
        rows = rows[:-1]

        word, type_str, ipa, sound = rows[0].split(DIVIDER)

        word_type = WordType.return_type(type_str)
        senses = []

        for i in range(1, 4):
            definition, example, my_example = rows[i].split(DIVIDER)
            sense = Sense(definition, example)
            sense.add_new_example(my_example)

            senses.append(sense) 

        return Word(1, word, word_type, ipa, sound, senses)


    def load(cls, date):
        """
            Load words from the date information

            Paramters
            ---------
                date: python datetime
        """
        folder = os.path.join(DATABASE, convert_date_2_str(date, divide_str='_'))
        files = get_list_file_paths(folder)
        words = []

        for file in files: 
            word = cls.__load_word(file)
            words.append(word)

        return words
