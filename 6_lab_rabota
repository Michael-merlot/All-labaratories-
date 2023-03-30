import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox
# sys нужна для получения информации об ОС. PyQt5 - Для оконных приложений. Application - Управляет потоком управления и осн настройками приложения с графическим интерфейсом.
# QWidget – является базовым классом для всех объектов пользовательского интерфейса. QLineEdit – виджет, который разрешает вводить и редактировать одну строку текста
# QHBoxLayout – выстраивает виджеты по горизонтали. QVBoxLayout – выстраивает виджеты по вертикали. QPushButton – кнопка, на которую можно нажимать

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

# Создаем оси
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout() #
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

# h - горизонтальные, v - вертикальные
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_result)

# Создаем виджеты и привязываем их к осям
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_0 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_0)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_third.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_third.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_third.addWidget(self.b_9)

        self.b_plus = QPushButton("+", self)
        self.hbox_fourth.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_fourth.addWidget(self.b_minus)

        self.b_mult = QPushButton("*", self)
        self.hbox_fourth.addWidget(self.b_mult)

        self.b_div = QPushButton("/", self)
        self.hbox_fourth.addWidget(self.b_div)

        self.b_float = QPushButton("float", self)
        self.hbox_fourth.addWidget(self.b_float)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_clear = QPushButton("Clear", self)
        self.hbox_result.addWidget(self.b_clear)

#  Кнопки операций
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("*"))
        self.b_div.clicked.connect(lambda: self._operation("/"))

        self.b_result.clicked.connect(self._result)
        self.b_clear.clicked.connect(self._clear)

#  Кнопки цифр
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_float.clicked.connect(lambda: self._button("."))

# Создаем контейнер для ошибок
    def warn_display(self, log):
        err = QMessageBox()
        if log == 1:
            err.setText("Пожалуйста, введите правильное значение \n Может быть набрано много точек или текста")
        elif log == 2:
            err.setText("Ошибка деления на ноль")
        err.setWindowTitle("Ошибка")
        err.exec_()

# Обработка кнопок за ввод цифр в линию ввода текста
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

# Операции
    def _operation(self, op):
        try:
            self.num_1 = float(self.input.text())
        except:
            self.warn_display(1)

        self.op = op
        self.input.setText("")

# Результат
    def _result(self):
        try:
            self.num_2 = float(self.input.text())
        except:
            self.warn_display(1)

        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == "/":
            if self.num_2 != 0.0:
                self.input.setText(str(self.num_1 / self.num_2))
            else:
                self.warn_display(2)

# Очистка
    def _clear(self):
        self.input.clear()

# Запуск приложения
app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
