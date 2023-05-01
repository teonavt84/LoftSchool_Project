print('Электронная очередь 2.1')
print('************************')
name_base = []
while True:
    name = input('Введите фамилию, или нажмите Enter для выхода: ')
    if name == '':
        print('Всего Вам доброго! До свидания!')
        break
    else:
        print('*****************')
        name_base.append(name)
        for name in name_base:
            print(f'|{name:^15}|')
        print('*****************')
