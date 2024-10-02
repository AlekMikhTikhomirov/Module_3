from types import NoneType


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if  len(str_number) == 1 and int(str_number) != 0:
        return first
    elif len(str_number) == 1 and int(str_number) == 0:
        return 1
    elif len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(number = int(input("Enter any non-zero number & press Enter: ")))
print(result)