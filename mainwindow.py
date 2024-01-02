# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from window import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QFile
from PyQt6.QtGui import QPixmap



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Calculadora")
        self.op1 = ""
        self.op2 = ""
        self.operation = None
        self.is_op1_ready = False
        self.resultado_2.setStyleSheet("color: gray;")
        self.setFixedSize(1024, 720)


    def digito9(self):
        if not self.is_op1_ready:
            self.op1 += "9"
        else:
            self.op2 += "9"
        
        self.resultado.setText(self.resultado.text() + "9")
        

    def digito8(self):
        if not self.is_op1_ready:
            self.op1 += "8"
        else:
            self.op2 += "8"
        
        self.resultado.setText(self.resultado.text() + "8")


    def digito7(self):
        if not self.is_op1_ready:
            self.op1 += "7"
        else:
            self.op2 += "7"
        
        self.resultado.setText(self.resultado.text() + "7")

    def digito6(self):
        if not self.is_op1_ready:
            self.op1 += "6"
        else:
            self.op2 += "6"

        self.resultado.setText(self.resultado.text() + "6")

    def digito5(self):
        if not self.is_op1_ready:
            self.op1 += "5"
        else:
            self.op2 += "5"

        self.resultado.setText(self.resultado.text() + "5")


    def digito4(self):
        if not self.is_op1_ready:
            self.op1 += "4"
        else:
            self.op2 += "4"

        self.resultado.setText(self.resultado.text() + "4")


    def digito3(self):
        if not self.is_op1_ready:
            self.op1 += "3"
        else:
            self.op2 += "3"

        self.resultado.setText(self.resultado.text() + "3")


    def digito2(self):
        if not self.is_op1_ready:
            self.op1 += "2"
        else:
            self.op2 += "2"

        self.resultado.setText(self.resultado.text() + "2")


    def digito1(self):
        if not self.is_op1_ready:
            self.op1 += "1"
        else:
            self.op2 += "1"

        self.resultado.setText(self.resultado.text() + "1")


    def digito0(self):
        if not self.is_op1_ready:
            self.op1 += "0"
        else:
            self.op2 += "0"

        self.resultado.setText(self.resultado.text() + "0")


    def digitodot(self):
        if not self.is_op1_ready:
            self.op1 += "."
        else:
            self.op2 += "."

        self.resultado.setText(self.resultado.text() + ".")


    def equals(self):
        if self.operation == "+":
            self.resultado.setText(f"{float(self.op1) + float(self.op2)}")
            self.resultado_2.clear()

        elif self.operation == "-":
            self.resultado.setText(f"{float(self.op1) - float(self.op2)}")
            self.resultado_2.clear()

        elif self.operation == "/":
            self.resultado.setText(f"{round(float(self.op1) / float(self.op2), 6)}")
            self.resultado_2.clear()
        
        elif self.operation == "*":
            self.resultado.setText(f"{float(self.op1) * float(self.op2)}")
            self.resultado_2.clear()


    def clear(self):
        self.op1 = ""
        self.op2 = ""
        self.operation = None
        self.is_op1_ready = False

        self.resultado.clear()
        self.resultado_2.clear()


    # soma dois numeros
    def sum(self):
        self.operation = "+"
        self.is_op1_ready = True

        self.resultado.clear()
        self.resultado_2.setText(f"{self.op1} + ")


    # divide 2 numeros
    def div(self):
        self.operation = "/"
        self.is_op1_ready = True

        self.resultado.clear()
        self.resultado_2.setText(f"{self.op1} / ")


    # multiplica 2 numeros
    def mul(self):
        self.operation = "*"
        self.is_op1_ready = True

        self.resultado.clear()
        self.resultado_2.setText(f"{self.op1} x ")


    # subtrai 2 numeros
    def sub(self):
        self.operation = "-"
        self.is_op1_ready = True

        self.resultado.clear()
        self.resultado_2.setText(f"{self.op1} - ")


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())