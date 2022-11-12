# Подгружаем библиотеки
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt

import sqlite3 as SQL

from PasswordGenerator import password_generate  # Модуль с функцией-генератором пароля

# Подгружаем формы
from Designs.ui_MainWidget_design import Ui_MainWindow as MainWindow
from Designs.ui_PasswordManagerWidget_design import Ui_MainWindow as PswMngWindow


# Создаём классы с окнами, подгружая дизайны из конвертированных (.ui -> .py) py-файлов
class MainWidget(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate)
        self.pushButton_2.clicked.connect(self.loadPaswMngWin)

    def generate(self):
        global password

        CHECK_BOXES = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6]  # Все checkbox окна
        symb_line = ""  # Строка, состоящая из симвлов, из которых будет генерироваться пароль

        if (True in [bool(cb.checkState()) for cb in CHECK_BOXES]):  # Если хотя бы одно отмечено галочкой
            for i in range(len(CHECK_BOXES)):
                if bool(CHECK_BOXES[i].checkState()):
                    symb_line += SYMBOLYC_DICTIONARY[i]
            
            self.textEdit.setText(password_generate(symb_line, self.spinBox.value()))  # Генерируем пароль и выводим его в textEdit
            password = self.textEdit.toPlainText()

    def loadPaswMngWin(self):
        dialog = PasswordManagerWidget(self)
        dialog.show()


class PasswordManagerWidget(QMainWindow, PswMngWindow):
    def __init__(self, parent=None):
        super(PasswordManagerWidget, self).__init__(parent)
        self.setupUi(self)
        
        self.textEdit_3.setText(password)
        self.reloadTable()
        self.pushButton.clicked.connect(self.addToDB)

    def addToDB(self):
        """
        Функция, которая добавляет строку в таблицу БД
        """

        # Получаем регистрационные данные
        user_web = self.textEdit.toPlainText()
        user_login = self.textEdit_2.toPlainText()
        user_password = self.textEdit_3.toPlainText()

        sql.execute(f"SELECT login FROM {db_name}")
        for web, login, _ in sql.execute(f"SELECT * FROM {db_name}"): # Пробегаемся по всем строкам
            if login == user_login and web == user_web:  # Если такая пара сайт-логин внесена
                print(f'Пользователь "{login}" на сервисе "{web}" уже присутсвует в базе!')  # Выдаем ошибку
                break
        else:  # А если нет..
            sql.execute(f"INSERT INTO {db_name} VALUES (?, ?, ?)", (user_web, user_login, user_password))  # Вносим :)
            db.commit()

        self.reloadTable()

    def reloadTable(self):
        """
        Функция, которая будет обновлять таблицу в форме,
        в которую подгружаются данные из таблицы базы данных
        """
        VALUE = list(sql.execute(f"SELECT * FROM {db_name}"))
        RowCount = len(VALUE)

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
            web, login, passw = VALUE[i]
            table.horizontalHeaderItem(0).setToolTip("Column 1 ")
            table.horizontalHeaderItem(1).setToolTip("Column 2 ")
            table.horizontalHeaderItem(1).setToolTip("Column 3 ")

            table.setItem(i, 0, QTableWidgetItem(web))
            table.setItem(i, 1, QTableWidgetItem(login))
            table.setItem(i, 2, QTableWidgetItem(passw))


# Подключаемся к БД
db = SQL.connect("PasswordManagerDB.db")  # Файл БД
sql = db.cursor()
db_name = "PasswordManager"  # Название таблицы в БД

# Если таблица <db_name> не создана - создаем
sql.execute(f"""CREATE TABLE IF NOT EXISTS {db_name} (
    web TEXT,
    login TEXT,
    password TEXT
)""")

db.commit()

#  Списки с символами для генерации паролей
SYMBOLYC_DICTIONARY = [
    "abcdefghijklmnopqrstuvwxyz",
    "abcdefghijklmnopqrstuvwxyz".upper(),
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper(),
    "1234567890",
    '''@/*#!$%^?\[]-_)+=;`~.,<>'"|'''
]

password = ""

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