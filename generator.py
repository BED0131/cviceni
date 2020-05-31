from numpy.random import randint
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import QSize, Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center: Point, width: int, height: int):
        self.center = center
        self.width = width
        self.height = height


class Generator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.point = bod
        self.setMinimumSize(QSize(800, 600))
        self.setWindowTitle("Generátor")

        buttonGeneruj = QPushButton('Generuj', self)
        buttonGeneruj.clicked.connect(self.drawCircle)
        buttonGeneruj.resize(100, 50)
        buttonGeneruj.move(10, 10)
        self.circle = None

    def drawCircle(self):
        for n in range(0, pocet):
            self.circle = kruh
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        QMainWindow.paintEvent(self, event)

        for i in range(0, pocet):
            bod = Point(randint(20, 780, 1), randint(20, 580, 1))

            if self.circle is not None:
                self.point = bod
                brush = QBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), Qt.SolidPattern)
                painter.setBrush(brush)
                painter.drawEllipse(QPoint(self.point.x, self.point.y), self.circle.width, self.circle.height)


pocet = 10
bod = Point(randint(20, 780, 1), randint(20, 580, 1))
kruh = Circle(bod, 10, 10)
app = QApplication(sys.argv)
mainWin = Generator()
mainWin.show()
sys.exit(app.exec_())
