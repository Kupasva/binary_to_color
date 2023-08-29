import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QLabel

class GridWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a scroll area widget
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to contain the grid layout
        widget = QWidget(scroll_area)
        scroll_area.setWidget(widget)

        # Create a grid layout
        grid_layout = QGridLayout(widget)

        # Add labels to the grid layout
        for i in range(10):
            for j in range(10):
                label = QLabel(f'Label {i}-{j}')
                grid_layout.addWidget(label, i, j)

        # Set the scroll area as the main layout of the window
        self.setLayout(QGridLayout())
        self.layout().addWidget(scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec_())
