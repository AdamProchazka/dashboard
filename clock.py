from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QColor
from PyQt5 import QtCore
import sys

class Clock(QLCDNumber):
    def __init__(self):
        super().__init__()

        title = "Clock"
        top = 400
        left = 400
        width = 450
        height = 300

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
                                   
        palete = self.palette()

        palete.setColor(palete.WindowText, QColor(255,255, 255))
        palete.setColor(palete.Background, QColor(0, 0, 0))
		
        self.setPalette(palete)

        self.setSegmentStyle(QLCDNumber.Filled)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if(time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)

app = QApplication(sys.argv)
clock = Clock()
clock.showFullScreen()
app.exec()

