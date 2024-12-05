import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
import random


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.button = QPushButton("Add Circle", self)
        self.button.clicked.connect(self.add_circle)
        self.layout.addWidget(self.button)

        self.circles = []

    def add_circle(self):
        radius = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(0, self.width() - radius)
        y = random.randint(0, self.height() - radius)
        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, radius, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
