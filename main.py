from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit


class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.set()
        self.initUI()
        # self.connects()

    def set(self):
        self.setWindowTitle("Конвертатор")
        self.show()

    def initUI(self):
        text1 = QLabel("Введите температуру в градусах Цельсия:")
        self.input1 = QLineEdit("")
        self.button = QPushButton("Отправить")
        text2 = QLabel("В градусах Фаренгейта:")
        input2 = QLineEdit("")
        line = QVBoxLayout()
        line.setSpacing(10)
        line.addWidget(text1, alignment=Qt.AlignLeft)
        line.addWidget(self.input1, alignment=Qt.AlignLeft)
        line.addWidget(self.button, alignment=Qt.AlignLeft)
        line.addWidget(text2, alignment=Qt.AlignLeft)
        line.addWidget(input2, alignment=Qt.AlignLeft)
        self.setLayout(line)

    def event(self):
        a = self.input1.text()
        print(a)

    # def connects(self):
    #     self.button.clicked.connect(event)


app = QApplication([])
win = Win()
app.exec_()
