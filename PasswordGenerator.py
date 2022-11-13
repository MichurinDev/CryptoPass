from random import choice


def password_generate(symb_line: str, counter: int):
    password = ""  # Создаем строку для пароля

    for _ in range(counter):
        # Рандомно выбираем counter символов из строки symb_line
        password += choice(symb_line)

    return password  # Возвращаем сгенерированный пароль
