# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
a = input("IP-network: ")
b = a.split("/")
c, d = b
print(d)
c = c.split("." )
c = [int(i) for i in c]
e, f, g, h = c

print("Network:\n", "{:<10} {:<10} {:<10} {:<10}".format(e, f, g, h))
print(' {:010b} {:010b} {:010b} {:010b}'.format(e, f, g, h))
