import datetime
constants = {'num_of_zeros': 3,
             'alignment_name': 13,
             'alignment_operation': 5,
             'alignment_date': 5,
             'print_line': '-'*51,
             'length_name': 10,
             'print_star': '*'*20}
print('Электронная очередь 3.1')
print(constants['print_star'])
base = []
i = 1


def name_client() -> str:
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


def date_time() -> datetime:
    date = datetime.datetime.now()
    formatted_date = date.strftime("%d-%m-%y %H:%M:%S")
    return formatted_date


def data_client(i: int, name: str, operation: str, date: datetime) -> list:
    while True:
        sub_data = {'Number': i,
                    'Name': name.title(),
                    'Operation': operation.title(),
                    'Date': date}
        base.append(sub_data)
        i += 1
        return base


def printing_queue(data: list):
    print(constants['print_line'])
    for element in data:
        if len(element['Name']) > constants['length_name']:
            element['Name'] = element['Name'][:constants['length_name']] + '...'
        print(f"| {element['Number']:0{constants['num_of_zeros']}} | "
              f"{element['Name']:^{constants['alignment_name']}} | "
              f"{element['Operation']:^{constants['alignment_operation']}} | "
              f"{element['Date']:^{constants['alignment_date']}} |")
    print(constants['print_line'])


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
