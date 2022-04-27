
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
import sys
import calc
import math


class Window(QMainWindow, calc.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(
            Qt.WindowFlags.CustomizeWindowHint |
            Qt.WindowFlags.WindowCloseButtonHint |
            Qt.WindowFlags.WindowMinMaxButtonsHint
        )

        self.is_equal = False

        self.lineEdit.setAlignment(Qt.Alignment.AlignRight)
        self.lineEdit_2.setAlignment(Qt.Alignment.AlignRight)

        self.pushButton_erase.clicked.connect(self.erasure)
        self.pushButton_equally.clicked.connect(self.res)
        self.pushButton_CE.clicked.connect(self.cleaning)
        self.pushButton_fact.clicked.connect(self.res_fact)
        self.pushButton_degree.clicked.connect(self.res_degree)
        self.pushButton_percent.clicked.connect(self.res_precent)

        self.pushButton_1.clicked.connect(lambda: self.conclusion('1'))
        self.pushButton_2.clicked.connect(lambda: self.conclusion('2'))
        self.pushButton_3.clicked.connect(lambda: self.conclusion('3'))
        self.pushButton_4.clicked.connect(lambda: self.conclusion('4'))
        self.pushButton_5.clicked.connect(lambda: self.conclusion('5'))
        self.pushButton_6.clicked.connect(lambda: self.conclusion('6'))
        self.pushButton_7.clicked.connect(lambda: self.conclusion('7'))
        self.pushButton_8.clicked.connect(lambda: self.conclusion('8'))
        self.pushButton_9.clicked.connect(lambda: self.conclusion('9'))
        self.pushButton_0.clicked.connect(lambda: self.conclusion('0'))
        self.pushButton_root.clicked.connect(lambda: self.res_root('√'))
        self.pushButton_plus.clicked.connect(lambda: self.conclusion('+'))
        self.pushButton_minus.clicked.connect(lambda: self.conclusion('-'))
        self.pushButton_multiply.clicked.connect(lambda: self.conclusion('*'))
        self.pushButton_division.clicked.connect(lambda: self.conclusion('/'))
        self.pushButton_point.clicked.connect(lambda: self.conclusion('.'))
        self.pushButton_bracketopen.clicked.connect(
            lambda: self.conclusion('('))
        self.pushButton_bracketclose.clicked.connect(
            lambda: self.conclusion(')'))

        self.len_line = 18
        self.size = 20

    def conclusion(self, num):
        if len(self.lineEdit.text()) > self.len_line and self.size > 12:
            self.lineEdit.setStyleSheet("QLineEdit{\n"
                                        "    background-color:  #171717;\n"
                                        "    color: white;\n"
                                        f"    font: 87 {self.size}pt \"Segoe UI\";\n"
                                        "    border-style: solid;\n"
                                        "}")
            self.len_line += 2
            self.size -= 2

        if self.lineEdit.text() == '0' or self.is_equal:
            if num == '.':
                self.lineEdit.setText(self.lineEdit.text() + num)
            elif num in ('-', '+', '*', '/'):
                self.lineEdit.setText(self.lineEdit.text()+num)
                self.is_equal = False
            else:
                self.lineEdit_2.setText('')
                self.lineEdit.setText(num)
                self.is_equal = False
        elif self.lineEdit.text()[-1] in ('.', '-', '+', '*', '/') and num in ('.', '-', '+', '*', '/'):
            self.lineEdit.setText(self.lineEdit.text()[:-1] + num)
        else:
            self.lineEdit.setText(self.lineEdit.text() + num)

    def erasure(self):
        if self.is_equal:
            self.lineEdit.setText('0')
        elif len(self.lineEdit.text()) == 1:
            self.lineEdit.setText('0')
        else:
            self.lineEdit.setText(self.lineEdit.text()[:-1])
            self.len_line = 18
            self.size = 20
            self.lineEdit.setStyleSheet("QLineEdit{\n"
                                        "    background-color:  #171717;\n"
                                        "    color: white;\n"
                                        f"    font: 87 {self.size}pt \"Segoe UI\";\n"
                                        "    border-style: solid;\n"
                                        "}")

    def cleaning(self):
        self.lineEdit_2.setText('')
        self.lineEdit.setText('0')
        self.len_line = 18
        self.size = 20
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "    background-color:  #171717;\n"
                                    "    color: white;\n"
                                    f"    font: 87 {self.size}pt \"Segoe UI\";\n"
                                    "    border-style: solid;\n"
                                    "}")

    def poxyi(self, *num):
        answer = []
        n = 0
        for i in range(len(self.lineEdit.text())):
            if self.lineEdit.text()[i] in ("+", "-", "*", "/", "("):
                answer.append(self.lineEdit.text()[n:i])
                answer.append(self.lineEdit.text()[i])
                n = i + 1
        answer.append(self.lineEdit.text()[n:])
        return answer

    def res(self):
        if self.lineEdit.text()[0] == '0' and self.lineEdit.text()[1:] in ('-', '+', '*', '/'):
            self.lineEdit_2.setText(self.lineEdit.text()+'0=')
            self.lineEdit.setText('0')
        else:
            try:
                self.lineEdit_2.setText(self.lineEdit.text()+'=')
                result = str(eval(self.lineEdit.text()))
                self.lineEdit.setText(result)
                if len(result) >= 3:
                    if result[-2] == '.' and result[-1] == '0':
                        self.lineEdit.setText(result[:-2])
                else:
                    self.lineEdit.setText(result)
                self.is_equal = True
            except:
                self.lineEdit_2.setText('')
                self.lineEdit.setText('Результат не определен')
                self.is_equal = True

    def res_root(self, num):
        # self.lineEdit_2.setText('√(' + self.lineEdit.text() + ')')
        # try:
        #     root_num = str(math.sqrt(int(self.lineEdit.text())))
        #     if root_num[-1] == '0':
        #         self.lineEdit.setText(root_num[:-2])
        #         self.is_equal = True
        #     else:
        #         self.lineEdit.setText(root_num)
        #         self.is_equal = True
        # except:
        #     self.lineEdit.setText('похуй')

        res = self.poxyi(self)
        try:
            self.lineEdit_2.setText(
                ''.join(res[:-1]) + '√(' + str(res[-1]) + ')')
            res[-1] = math.sqrt(float(res[-1]))
            self.lineEdit.setText(''.join(map(str, res)))
        except:
            self.lineEdit_2.setText('')
            self.lineEdit.setText('Результат не определен')

    def res_fact(self, num):
        # self.lineEdit_2.setText('fact(' + self.lineEdit.text() + ')')
        # try:
        #     fact_num = str(math.factorial(int(self.lineEdit.text())))
        #     self.lineEdit.setText(fact_num)
        #     self.is_equal = True
        # except:
        #     self.lineEdit.setText('похуй')

        res = self.poxyi(self)
        try:
            self.lineEdit_2.setText(
                ''.join(res[:-1]) + 'fact(' + str(res[-1]) + ')')
            res[-1] = math.factorial(int(res[-1]))
            self.lineEdit.setText(''.join(map(str, res)))
        except:
            self.lineEdit_2.setText('')
            self.lineEdit.setText('Не целое число')

    def res_degree(self, num):
        pass

    def res_precent(self, num):
        res = self.poxyi(self)
        try:
            if len(res) == 1:
                self.lineEdit_2.setText(''.join(res))
                res[-1] = float(res[-1])/100
                self.lineEdit.setText(''.join(map(str, res)))
            else:
                self.lineEdit_2.setText(''.join(res[:-1]) + str(res[-1]) + '%')
                res[-1] = float(res[-3])*float(res[-1])/100
                self.lineEdit.setText(''.join(map(str, res)))
        except:
            self.lineEdit_2.setText('')
            self.lineEdit.setText('Результат не определен')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
