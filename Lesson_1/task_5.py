"""
Task 5: Написать код, который выполняет пинг веб-ресурсов yandex.ru, youtube.com
и преобразовывает результат из байтовового типа данных в строковый без ошибок для
любой кодировки операционной системы.

"""

import subprocess
import platform
# import locale
import chardet

# param = '-n' if platform.system().lower() == 'windows' else '-c'
# args = ['ping', param, '3', 'gb.ru']
# process = subprocess.Popen(args, stdout=subprocess.PIPE)
#
# for line in process.stdout:
#     result = locale.getpreferredencoding() ### метод locale отдельно отрабатывает но на выходе выдаёт "абру-кадабру"
#     print('result = ', result)
#     line = line.decode(result).encode('utf-8')
#     print(line.decode('utf-8'))


param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '3', 'gb.ru']
process = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in process.stdout:
    result = chardet.detect(line)  # Странно, но через chardet всё работает
    print('result = ', result)
    line = line.decode(result).encode('utf-8')
    print(line.decode('utf-8'))
