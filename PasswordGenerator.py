from random import choice


def password_generate(symb_line: str, counter: int):
    password = ""  # Создаем строку для пароля

    for _ in range(counter):
        password += choice(symb_line)  # Рандомно выбираем counter символов из строки symb_line

    return password  # Возвращаем сгенерированный пароль