# -*- coding:utf8 -*-
import transfer

# 120度 三相波形
def the_wave(d, q, theta):
    res_reverse_park = transfer.reverse_park(d, q, theta)
    return transfer.reverse_clarke(res_reverse_park['alpha'], res_reverse_park['beta'])

def is_right(d, q, theta):
    wave = the_wave(d, q, theta)
    cl = transfer.clarke(wave['a'], wave['b'], wave['c'])
    res = transfer.park(cl['alpha'], cl['beta'], theta)
    return abs(d - res['d']) < 0.001 and abs(q - res['q']) < 0.001

for i in range(360):
    if not is_right(5, 0, i):
        print ('error')

print (is_right(5, 0, 60))