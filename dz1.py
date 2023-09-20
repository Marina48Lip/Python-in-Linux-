# Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
# Функция должна возвращать True, 
# если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess

def func(text, instr):
    if instr in text:
        return True
    else:
        return False

if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    instr = 'VERSION="22.04.1 LTS (Jammy Jellyfish)"'
    print(func(out, instr))
