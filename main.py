# Подгружаем библиотеки
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow

from random import choice

# Создаём класс с окном, подгружая дизайн из конвертированного (.ui -> .py) py-файла
class MyWidget(QMainWindow, Ui_MainWindow):
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


# Функция генератора пароля
def password_generate(symb_line: str, counter: int):
    password = ""  # Создаем строку для пароля

    for _ in range(counter):
        password += choice(symb_line)  # Рандомно выбираем counter символов из строки symb_line

    return password  # Возвращаем сгенерированный пароль


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
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())