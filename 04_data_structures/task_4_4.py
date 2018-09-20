# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
vlans1 = command1.strip().split()
vlans1 = vlans1[-1].split(',')
vlans2 = command2.strip().split()
vlans2 = vlans2[-1].split(',')
r = set(vlans2).intersection(set(vlans1))
r = list(r)
r = [int(i) for i in r]
r.sort()
print(r)
