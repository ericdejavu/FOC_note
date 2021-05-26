# -*- coding:utf8 -*-
import math

# 扇区选择
def page_sector(alpha, beta):
    sector = 0
    k1, k2 = math.sqrt(3) / 2, 0.5
    if beta > 0:
        sector += 1
    if k1 * alpha - k2 * beta > 0:
        sector += 2
    if -k1 * alpha - k2 * beta > 0:
        sector += 4
    return sector

# pwm 向量时长占比计算
def pwm_rate(sector, alpha, beta, udc, t):
    tx, ty, tn = 0, 0, 0
    k1, k2, k3 = math.sqrt(3) / 2, 1.5, math.sqrt(3)
    if sector == 1:
        tx = (-k2 * alpha + k1 * beta) * (t / udc)
        ty = (k2 * alpha + k3 * beta) * (t / udc)
    elif sector == 2:
        tx = (k2 * alpha + k1 * beta) * (t / udc)
        ty = -(k3 * beta * t / udc)
    elif sector == 3:
        tx = -((k2 * alpha + k1 * beta) * (t / udc))
        ty = k3 * beta * t / udc
    elif sector == 4:
        tx = -(k3 * beta * t / udc)
        ty = (-k2 * alpha + k1 * beta) * (t / udc)
    elif sector == 5:
        tx = k3 * beta * t / udc
        ty = -((k2 * alpha + k1 * beta) * (t / udc))
    else:
        tx = -((k2 * alpha + k3 * beta) * (t / udc))
        ty = -((-k2 * alpha + k3 * beta) * (t / udc))
    
    # 溢出处理
    usage = tx + ty
    if usage > t:
        tx /= usage * 1.0
        ty /= (tx + ty)
    
    return {'tx': tx, 'ty': ty, 'tn': t - tx - ty}

# 定时器比较值计算
def compare(sector, tx, ty, tn):
    # 三相pwm
    ta = tn / 4.0
    tb = tx / 2.0 + ta
    tc = ty / 2.0 + tb

    tcmp1, tcmp2, tcmp3 = 0, 0, 0
    
    if sector == 1:
        tcmp1 = tb
        tcmp2 = ta
        tcmp3 = tc
    elif sector == 2:
        tcmp1 = ta
        tcmp2 = tc
        tcmp3 = tb
    elif sector == 3:
        tcmp1 = ta
        tcmp2 = tb
        tcmp3 = tc
    elif sector == 4:
        tcmp1 = tc
        tcmp2 = tb
        tcmp3 = ta
    elif sector == 5:
        tcmp1 = tc
        tcmp2 = ta
        tcmp3 = tb
    else:
        tcmp1 = tb
        tcmp2 = tc
        tcmp3 = ta
    
    return {'tcmp1': tcmp1, 'tcmp2': tcmp2, 'tcmp3': tcmp3}

# alpha_beta电压以及母线电压、定时器周期
def generate(alpha, beta, udc, t):
    sector = page_sector(alpha, beta)
    rates = pwm_rate(sector, alpha, beta, udc, t)
    tx, ty, tn = rates['tx'], rates['ty'], rates['tn']
    return compare(sector, tx, ty, tn)


    