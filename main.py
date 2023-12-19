from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.set()
        self.initUI()
        self.connects()

    def set(self):
        self.setWindowTitle("Конвертатор")
        self.show()

    def initUI(self):
        text1 = QLabel("Введите температуру в градусах Цельсия:")
        self.input1 = QLineEdit("")
        self.button1 = QPushButton("Отправить")
        self.button2 = QPushButton("Отправить")
        text2 = QLabel("В градусах Фаренгейта:")
        self.input2 = QLineEdit()
        line = QVBoxLayout()
        line1 = QVBoxLayout()
        line2 = QHBoxLayout()
        line.addWidget(text1, alignment=Qt.AlignLeft)
        line.addWidget(self.input1, alignment=Qt.AlignLeft)
        line.addWidget(self.button1, alignment=Qt.AlignLeft)
        line1.addWidget(text2, alignment=Qt.AlignLeft)
        line1.addWidget(self.input2, alignment=Qt.AlignLeft)
        line1.addWidget(self.button2, alignment=Qt.AlignLeft)
        line2.addLayout(line)
        line2.addLayout(line1)
        self.setLayout(line2)

    def event1(self):
        try:
            a = float(self.input1.text())
            b = a * 1.8 + 32
            c = self.input2.setText(f"{b}")
        except:
            self.input1.setText("Введите ЦЕЛОЕ число")

    def event2(self):
        try:
            a = float(self.input2.text())
            b = (a - 32) / 1.8
            с = self.input1.setText(f"{b}")
        except:
            self.input2.setText("Введите ЦЕЛОЕ число")

    def connects(self):
        self.button1.clicked.connect(self.event1)
        self.button2.clicked.connect(self.event2)


app = QApplication([])
win = Win()
app.exec_()
