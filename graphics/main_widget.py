from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from utilities import get_full_path, get_file_folder
import os


MAIN_WIDGET_UI = "ui_files\\main_widget.ui"


class MyMainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi(get_full_path(__file__, MAIN_WIDGET_UI), self)
