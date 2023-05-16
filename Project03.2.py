import datetime
import random
constants = {'num_of_zeros': 3,
             'alignment_name': 13,
             'alignment_operation': 5,
             'alignment_date': 5,
             'print_line': '-'*61,
             'length_name': 10,
             'print_star': '*'*20,
             'num_in_header': 3,
             'name_in_header': 13,
             'code_in_header': 5,
             'date_in_header': 17,
             'duration_in_header': 7,
             'random_begin': 5,
             'random_end': 10}
print('Электронная очередь 3.1')
print(constants['print_star'])
base = []
base_time = []
i = 1


def name_client() -> str:
    while True:
        name_client = input('Введите фамилию, или нажмите Enter для выхода: ')
        if name_client != '':
            return name_client
        else:
            name_client = ''
            return name_client


def operation_client() -> str:
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


def data_client(i: int, name: str, operation: str, date: datetime, time: int) -> list:
    while True:
        sub_data = {'Number': i,
                    'Name': name.title(),
                    'Operation': operation.title(),
                    'Date': date,
                    'Time': time}
        base.append(sub_data)
        i += 1
        return base


def printing_queue(data: list):
    print(constants['print_line'])
    print(f"| {'№':^{constants['num_in_header']}} |"
          f" {'Фамилия':^{constants['name_in_header']}} |"
          f" {'Код':^{constants['code_in_header']}} | "
          f"{'Дата':^{constants['date_in_header']}} |"
          f" {'Длит.':^{constants['duration_in_header']}} |")
    print(constants['print_line'])
    for element in data:
        if len(element['Name']) > constants['length_name']:
            element['Name'] = element['Name'][:constants['length_name']] + '...'
        print(f"| {element['Number']:0{constants['num_of_zeros']}} |"
              f" {element['Name']:^{constants['alignment_name']}} |"
              f" {element['Operation']:^{constants['alignment_operation']}} |"
              f" {element['Date']:^{constants['alignment_date']}} |"
              f" {element['Time']} |")
    print(constants['print_line'])


def print_queue_length(idx: int):
    idx -= 1
    if idx % 100 in range(11, 20):
        n_people = 'человек'
    elif idx % 10 == 1:
        n_people = 'человек'
    elif idx % 10 in range(2, 5):
        n_people = 'человека'
    else:
        n_people = 'человек'
    print(f'Добрый день. Длина очереди перед вами: {idx} {n_people}')


def processing_time() -> datetime:
    time = random.randint(constants['random_begin'], constants['random_end'])
    time_string = datetime.timedelta(seconds=time)
    return time_string


def client_processing_time(time: datetime):
    base_time.append(time)
    total_time = datetime.timedelta()
    for t in base_time:
        total_time += t
    avg_time = int(total_time.total_seconds() / len(base_time))
    delta = datetime.timedelta(seconds=avg_time)
    formatted_time = (datetime.datetime.min + delta).strftime("%M:%S")
    print(f"Среднее время обслуживания клиента: {formatted_time}")


try:
    while True:
        print_queue_length(i)  # Печать длины очереди
        time = processing_time()
        client_processing_time(time)  # Печать среднего времени обслуживания клиента
        name = name_client()  # Ввод имени
        if name != '':
            operation = operation_client()  # Выбор операции
            date = date_time()
            data_cl = data_client(i, name, operation, date, time)
            printing_queue(data_cl)
            i += 1
        else:
            print('Всего Вам доброго! До свидания!')
            break
except KeyboardInterrupt:
    print('Всего Вам доброго! До свидания!')