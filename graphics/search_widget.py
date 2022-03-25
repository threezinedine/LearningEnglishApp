from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit
from PyQt5 import uic
from utilities import get_full_path
from utilities.display import GraphicDisplayer
import os
from time import sleep
from search_engine import OxfordDictionary
from utilities.database import Database


SEARCH_WIDGET_UI = "ui_files\\search_widget.ui"


class MySearchWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init()

        self.sound_button = self.findChild(QPushButton, 'sound_button')
        self.sound_button.clicked.connect(self.__play_sound)

        self.search_line = self.findChild(QLineEdit, 'search_line')
        self.search_button = self.findChild(QPushButton, 'search_button')
        self.search_button.clicked.connect(self.__search)

        self.save_button = self.findChild(QPushButton, 'save_button')
        self.save_button.clicked.connect(self.__save)

        self.word_label = self.findChild(QLabel, 'word_label')
        self.pronunciation_label = self.findChild(QLabel, 'pronunciation_label')
        self.word_type_label = self.findChild(QLabel, 'word_type_label')

        self.definition_1 = self.findChild(QLabel, 'definition_label_1')
        self.definition_2 = self.findChild(QLabel, 'definition_label_2')
        self.definition_3 = self.findChild(QLabel, 'definition_label_3')

        self.example_1 = self.findChild(QLabel, 'example_label_1')
        self.example_2 = self.findChild(QLabel, 'example_label_2')
        self.example_3 = self.findChild(QLabel, 'example_label_3')

        self.my_example_1 = self.findChild(QLineEdit, 'my_example_label_1')
        self.my_example_2 = self.findChild(QLineEdit, 'my_example_label_2')
        self.my_example_3 = self.findChild(QLineEdit, 'my_example_label_3')

        self.sense_3 = self.findChild(QVBoxLayout, 'sense_3')

        self.dict = OxfordDictionary()
        self.frames_dict = self.initial_frame_dict()
        self.graphic_displayer = GraphicDisplayer(self.frames_dict)

        self.current_word = None


    def initial_sense(self, definition, example, my_example):
        return {
                "definition": definition,
                "example": example,
                "my_example": my_example
                }
    

    def initial_frame_dict(self):
        senses = [self.initial_sense(self.definition_1, self.example_1, self.my_example_1), 
                 self.initial_sense(self.definition_2, self.example_2, self.my_example_2),
                 self.initial_sense(self.definition_3, self.example_3, self.my_example_3)]
        frames_dict = {
                "word": self.word_label,
                "ipa": self.pronunciation_label,
                "word_type": self.word_label,
                "sound": "",
                "senses": senses
                }

    def init(self):
        uic.loadUi(get_full_path(__file__, SEARCH_WIDGET_UI), self)

    def __play_sound(self):
        print("sound is playing ...")
        sleep(1)
        print("done.")

    def __save(self):
        if self.current_word is None:
            pass
        else:
            pass

    def __search(self):
        words = self.dict.search_word(self.search_line.text())
        if words is not None:
            self.graphic_displayer.show(words[0])
