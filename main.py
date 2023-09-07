import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me!")
        button.setChecked(True)
        button.clicked.connect(self.the_button_was_clicked)

        # set the central widget of the window
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("Clicked")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()