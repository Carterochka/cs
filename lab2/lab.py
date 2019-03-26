def multiply(multiplicand, multiplier):
    bin_multiplicand = to_n_bit(bin(multiplicand).lstrip('0b'), n=32)
    print('Multiplicand: ' + bin_multiplicand)
    
    bin_multiplier = to_n_bit(bin(multiplier).lstrip('0b'), n=32)
    print('Multiplier: ' + bin_multiplier)
    
    bin_product = to_n_bit(bin(0).lstrip('0b'), n=64)
    print('Initializing register: ' + bin_product)
    print()
    
    for i in range(0, 32):
        if bin_multiplier[len(bin_multiplier) - 1] == '1':
            print('Multiplier LSB=1: adding multiplicand to product')
            bin_product = bin_add(bin_multiplicand, bin_product)
            print('Product: ' + bin_product)
        # multiplicand left bin-shift
        bin_multiplicand = shift_left(bin_multiplicand)
        print('Shifting multiplicand to left: ' + bin_multiplicand)
        # multiplier right bin-shift
        bin_multiplier = shift_right(bin_multiplier)
        print('Shifting multiplier to right: ' + bin_multiplier)
        print()

    return int(bin_product, 2)


def bin_add(a, b, n=64):
    a_i = int(a, 2)
    b_i = int(b, 2)
    return to_n_bit(bin(a_i+b_i).lstrip('0b'), n)


def bin_subtract(a, b, n=32):
    a_i = int(a, 2)
    b_i = int(b, 2)
    return to_n_bit(bin(a_i-b_i).lstrip('0b'), n)


def to_n_bit(bin_number, n=32):
    temp_str = ''
    while len(temp_str + bin_number) < n:
        temp_str += '0'
    
    return temp_str + bin_number


def shift_left(str):
    return str[1:len(str)] + '0'

def shift_right(str):
    return '0' + str[:len(str) - 1]


def divide(dividend, divisor):
    bin_dividend = to_n_bit(bin(dividend).lstrip('0b'), n=32)
    print('Dividend: ' + bin_dividend)
    
    bin_divisor = bin(divisor).lstrip('0b')
    while len(bin_divisor) < 32:
        bin_divisor += '0'
    print('Divisor:  ' + bin_divisor)
    
    bin_register = bin_dividend + to_n_bit('', n=32)
    print('Initial register: ' + '\033[92m' + bin_register[:32] + '\033[0m' + bin_register[32:])
    print()
    
    for i in range(0, 32 - len(bin(divisor).lstrip('0b')) + 1):
        if bin_divisor <= bin_register[:32] :
            print('Divisor is less then dividend')
            print('Last bit in quotient is 1')
            print('Shifting register to left')
            res = bin_subtract(bin_register[:32], bin_divisor)
            bin_register = res + bin_register[32:]
            lsb = '1'
        else:
            print('Divisor is greater then dividend')
            print('The last quotient bit is set to 0\n')
            lsb = '0'
        bin_register = bin_register[:32] + shift_left(bin_register[32:])
        bin_register = bin_register[:63] + lsb
        bin_divisor = shift_right(bin_divisor)
        print('Divisor:  ' + bin_divisor)
        print('Register: ' + '\033[92m' + bin_register[:32] + '\033[0m' + bin_register[32:])
        print()

    return int(bin_register[32:], 2)
