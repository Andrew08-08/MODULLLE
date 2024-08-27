my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while len(my_list):
    number = int(input('Введите число из списка: '))
    if number > -1:
        print('Далее')
        continue
    else:
        print('Отрицательно!')
        break