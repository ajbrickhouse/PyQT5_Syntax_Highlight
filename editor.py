import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5 import QtGui
from syntax import PythonHighlighter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QTextEdit widget and set it as the central widget
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        # set the font size to 12
        font = QtGui.QFont("Consolas", 12)
        self.text_edit.setFont(font)
        # disable word wrap
        self.text_edit.setLineWrapMode(QTextEdit.NoWrap)
        # set background color to black
        self.text_edit.setStyleSheet("background-color: black; color: white;")
        # read the file test.py
        with open("syntax.py", "r") as f:
            self.text_edit.setText(f.read())
        # Apply syntax highlighting to the QTextEdit widget
        self.highlighter = PythonHighlighter(self.text_edit.document())
        # Set the window properties
        self.setWindowTitle("Python Syntax Highlighting")
        self.setGeometry(100, 100, 1000, 1500)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
