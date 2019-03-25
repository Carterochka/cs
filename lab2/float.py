import ctypes
from math import pow
from lab import shift_right

def float_to_bin(num):
    t = bin(ctypes.c_uint.from_buffer(ctypes.c_float(num)).value).lstrip('0b')
    while len(t) != 32:
        t = '0' + t
    return t


def bin_to_float(bin_num):
    power = pow(2, int(bin_num[1:9], 2) - 127)
    sign = pow(-1, int(bin_num[0]))
    value = 1.
    for i in range(0, 23):
        value += int(bin_num[9 + i]) * pow(2, -i-1)

    return sign * power * value


def add_floats(a, b):
    

    return
