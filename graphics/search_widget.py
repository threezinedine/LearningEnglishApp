from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit
from PyQt5 import uic
from utilities import get_full_path
from utilities.display import GraphicDisplayer
import os
from time import sleep
from search_engine import OxfordDictionary


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

        self.word_label = self.findChild(QLabel, 'word_label')
        self.pronounciation_label = self.findChild(QLabel, 'pronounciation_label')

        self.definition_1 = self.findChild(QLabel, 'definition_label_1')
        self.definition_2 = self.findChild(QLabel, 'definition_label_2')
        self.definition_3 = self.findChild(QLabel, 'definition_label_3')

        self.sentence_1 = self.findChild(QLabel, 'sentence_label_1')
        self.sentence_2 = self.findChild(QLabel, 'sentence_label_2')
        self.sentence_3 = self.findChild(QLabel, 'sentence_label_3')

        self.sense_3 = self.findChild(QVBoxLayout, 'sense_3')

        self.dict = OxfordDictionary()
        self.graphic_displayer = GraphicDisplayer(self.word_label, self.pronounciation_label,
                    [self.definition_1, self.definition_2, self.definition_3],
                    [self.sentence_1, self.sentence_2, self.sentence_3])

    def init(self):
        uic.loadUi(get_full_path(__file__, SEARCH_WIDGET_UI), self)

    def __play_sound(self):
        print("sound is playing ...")
        sleep(1)
        print("done.")

    def __add_sense(self, sense_data, sense):
        definition_label = QLabel(f"Definition: {sense_data['definition']}")
        sentence = QLabel(f"Sentence: {sense_data['sentence']}")
        my_example = QLabel("My Example: ")
        my_sentence = QLineEdit()
        layout = QHBoxLayout()
        layout.addWidget(my_example)
        layout.addWidget(my_sentence)
        sense.addWidget(definition_label)
        sense.addWidget(sentence)
        sense.addLayout(layout)

    def __search(self):
        words = self.dict.search_word(self.search_line.text())
        if words is not None:
            self.graphic_displayer.show(words[0])
