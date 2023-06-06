from PySide6.QtWidgets import QMainWindow


class ProgressWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Installing...")
        self.setGeometry(100, 100, 600, 600)
        self.show()