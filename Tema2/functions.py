# Exercitiul 1
def sum_of_int_and_floats(*args, **kwargs):
    suma = 0
    for x in args:
        if type(x) == int:
            suma = suma + x
        elif type(x) == float:
            suma = suma + x
        else:
            continue
    return suma


print(sum_of_int_and_floats(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_of_int_and_floats())
print(sum_of_int_and_floats(2, 4, 'abc', param_1=2))


# Exercitiul 2
def sum_all_numbers(n):
    if n == 0:
        return 0
    return n + sum_all_numbers(n-1)


def sum_even_numbers(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_even_numbers(n-2)
    else:
        return sum_even_numbers(n-1)


def sum_odd_numbers(n):
    if n < 0:
        return 0
    if n % 2 == 1:
        return n + sum_odd_numbers(n-2)
    else:
        return sum_odd_numbers(n-1)


print(sum_all_numbers(9))
print(sum_even_numbers(11))
print(sum_odd_numbers(12))


# Exercitiul 3
def integer_validation():
    inserted_key = input('Write the key to validate = ')
    try:
        inserted_key = int(inserted_key)
        print(f'{inserted_key} is an integer')
        return inserted_key
    except ValueError:
        print(f'{inserted_key} is not an integer')
        return 0


print(integer_validation())
