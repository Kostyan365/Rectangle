import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)  # Загружаем дизайн
        self.setWindowTitle('Git и желтые окружности')
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
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        x1 = random.randrange(0, self.width)
        y2 = random.randrange(0, self.height)
        z = random.randrange(5, 100)
        qp.drawEllipse(x1, y2, z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
