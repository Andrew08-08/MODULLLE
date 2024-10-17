def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 999, 1)
print_params('hello', 2, 0)
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [111, 222, 333]
value_dict = {'a' : 'Add', 'b' : 'For', 'c' : 'Q'}
print_params(*value_list)
print_params(**value_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)