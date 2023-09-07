import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
    #
    #    # self.button_is_checked = True
    #
    #     self.setWindowTitle("My App")
    #
    #     self.button = QPushButton("Press me!")
    #     self.button.clicked.connect(self.the_button_was_clicked)
    #     # self.button.setCheckable(True)
    #     # self.button.released.connect(self.the_button_was_released)
    #     # self.button.setChecked(self.button_is_checked)
    #
    #
    #     # set the central widget of the window
    #     self.setCentralWidget(self.button)
    # # def the_button_was_clicked(self):
    # #     print("Clicked!")
    #
    # # def the_button_was_released(self):
    # #     self.button_is_checked = self.button.isChecked()
    # #     print(self.button_is_checked)
    # def the_button_was_clicked(self):
    #     self.toolButtonStyleChanged.setText("You already clicked me.")
    #     self.button.setEnabled(False)
    #
    #     # also change the window title
    #     self.setWindowTitle("My Oneshot App")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("My Oneshot App")
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()