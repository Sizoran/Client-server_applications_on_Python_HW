"""
Task 3: Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе. Важно: решение должно быть универсальным,
т.е. не зависеть от того, какие конкретно слова мы исследуем.

"""

base_list = ['attribute', 'класс', 'функция', 'type']


def check_func(arg_list):
    for i in arg_list:
        try:
            temp_i = eval(f'b"{i}"')
            print(f'Element: "{i}" can covert to bytes, result: {temp_i}')
        except:
            print(f'Element: "{i}" can not covert to bytes')


check_func(base_list)
