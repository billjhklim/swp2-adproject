import random

from PyQt5.QtWidgets import *
import sys
from matrix import matrix1, matrix2, matrix3
import threading
matrix = matrix1
k = random.randint(1, 4)
if (k == 1):
    matrix = matrix1
elif (k == 2):
    matrix = matrix2
else:
    matrix = matrix3
class basicWindow(QWidget):
    global count
    def __init__(self):
        super().__init__()
        Outhboxlayout = QHBoxLayout()
        hboxlayout = QHBoxLayout()
        vboxlayout = QVBoxLayout()
        Btn1 = QPushButton("난이도")
        Btn2 = QPushButton("제출")
        Btn3 = QPushButton("초기화")
        self.label = QLabel("타이머")
        hboxlayout.addWidget(Btn1)
        hboxlayout.addWidget(Btn2)
        hboxlayout.addWidget(Btn3)
        hboxlayout.addWidget(self.label)
        vboxlayout.addLayout(hboxlayout)
        grid_layout = QGridLayout()
        vboxlayout.addLayout(grid_layout)
        Outhboxlayout.addLayout(vboxlayout)
        Outhboxlayout.addLayout(grid_layout)

        self.setLayout(Outhboxlayout)

        for x in range(9):
            for y in range(9):
                button = QPushButton(str(str(matrix[x][y])))
                button.setMaximumWidth(40)
                grid_layout.addWidget(button, x, y)
                button.clicked.connect(self.button_clicked)

        self.setWindowTitle('sudoku')

    def button_clicked(self):
        button = self.sender()
        text, ok = QInputDialog.getInt(self, '값', '값을 입력하세요')
        if ok:
            button.setText(str(text))
count = 0
def startTimer():
    global count
    timer = threading.Timer(10, startTimer)
    timer.start()

    count += 1
    if count > 5:
        timer.cancel()

startTimer()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())



