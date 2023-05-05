import os
import re
clear = lambda: os.system('cls')
print('Электронная очередь 2.3')
print('************************')
base = []
i = 1


def name_client() -> str:
    while True:
        name_client = input('Введите фамилию, или нажмите Enter для выхода: ')
        if name_client == '':
            return name_client
        confirmation = input('Вы уверены в правильности ввода данных? Введите 1 для подтверждения или 2 для повтора: ')
        if confirmation == '2':
            pass
        else:
            if confirmation == '1':
                return name_client


def name_verification(name: str) -> str:
    name = name.replace('+', '-').replace('_', '-').replace('=', '-')
    parts = name.split("-")
    formatted_parts = []
    for part in parts:
        formatted_part = part.capitalize()  # первая буква заглавная
        formatted_part = formatted_part[0] + formatted_part[1:].lower()
        formatted_parts.append(formatted_part)
    formatted_name = "-".join(formatted_parts)
    return formatted_name

def valid_symbols_name(name: str) -> bool:
    while True:
        name_valid = re.compile(r"[<>/{}[\]~1234567890`]")
        if name_valid.search(name):
            valid = False
        else:
            valid = True
        return valid

def operation_client() -> str:
    operation_data = ['M', 'N', 'P', 'S']
    while True:
        operation_type = input('Введите операцию. Доступные операции: M, N, P, S: ')
        if operation_type.capitalize() in operation_data:
            return operation_type
        else:
            print('Введен неверный код операции.')


def data_client(i: int, name: str, operation: str) -> list:
    while True:
        sub_data = [i, name.capitalize(), operation.capitalize()]
        base.append(sub_data)
        i += 1
        return base


def printing_queue(data: list):
    print('------------------------')
    for i, name, oper in data:
        print(f'{i:03d} |{name:^15s}| {oper:5s}')
    print('------------------------')


while True:
    name = name_client()
    if name == '':
        print('Всего Вам доброго! До свидания!')
        break
    else:
        valid_symbols_name(name)
    if not valid_symbols_name(name):
        print('Введено некорректная фамилия.')
    else:
        valid_symbols_name(name)
        name = name_verification(name)
        operation = operation_client()
        data_cl = data_client(i, name, operation)
        clear() # Работает только через cmd
        printing_queue(data_cl)
        i += 1

