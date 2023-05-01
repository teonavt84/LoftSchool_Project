print('Электронная очередь 2.2')
print('************************')
name_data = []


def create_queue_list(data):
    operation_data = ['M', 'N', 'P', 'S']
    i = 1
    while True:
        name = input('Введите фамилию, или нажмите Enter для выхода: ')
        if name == '':
            print('Всего Вам доброго! До свидания!')
            break
        else:
            while True:
                operation = input('Введите операцию. Доступные операции: M, N, P, S: ')
                if operation.capitalize() in operation_data:
                    sub_data = [i, name.capitalize(), operation.capitalize()]
                    data.append(sub_data)
                    print('------------------------')
                    for i, name, oper in data:
                        print(f'{i:03d} |{name:^15s}| {oper:5s}')
                        i += 1
                    print('------------------------')
                    break
                else:
                    print('Введен неверный код операции.')
                    pass


create_queue_list(name_data)
