import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from subprocess import Popen

class FileRunnerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create buttons
        btn_run_file1 = QPushButton('Run Test file', self)
        btn_run_file2 = QPushButton('Run Test1 file', self)

        # Connect buttons to functions
        btn_run_file1.clicked.connect(self.run_file1)
        btn_run_file2.clicked.connect(self.run_file2)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(btn_run_file1)
        layout.addWidget(btn_run_file2)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setGeometry(300, 300, 500, 200)  # Adjust the size of the window
        self.setWindowTitle('File Runner App')

        # Add some styling
        self.setStyleSheet("""
            FileRunnerApp {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                height: 40px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def run_file1(self):
        # File name in the quotation to be run
        process = Popen(['python', 'test.py'])

    def run_file2(self):
        # File name in the quotation
        process = Popen(['python', 'test1.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileRunnerApp()
    ex.show()
    sys.exit(app.exec_())
