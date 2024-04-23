def show_menu(menu, header=''):
    max_len_item_name = max([len(item) for item in menu])
    count_item = len(str(len(menu)))
    line_table = '+' + '-' * (max_len_item_name + count_item + 3) + '+'
    str_menu = line_table + '\n'

    if header != '':
        str_menu = str_menu + f'| {header.center(max_len_item_name + count_item)}  |' + '\n'
        str_menu = str_menu + line_table + '\n'

    for number, item in enumerate(menu, 1):
        str_menu = str_menu + f'| {str(number).ljust(count_item)} {item.ljust(max_len_item_name)} |' + '\n'

    return str_menu + line_table

print(show_menu(['первый', 'второй', 'третий'], 'меню'))
print(show_menu(['первый', 'второй 12345', 'третий']))
print('Первое изменение')
print('Второе изменение')
print('Третье изменение')

