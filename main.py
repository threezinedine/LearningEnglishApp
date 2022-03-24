import sys
from graphics import MyMainWidget, MySearchWidget
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv) 
    win = MySearchWidget()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
