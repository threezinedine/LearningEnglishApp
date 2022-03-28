from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5 import uic
from utilities.display import GraphicDisplayer
from utilities.database import Database
from data import ReviewRule, TodayFile, Sound
from utilities import expand_arr


class ReviewWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.today_file = None
        self.current_word = None
        self.sound = None
        self.initUI()

        self.next_button = self.findChild(QPushButton, 'next_button')
        self.next_button.clicked.connect(self.__click_next_button)

        self.sound_buton = self.findChild(QPushButton, 'sound_button')
        self.sound_buton.clicked.connect(self.__click_sound_button)

        self.word_label = self.findChild(QLabel, 'word_label')
        self.word_type_label = self.findChild(QLabel, 'word_type_label')
        self.ipa = self.findChild(QLabel, 'ipa_label')

        self.definition_label_1 = self.findChild(QLabel, 'definition_label_1')
        self.definition_label_2 = self.findChild(QLabel, 'definition_label_2')
        self.definition_label_3 = self.findChild(QLabel, 'definition_label_3')

        self.example_label_1 = self.findChild(QLabel, 'example_label_1')
        self.example_label_2 = self.findChild(QLabel, 'example_label_2')
        self.example_label_3 = self.findChild(QLabel, 'example_label_3')

        self.my_example_label_1 = self.findChild(QLabel, 'my_example_label_1')
        self.my_example_label_2 = self.findChild(QLabel, 'my_example_label_2')
        self.my_example_label_3 = self.findChild(QLabel, 'my_example_label_3')
        
        self.graphic_displayer = GraphicDisplayer(self.__graphic_dict())

    def __graphic_sense(self, definition, example, my_example):
        return {
                "definition": definition,
                "example": example,
                "my_example": my_example
                }

    def __graphic_dict(self):
        return {
                "word": self.word_label,
                "word_type": self.word_type_label,
                "ipa": self.ipa_label,
                "senses": [self.__graphic_sense(self.definition_label_1, self.example_label_1, self.my_example_label_1),
                    self.__graphic_sense(self.definition_label_2, self.example_label_2, self.my_example_label_2),
                    self.__graphic_sense(self.definition_label_3, self.example_label_3, self.my_example_label_3)]
                }

    def create_today_file(self):
        review_dates = ReviewRule().get_reviewed_dates()
        all_words = []
        for date in review_dates:
            words = Database().load(date)
            for word in words:
                Database().save(word, review=True)
                all_words.append(f"{word['word']}_{word['word_type']}")

        all_words = expand_arr(all_words)

        self.today_file = TodayFile({"words": all_words, "review_done": False})
        Database().save_today_info(self.today_file)
        
    def initUI(self):
        uic.loadUi('graphics/ui_files/review_widget.ui', self)
        self.setGeometry(50, 50, 1000, 600)

        if Database().has_today_info():
            self.today_file = Database().load_today_file()
        else:
            self.create_today_file()

    def __click_next_button(self):
        if not self.today_file.has_review_done():
            self.current_word = Database().load_review_word(self.today_file.get_word())
            self.graphic_displayer.show(self.current_word)
            self.__click_sound_button()
            Database().save_today_info(self.today_file)
        else:
            Database().clear_review_folder()

    def __click_sound_button(self):
        if self.current_word is not None:
            self.sound = Sound(self.current_word['sound'])
            self.sound.play()

