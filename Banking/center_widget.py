import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window size to fit the screen
        self.setGeometry(0, 0, self.screen().geometry().width(), self.screen().geometry().height())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
##Upside code is to adjust the main window to the screen size
##Below code is to set the widget to the ccenter of the screen


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class CenterWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the widget size
        self.setGeometry(0, 0, 300, 200)

        # Center the widget on the screen
        self.center()

    def center(self):
        # Get the screen geometry
        screen_geometry = QDesktopWidget().screenGeometry()

        # Calculate the center point
        center_point = screen_geometry.center()

        # Move the widget to the center
        self.move(center_point.x() - self.width() / 2, center_point.y() - self.height() / 2)

app = QApplication(sys.argv)
widget = CenterWidget()
widget.show()
sys.exit(app.exec_())
