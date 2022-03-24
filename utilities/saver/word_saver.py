from .i_saver import ISaver
from ..date import get_current_date_str
from ..file import create_folder_if_not_exist
import os 


DIVIDER = ":;"


class WordSaver(ISaver):
    """
        Class saves the Word objects to database (in folder that has the searched date)
    """
    def save(cls, word):
        """
            Save the Word into the current date folder.

            Paramters
            ---------
                word: Word object
                    The word that needed to store.

                writing_mode: string, default: w
                    The writing mode in save the word into the database, 'w' will overide the data
        """
        current_date = get_current_date_str()
        create_folder_if_not_exist(current_date)
        file_name = os.path.join(current_date, f"{word.word}_{word.word_type.value}.txt")

        save_string = ""
        save_string = DIVIDER.join([word.word, word.word_type.value, word.ipa, word.sound.url])
        save_string += "\n"

        for sense in word.senses:
            save_string += DIVIDER.join([sense.definition, sense.example, sense.my_example])
            save_string += "\n"

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(save_string)
