def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params([1,2,3])

values_list = [11, True, 'words']
values_dict = {'a': 1 , 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [(121, "let's try tuple", [11, 9] ), "Wow"]

print_params(*values_list2)