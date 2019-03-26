import ctypes
from math import pow
from lab import shift_right, bin_subtract, bin_add


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
    first = a if abs(bin_to_float(a)) > abs(bin_to_float(b)) else b
    second = b if abs(bin_to_float(a)) > abs(bin_to_float(b)) else a
    
    exp_f = first[1:9]
    exp_s = second[1:9]
    exp_diff = int(bin_subtract(exp_f, exp_s), 2)
    print('Exponents difference: ', exp_diff)
    
    second_mant = '1' + second[9:]
    second_flag = '1'
    for i in range(0, exp_diff):
        second_flag = '0'
        second_mant = shift_right(second_mant)
    
    print('Shifted mantissa of least number: ', second_mant[1:])
    
    second = second[0] + exp_f + second_mant[1:]
    
    # think
    mant_sum = bin_add('1' + first[9:], second_flag + second[9:], n=25)
    mant_shift = '0'
    if mant_sum[1] == 0:
        mant_shift = '1'
    mant_sum = mant_sum[2:]

    print('Summed mantissa: ', mant_sum)

    new_exp = bin_add(exp_f, mant_shift, n=8)

    res = first[0] + new_exp + mant_sum

    print('Addition result: ', res)

    return res
