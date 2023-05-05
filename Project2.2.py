print('Электронная очередь 2.2')
print('************************')
base = []
i = 1
def name_client():
    while True:
        name_client = input('Введите фамилию, или нажмите Enter для выхода: ')
        if name_client != '':
            return name_client
        else:
            name_client = ''
            return name_client


def operation_client():
    operation_data = ['M', 'N', 'P', 'S']
    while True:
        operation_type = input('Введите операцию. Доступные операции: M, N, P, S: ')
        if operation_type.capitalize() in operation_data:
            return operation_type
        else:
            print('Введен неверный код операции.')


def data_client(i, name, operation):
    while True:
        sub_data = [i, name.capitalize(), operation.capitalize()]
        base.append(sub_data)
        i += 1
        return base

def printing_queue(data):
    print('------------------------')
    for i, name, oper in data:
        print(f'{i:03d} |{name:^15s}| {oper:5s}')
    print('------------------------')

while True:
    name = name_client()
    if name != '':
        operation = operation_client()
        data_cl = data_client(i, name, operation)
        printing_queue(data_cl)
        i += 1
    else:
        print('Всего Вам доброго! До свидания!')
        break
