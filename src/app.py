import sys
from main_window import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_window = MainWindow()
    sys.exit(app.exec())