from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit
from functools import partial
from threading import Thread
from PyQt5 import uic
from utilities import get_full_path, play_url
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

        self.match_results = self.findChild(QVBoxLayout, 'match_results')

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

        self.my_example_1 = self.findChild(QLineEdit, 'my_example_1')
        self.my_example_2 = self.findChild(QLineEdit, 'my_example_2')
        self.my_example_3 = self.findChild(QLineEdit, 'my_example_3')

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
                "word_type": self.word_type_label,
                "sound": "",
                "senses": senses
                }
        return frames_dict

    def reset_frames(self):
        self.word_label.setText("")
        self.pronunciation_label.setText("")
        self.word_type_label.setText("")
        self.definition_1.setText("")
        self.definition_2.setText("")
        self.definition_3.setText("")

        self.example_1.setText("")
        self.example_2.setText("")
        self.example_3.setText("")

        self.my_example_1.setText("")
        self.my_example_2.setText("")
        self.my_example_3.setText("")

    def init(self):
        uic.loadUi(get_full_path(__file__, SEARCH_WIDGET_UI), self)
        self.setGeometry(50, 50, 1000, 900)

    def __play_sound(self):
        play_url(self.current_word['sound'])

    def __save(self):
        if self.current_word is None:
            pass
        else:
            for index, my_example in enumerate([self.my_example_1, self.my_example_2, self.my_example_3]):
                if index < len(self.current_word.properties['senses']):
                    if my_example.text() != "":
                        self.current_word.properties['senses'][index]['my_example'] = my_example.text()

            Database().save(self.current_word)

    def click_search_button(self):
        thread = Thread(target=self.__search, args=())
        thread.start()

    def __remove_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.removeItem(layout.itemAt(i))

    def __show__word(self, words, index=0):
        self.reset_frames()
        if words is not None:
            self.graphic_displayer.show(words[index])
            self.__remove_layout(self.match_results)
            self.current_word = words[index]
            self.__save()

            for i in range(len(words)):
                other_button = QPushButton(f"{words[i]['word']}({words[i]['word_type']})")
                other_button.clicked.connect(partial(self.__show__word, words, i))
                self.match_results.addWidget(other_button) 

    def __search(self):
        words = self.dict.search_word(self.search_line.text())
        self.__show__word(words)
