from PySide6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton
from PySide6.QtCore import Qt, Slot
import sys

@Slot()
def close_app():
    sys.exit()


app = QApplication([])

### Label
label = QLabel("Welcome!")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

### Button
install_button = QPushButton("Install")
close_button = QPushButton("Close")
close_button.clicked.connect(close_app)

### Window
window = QWidget()
window.resize(600, 600)
window.setWindowTitle("Antalya Vandals")

### Layout
layout = QGridLayout(window)
layout.addWidget(label, 0, 0, 0, 2)
layout.addWidget(close_button, 1, 0, Qt.AlignmentFlag.AlignBottom)
layout.addWidget(install_button, 1, 1, Qt.AlignmentFlag.AlignBottom)

window.show()
app.exec()

