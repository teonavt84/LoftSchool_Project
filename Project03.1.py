import datetime
print('Электронная очередь 3.1')
print('*'*20)
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
    operation_data = {'M', 'N', 'P', 'S'}
    while True:
        operation_type = input('Введите операцию. Доступные операции: M, N, P, S: ')
        if operation_type.capitalize() in operation_data:
            return operation_type
        else:
            print('Введен неверный код операции.')


def date_time():
    date = datetime.datetime.now()
    formatted_date = date.strftime("%d-%m-%y %H:%M:%S")
    return formatted_date


def data_client(i, name, operation, date):
    while True:
        sub_data = {'Number': f"{i:03}",
                    'Name': f"{name.title():^15s}",
                    'Operation': f"{operation.title():^5}", 'Date': date}
        base.append(sub_data)
        i += 1
        return base


def printing_queue(data):
    print('-'*51)
    for element in data:
        element['Name'] = element['Name'][:10] + '...'
        print(' | '.join(map(str, element.values())), '|')
    print('-'*51)


while True:
    print(f'Добрый день. Длина очереди перед вами: {i - 1}')
    name = name_client()
    if name != '':
        operation = operation_client()
        date = date_time()
        data_cl = data_client(i, name, operation, date)
        printing_queue(data_cl)
        i += 1
    else:
        print('Всего Вам доброго! До свидания!')
        break
