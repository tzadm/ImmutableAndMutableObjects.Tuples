immutable_var = ('Сергей', 'возраст', 56, True, ['адрес', 8, 7])
print(immutable_var)
immutable_var [4][1] = 'Где вы живете'
print(immutable_var)
'''Кортеж относится к неизменяемым типам данных,
   элементы которого невозможно изменить, создается для сохранения данных неизменными. Исключение составляет
   список в составе кортежа содержание которого можно изменить.
'''
mutable_list = ['Сергей', 'возраст', 56, True, ['адрес', 8, 7]]
mutable_list[0] = 'Владимир'
print(mutable_list)

