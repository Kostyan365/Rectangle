import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QRect


class Ui_Form(object):
    def __init__(self):
        self.centralWidget = None
        self.pushButton = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 391)
        self.centralWidget = QWidget(MainWindow)
        self.pushButton = QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QRect(190, 360, 75, 23))
        self.pushButton.setText('старт')
        MainWindow.setCentralWidget(self.centralWidget)


class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.width, self.height = self.size().width(), self.size().height()
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        x1 = random.randrange(0, self.width)
        y2 = random.randrange(0, self.height)
        z = random.randrange(5, 100)
        color = QColor(r, g, b)
        qp.setBrush(QBrush(color, Qt.SolidPattern))
        qp.drawEllipse(x1, y2, z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
