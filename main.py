import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSlider, QLineEdit
from PyQt5.QtCore import Qt

class ColorChanger(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Changer')
        layout = QVBoxLayout()

        # Create RGB sliders
        self.red_slider = QSlider(Qt.Horizontal)
        self.red_slider.setMaximum(255)
        self.red_slider.valueChanged.connect(self.update_color)
        layout.addWidget(self.red_slider)

        self.green_slider = QSlider(Qt.Horizontal)
        self.green_slider.setMaximum(255)
        self.green_slider.valueChanged.connect(self.update_color)
        layout.addWidget(self.green_slider)

        self.blue_slider = QSlider(Qt.Horizontal)
        self.blue_slider.setMaximum(255)
        self.blue_slider.valueChanged.connect(self.update_color)
        layout.addWidget(self.blue_slider)

        # Create text inputs for RGB values
        self.red_input = QLineEdit()
        self.red_input.textChanged.connect(self.update_slider)
        layout.addWidget(self.red_input)

        self.green_input = QLineEdit()
        self.green_input.textChanged.connect(self.update_slider)
        layout.addWidget(self.green_input)

        self.blue_input = QLineEdit()
        self.blue_input.textChanged.connect(self.update_slider)
        layout.addWidget(self.blue_input)

        # Create color preview label
        self.color_label = QLabel()
        self.update_color()
        layout.addWidget(self.color_label)

        self.setLayout(layout)

    def update_color(self):
        # Get RGB values from sliders
        red = self.red_slider.value()
        green = self.green_slider.value()
        blue = self.blue_slider.value()

        # Set RGB values to text inputs
        self.red_input.setText(str(red))
        self.green_input.setText(str(green))
        self.blue_input.setText(str(blue))

        # Set background color of color preview label
        self.color_label.setStyleSheet(f'background-color: rgb({red}, {green}, {blue});')

    def update_slider(self):
        # Get RGB values from text inputs
        red = int(self.red_input.text()) if self.red_input.text().isdigit() else 0
        green = int(self.green_input.text()) if self.green_input.text().isdigit() else 0
        blue = int(self.blue_input.text()) if self.blue_input.text().isdigit() else 0

        # Set RGB values to sliders
        self.red_slider.setValue(red)
        self.green_slider.setValue(green)
        self.blue_slider.setValue(blue)

        # Set background color of color preview label
        self.color_label.setStyleSheet(f'background-color: rgb({red}, {green}, {blue});')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChanger()
    window.show()
    sys.exit(app.exec_())

    sys.exit(app.exec_())
