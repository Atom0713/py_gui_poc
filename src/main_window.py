import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Qt
from progress_window import ProgressWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Antalya Vandals")

        self.instalButton = QPushButton("Install", self)
        self.instalButton.move(380, 550)
        self.instalButton.clicked.connect(self.progress_window)

        self.close_button = QPushButton("Close", self)
        self.close_button.move(490, 550)
        self.close_button.clicked.connect(self.close_app)

        self.label = QLabel("Welcome. To start press `Install`.", self)
        self.label.setGeometry(200,250,200,50)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setGeometry(100, 100, 600, 600)
        self.show()

    def close_app(self):
        sys.exit()

    def progress_window(self):
        self.progress_window = ProgressWindow()
        self.hide()
        self.progress_window.show()
