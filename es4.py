import math


def sum(a, b):

    ret = a + b
    return ret


def dist(primo_numero, secondo_numero):
    if primo_numero == 0:
        return 0
    return math.sqrt(primo_numero ** 2 + secondo_numero ** 2)


z = 0
print(dist(secondo_numero=z, primo_numero=2))
print(z)
