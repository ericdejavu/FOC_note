import svpwm

def the_pwm():
    return svpwm.generate(10, 14, 24, 0.0001)

print (the_pwm())