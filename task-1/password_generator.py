# Шкель Антон ПрИнж25-1

import secrets
import string


def generate_password(length):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = "".join(secrets.choice(alphabet) for _ in range(length))
        if length < 2:
            return password
        if any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
            return password


def ask_length():
    while True:
        value = input("Введите длину пароля: ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Нужно целое число больше нуля, попробуйте ещё раз.")


def main():
    print("Генератор паролей | Шкель Антон ПрИнж25-1")
    length = ask_length()
    print(f"Ваш пароль: {generate_password(length)}")


if __name__ == "__main__":
    main()
