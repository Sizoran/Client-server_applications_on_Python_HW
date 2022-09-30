"""
Task 4: Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode).

"""

base_list = ['разработка', 'администрирование', 'protocol', 'standard']
base_list_on_bytes = []
base_list_decode = []

for i in base_list:
    base_list_on_bytes.append(i.encode('utf-8'))

print(base_list_on_bytes)

for i in base_list_on_bytes:
    base_list_decode.append(i.decode('utf-8'))

print(base_list_decode)
