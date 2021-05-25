# -*- coding:utf8 -*-
import math

def rad(deg):
    return deg * math.pi / 180

def clarke(a, b, c):
    return {'alpha': a, 'beta': (a+2*b) / math.sqrt(3)}

def park(alpha, beta, theta):
    _theta = rad(theta)
    return {'d': alpha * math.cos(_theta) + beta * math.sin(_theta), 'q': -alpha * math.sin(_theta) + beta * math.cos(_theta)}

def reverse_park(d, q, theta):
    _theta = rad(theta)
    return {'alpha': d * math.cos(_theta) - q * math.sin(_theta), 'beta': d * math.sin(_theta) + q * math.cos(_theta)}

def reverse_clarke(alpha, beta):
    return {'a': alpha, 'b': (-alpha + beta*math.sqrt(3)) / 2.0, 'c': -(alpha + beta*math.sqrt(3)) / 2.0}


