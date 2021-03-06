import os
import json
from data import Word, TodayFile
from .i_database import IDatabase
from ..file import create_folder_if_not_exist, get_list_file_paths
from ..date import get_k_previous_date


class Database(IDatabase):
    base_folder = "database"
    review_folder = "review"

    create_folder_if_not_exist(base_folder)
    create_folder_if_not_exist(os.path.join(base_folder, review_folder))

    def __init__(self):
        today_folder = get_k_previous_date()
        self.__folder = os.path.join(self.base_folder, today_folder)     
        create_folder_if_not_exist(self.__folder)

    def save(cls, word, review=False):
        """
            Method receives the word and save it into the database.

            Parameters
            ----------
                word: Word object
        """

        # get current date (the name of the folder store all words searched in the day) 
        # and make full current date folder
        # ex: database\\25_03_2020
        today_folder = get_k_previous_date(divide_str='_')
        if not review:
            full_path_folder = os.path.join(cls.base_folder, today_folder)
        else:
            full_path_folder = os.path.join(cls.base_folder, cls.review_folder) 
        create_folder_if_not_exist(full_path_folder)

        # the file has the name format as {word}_{word_type}. Ex: cat_noun
        word_file_path = os.path.join(full_path_folder, f"{word['word']}_{word['word_type']}")

        # save the word by convert to the json string
        with open(word_file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(word.properties))

    @classmethod
    def __load_word(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.loads(file.read())

        return Word.word_from(data)

    def load(cls, date):
        """
            Method receives the formatted date and get all words that searched in that day.

            Parameters
            ----------
                date: formatted date. Ex, 25_03_2020 
                    The date that all needed words stored.

            Returns
            -------
                Word[*]:
                    All words that stored in the day that give in. 
        """
        words = []

        create_folder_if_not_exist(os.path.join(cls.base_folder, date))
        
        files = get_list_file_paths(os.path.join(cls.base_folder, date))
        for file in files:
            words.append(cls.__load_word(file))

        return words

    def load_review_word(cls, word_str):
        today_file = get_k_previous_date() 
        if os.path.isfile(os.path.join(cls.base_folder, cls.review_folder, word_str)):
            return cls.__load_word(os.path.join(cls.base_folder, cls.review_folder, word_str))

    def save_today_info(cls, today_file):
        file = get_k_previous_date()
        with open(os.path.join(cls.base_folder, cls.review_folder, file), 'w', encoding='utf-8') as f:
            f.write(json.dumps(today_file.properties))

    def has_today_info(cls):
        today_file = get_k_previous_date() 
        return os.path.isfile(os.path.join(cls.base_folder, cls.review_folder, today_file))

    def load_today_file(cls):
        file = get_k_previous_date()
        with open(os.path.join(cls.base_folder, cls.review_folder, file), 'r', encoding='utf-8') as f:
            today_file = TodayFile(json.loads(f.read()))

        return today_file

    def clear_review_folder(cls):
        today_file = get_k_previous_date()

        files = get_list_file_paths(os.path.join(cls.base_folder, cls.review_folder))

        for file in files:
            if file != os.path.join(cls.base_folder, cls.review_folder, today_file):
                os.remove(file)
