# Задача 3
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

month_dict = {
    'Январь' : 31,
    'Февраль' : 28,
    'Март' : 31,
    'Апрель' : 30,
    'Май' : 31,
    'Июнь' : 30,
    'Июль' : 31,
    'Август' : 31,
    'Сентябрь' : 30,
    'Октябрь' : 31,
    'Ноябрь' : 30,
    'Декабрь' : 31
}

user_input = input("Введите номер месяца: ")
month = int(user_input)

if 1 <= month <= 12 :
    print('Вы ввели', list(month_dict)[month-1])
    print(f'В этом месяце {month_dict[list(month_dict)[month-1]]} дней')
else :
    print('Некорректный ввод')
