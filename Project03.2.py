import datetime
import random
print('Электронная очередь 3.1')
print('*' * 20)
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
    print('-' * 61)
    print(f"| {'№':^3} | {'Фамилия':^13} | {'Код':^5} | {'Дата':^17} | {'Длит.':^7} |")
    print('-' * 61)
    for element in data:
        if len(element['Name']) > 10:
            element['Name'] = element['Name'][:10] + '...'
        print(f"| {element['Number']:03} |"
              f" {element['Name']:^13} |"
              f" {element['Operation']:^5} |"
              f" {element['Date']:^5} |"
              f" {element['Time']} |")
    print('-' * 61)


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
    time = random.randint(5, 10)
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


while True:
    print_queue_length(i)  # Печать длины очереди
    try:
        name = name_client()  # Ввод имени
    except KeyboardInterrupt:
        print('Всего Вам доброго! До свидания!')
        break
    if name != '':
        operation = operation_client()  # Выбор операции
        date = date_time()
        time = processing_time()
        client_processing_time(time)  # Печать среднего времени обслуживания клиента
        data_cl = data_client(i, name, operation, date, time)
        printing_queue(data_cl)
        i += 1
    else:
        print('Всего Вам доброго! До свидания!')
        break
