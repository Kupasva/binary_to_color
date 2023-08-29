from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Opacity Setting Example")
        
        # Create a layout and widget
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        # Create a label and line edit for opacity input
        opacity_label = QLabel("Opacity (0.0 - 1.0):")
        layout.addWidget(opacity_label)
        
        self.opacity_line_edit = QLineEdit()
        layout.addWidget(self.opacity_line_edit)
        
        # Connect a slot to handle opacity input changes
        self.opacity_line_edit.textChanged.connect(self.update_opacity)
        
        # Show the main window
        self.show()
    
    def update_opacity(self, text):
        try:
            opacity = float(text)
            self.setWindowOpacity(opacity)
        except ValueError:
            # Handle invalid input, e.g., non-numeric values
            pass

# Create the application
app = QApplication([])
window = MainWindow()

# Run the application
app.exec_()
