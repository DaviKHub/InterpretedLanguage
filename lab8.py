import re


def is_zip(zip_code: str):
    if bool(re.fullmatch(r"\d{6}", zip_code)):
        return True
    else:
        return False


def incorrect_arg(zip_code):
    if zip_code.isdigit():
        return zip_code
    else:
        raise ValueError("Неправильный формат zip кода. Должен быть шестизначным числом.")


while True:
    zip_code = input("Введите zip код:\t")
    try:
        print(incorrect_arg(zip_code))
        break
    except ValueError as e:
        print(e)