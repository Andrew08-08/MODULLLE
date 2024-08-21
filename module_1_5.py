immutable_var = ([1,2], [3,4], [5,6], True, 'Might & Magic')
print(immutable_var)
#immutable_var[0] = 8000
#print(immutable_var) # значения элементов кортежа не изменяются, так как изначально применяются для защиты списков.
mutable_list = ['a, b, c,', 8, 9, 10]
mutable_list[3] = 77777
print(mutable_list)