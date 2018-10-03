# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split(' ')#.split(',')
ospf_route.remove('via')
ospf_route[0] = 'OSPF'
protocol, prefix, metric, nupd,lupd,oi = ospf_route[0], ospf_route[8], ospf_route[9][1:-2], ospf_route[10][:-2], ospf_route[11][:-2], ospf_route[-1]

print(" Protocol: {:>18} \n".format(protocol), "Prefix: {:>28} \n".format(prefix), "AD/Metric: {:>18} \n".format(metric),
 "Next-Hop: {:>22} \n".format(nupd), "Last update: {:>15} \n".format(lupd), "Outbound Interface: {:>19} \n".format(oi))
