from PySide6.QtWidgets import QMainWindow, QProgressBar, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
import os


class ProgressWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Installing...")
        self.setGeometry(100, 100, 600, 600)

        self.progress_bar = QProgressBar(self, minimum=0, maximum=100, textVisible=False,
                        objectName="BlueProgressBar")
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
       #  self.progress_bar.setGeometry(100, 50, 300, 100)
        self.resize(300, 100)
        self.progress_bar.setValue(0)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.progress_bar)
        self.setLayout(self.vbox)

        self.show()

        timer = QTimer(self)
        timer.timeout.connect(self.progress)
        timer.start(1000)

    def progress(self):
        self.progress_bar.setValue(self.progress_bar.value()+10)
        if self.progress_bar.value() == 50:
            os.system("gnome-terminal -e 'bash -c \"MY_COMMAND; sleep 1000000\" '")
            
