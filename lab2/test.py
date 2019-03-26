from lab import *
from float import *
import random as rnd

# multiplication check
print('Multiplication check')
a1 = rnd.randint(1, 50)
b1 = rnd.randint(1, 50)
print('a1 = ', a1)
print('b1 = ', b1)

c1 = multiply(a1, b1)

print('Result: ', c1)
print('Expected result: ', a1 * b1)
print()
print()
print()


# division check
print('Division check')
a2 = rnd.randint(50, 100)
b2 = rnd.randint(1, 25)
print('a2 = ', a2)
print('b2 = ', b2)

c2 = divide(a2, b2)

print('Result: ', c2)
print('Expected result: ', int(a2/b2))
print()
print()
print()


# floating point check
print('Floating point numbers check')
a3 = rnd.randint(1, 10) * rnd.random()
b3 = rnd.randint(1, 5) * rnd.random()
print('a3 = ', a3)
print ('b3 = ', b3)

a3f = float_to_bin(a3)
b3f = float_to_bin(b3)
print('floating a3: ', a3f)
print('floating b3: ', b3f)

c3 = add_floats(a3f, b3f)
print('Result: ', bin_to_float(c3))
print('Expected result: ', a3 + b3)
