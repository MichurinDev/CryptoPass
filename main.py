# Подгружаем библиотеки
import sqlite3 as SQL
import sys
from pyperclip import copy
from win10toast import ToastNotifier

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from AlertWindow import showMessageBox
# Подгружаем формы
from Designs.ui_MainWidget_design import Ui_MainWindow as MainWindow
from Designs.ui_PasswordManagerWidget_design import \
    Ui_MainWindow as PswMngWindow
# Модуль с функцией-генератором пароля
from PasswordGenerator import password_generate


# Создаём классы с окнами,
# подгружая дизайны из конвертированных (.ui -> .py) py-файлов
class MainWidget(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Тыкаем - генерируется пароль
        self.pushButton.clicked.connect(self.generate)
        # Тыкаем - запускается менеджер паролей
        self.pushButton_2.clicked.connect(self.loadPaswMngWin)
        # Тыкаем - копируем сгенерированный пароль в буфер обмена
        self.pushButton_3.clicked.connect(self.copyInClipboard)

    def generate(self):
        global password

        CHECK_BOXES = [
            self.checkBox,
            self.checkBox_2,
            self.checkBox_3,
            self.checkBox_4,
            self.checkBox_5,
            self.checkBox_6
        ]  # Все checkbox окна

        # Строка, состоящая из симвлов, из которых будет генерироваться пароль
        symb_line = ""

        # Если хотя бы одно отмечено галочкой
        if (True in [bool(cb.checkState()) for cb in CHECK_BOXES]):
            for i in range(len(CHECK_BOXES)):
                if bool(CHECK_BOXES[i].checkState()):
                    # Добавляем в строку символов символы, выбранных списков
                    symb_line += SYMBOLYC_DICTIONARY[i]

            # Генерируем пароль и выводим его в textEdit
            self.textEdit.setText(
                password_generate(
                    symb_line, self.spinBox.value()
                    ))

            # Сохраняем сгенерированный пароль в глобальную переменную
            password = self.textEdit.toPlainText()

            # Записываем в файл с иторией
            with open(
                    "HistoryOfPasswordGeneration.txt",
                    "a",
                    encoding="utf-8") as history:
                history.write(f"{password}\n")

        else:
            showMessageBox(
                "Danger",
                "Выберете хотя бы один вид символов!",
                "Critical")

    def loadPaswMngWin(self):
        dialog = PasswordManagerWidget(self)
        dialog.show()

    def copyInClipboard(self):
        copy(password)
        toaster.show_toast(
            "Скопировано",
            "Сгенерированный пароль скопировани в буфер обмена!",
            icon_path="Images\\favicon.ico",
            threaded=True
        )


class PasswordManagerWidget(QMainWindow, PswMngWindow):
    def __init__(self, parent=None):
        super(PasswordManagerWidget, self).__init__(parent)
        self.setupUi(self)

        # Задаем значение текстового поля
        # с вводом пароля сгенерированным паролем
        self.textEdit_3.setText(password)
        self.reloadTable()  # Подгружаем таблицу формы

        # Тыкаем - добавляем новую строку
        self.pushButton.clicked.connect(self.addToDB)
        self.pushButton_2.clicked.connect(self.clearDB)

    def clearDB(self):
        sql.execute(f"DELETE FROM {table_name}")
        db.commit()
        self.reloadTable()

    def addToDB(self):
        """
        Функция, которая добавляет строку в таблицу БД
        """

        # Получаем регистрационные данные
        user_web = self.textEdit.toPlainText()
        user_login = self.textEdit_2.toPlainText()
        user_password = self.textEdit_3.toPlainText()

        sql.execute(f"SELECT login FROM {table_name}")

        # Пробегаемся по всем строкам
        for web, login, _ in sql.execute(f"SELECT * FROM {table_name}"):
            # Если такая пара сайт-логин внесена
            if login == user_login and web == user_web:
                # Выдаем ошибку
                showMessageBox(
                    "Danger",
                    f'Пользователь "{login}" на сервисе'
                    f'"{web}" уже присутсвует в базе!',
                    "Critical")
                break
        else:  # А если нет..
            sql.execute(
                f"INSERT INTO {table_name} VALUES (?, ?, ?)",
                (user_web, user_login, user_password)
                )  # Вносим :)

            db.commit()

        self.reloadTable()  # Обновляем таблицу формы

    def reloadTable(self):
        """
        Функция, которая будет обновлять таблицу в форме,
        в которую подгружаются данные из таблицы базы данных
        """

        # Выгруженная в список таблица
        VALUE = list(sql.execute(f"SELECT * FROM {table_name}"))
        RowCount = len(VALUE)  # Кол-во строчек

        # Создаем в форме таблицу 3 * RowCount
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
db_name = "PasswordManagerDB.db"  # Название БД
table_name = "PasswordManager"  # Название таблицы в БД

db = SQL.connect(db_name)  # Файл БД
sql = db.cursor()

# Если таблица <table_name> не создана - создаем
sql.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
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
    '''@/*#!$%^?\\[]-_)+=;`~.,<>'"|'''
]

# Глобальная переменная  паролем, чтобы передавать его между формами
password = ""

# Создаем экземпляр класса, отвечающий за уведомления
toaster = ToastNotifier()

# Адаптация под экраны с высоким разрешением
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(
        QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# Запускаем сие чудо
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
