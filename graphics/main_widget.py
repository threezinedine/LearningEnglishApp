from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5 import uic
from utilities import get_full_path, get_file_folder
import os
from .search_widget import MySearchWidget
from .review_widget import ReviewWidget


MAIN_WIDGET_UI = "ui_files\\main_widget.ui"


class MyMainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi(get_full_path(__file__, MAIN_WIDGET_UI), self)

        self.search_widget_button = self.findChild(QPushButton, 'search_button')
        self.search_widget_button.clicked.connect(self.click_search)

        self.review_widget_button = self.findChild(QPushButton, 'review_button')
        self.review_widget_button.clicked.connect(self.click_review)

        self.search_win = MySearchWidget()
        self.review_win = ReviewWidget()

    def click_search(self):
        self.search_win.show()

    def click_review(self):
        self.review_win.show()
