def simple_separator():
    print('**********')
    return simple_separator


simple_separator()
print('Привет всем!')


def long_separator(count):
    print('*' * count)
    return long_separator


long_separator(10)


def long_separator(simbol, count):
    print(simbol * count)
    return long_separator


long_separator('$', 10)
print('Привет всем!')
long_separator('$', 10)


def simple_separator_2():
    print('##########')
    return simple_separator_2


def hello_world():
    print('*************')
    print('')
    print('Hello World!')
    print('')
    print('###############')
    return hello_world


hello_world()


def hello_who(name):
    if name is None:
        name = 'World'
    print('*************')
    print('')
    print('Hello', name)
    print('')
    print('###############')


print(hello_who('Max'))


def pow_many(power, *args):
    result = sum(args) ** power
    return result


print(pow_many(2, 1, 2, 3, 4))


def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(k, '->', v)


print(print_key_val(name='Max', age=21))


# numbers = input('Введите последовательность чисел: ')
def my_filter(iterable, function):
    result = []
    for item in iterable:
        if function(item):
            result.append(item)
            return result


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True , почему выдает False?
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True почему выдает False?
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True почему выдает False?
