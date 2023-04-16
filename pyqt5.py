from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings, QVariant
from PyQt5.QtWidgets import *
import sys
from facts import facts

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("Test")
        self.initUI()

    def initUI(self):

        # Create the checkboxes for each subject
        self.checkboxes = {}
        subjects = ['History', 'Sports', 'Science', 'Technology', 'Geography', 'Animals', 'Food', 'Art', 'Music', 'Literature']
        for i, subject in enumerate(subjects):
            checkbox = QCheckBox(subject)
            checkbox.setObjectName(subject)
            checkbox.setChecked(False)
            checkbox.stateChanged.connect(self.updateSettings)
            self.checkboxes[subject] = checkbox

        # Add the checkboxes to a layout
        layout = QVBoxLayout()
        for checkbox in self.checkboxes.values():
            layout.addWidget(checkbox)

        # Add the layout to a widget and set it as the central widget of the window
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Load the initial settings
        self.loadSettings()


    def clicked(self):
        self.label.setText("You pressed the buton")
        self.update()

    def update(self):
        self.label.adjustSize()



    def loadSettings(self):
        # Load the settings from the INI file
        self.settings = QSettings('./settings.ini', QSettings.IniFormat)
        subjects = self.settings.value('Subjects', [])

        # Update the checkboxes based on the loaded settings
        for subject, checkbox in self.checkboxes.items():
            try:
                checkbox.setChecked(subject in subjects)
            except:
                continue

    def updateSettings(self):
        # Get the list of checked subjects
        checked_subjects = [subject for subject, checkbox in self.checkboxes.items() if checkbox.isChecked()]

        # Update the settings in the INI file
        self.settings.setValue('Subjects', checked_subjects)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    def moveWindowToCenter(win):
        # Get the size of the screen
        screen_size = QDesktopWidget().screenGeometry(-1)

        # Calculate the center of the screen
        center_x = (screen_size.width() - win.frameSize().width()) // 2
        center_y = (screen_size.height() - win.frameSize().height()) // 2

        # Move the window to the center of the screen
        win.move(center_x, center_y)
    
    moveWindowToCenter(win)


    win.show()
    sys.exit(app.exec_())

window()