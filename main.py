# Подгружаем библиотеки
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

from PasswordGenerator import password_generate  # Модуль с функцией-генератором пароля

# Подгружаем формы
from Designs.ui_MainWidget_design import Ui_MainWindow as MainWindow
from Designs.ui_PasswordManagerWidget_design import Ui_MainWindow as PswMngWindow


# Создаём класс с окном, подгружая дизайн из конвертированного (.ui -> .py) py-файла
class MainWidget(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        CHECK_BOXES = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6]  # Все checkbox окна
        symb_line = ""  # Строка, состоящая из симвлов, из которых будет генерироваться пароль

        if (True in [bool(cb.checkState()) for cb in CHECK_BOXES]):  # Если хотя бы одно отмечено галочкой
            for i in range(len(CHECK_BOXES)):
                if bool(CHECK_BOXES[i].checkState()):
                    symb_line += SYMBOLYC_DICTIONARY[i]
            
            self.textEdit.setText(password_generate(symb_line, self.spinBox.value()))  # Генерируем пароль и выводим его в textEdit


class PasswordManagerWidget(QMainWindow, PswMngWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        RowCount = int(input("Введите кличество строк:\n>> "))

        table = self.tableWidget
        table.setColumnCount(3)
        table.setRowCount(RowCount)
 
        # Задаём заголовки таблицы
        table.setHorizontalHeaderLabels(["Web", "Login", "Password"])
 
        # Задаем положение текста
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
 
        # Вставляем значения в ячейки
        for i in range(RowCount):
            table.horizontalHeaderItem(0).setToolTip("Column 1 ")
            table.horizontalHeaderItem(1).setToolTip("Column 2 ")

            table.setItem(i, 0, QTableWidgetItem(f"Text in row {i + 1}"))
            table.setItem(i, 1, QTableWidgetItem(f"Text in row {i + 1}"))


#  Списки с символома для генерации паролей
SYMBOLYC_DICTIONARY = [
    "abcdefghijklmnopqrstuvwxyz",
    "abcdefghijklmnopqrstuvwxyz".upper(),
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper(),
    "1234567890",
    '''@/*#!$%^?\[]-_)+=;`~.,<>'"|'''
]

# Адаптация под экраны с высоким разрешением
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# Запускаем сие чудо
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())