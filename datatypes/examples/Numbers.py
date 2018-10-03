#Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

#We can use the type() function to know which class a variable or a value belongs to and isinstance() function to check if it belongs to a particular class.


a = 5

# Output: <class 'int'>
print(type(a))

# Output: <class 'float'>
print(type(5.0))

# Output: (8+3j)
c = 5 + 3j
print(c + 3)

# Output: True
print(isinstance(c, complex))



#Python provides operations involving fractional numbers through its fractions module.

#A fraction has a numerator and a denominator, both of which are integers. This module has support for rational number arithmetic. We can create Fraction objects in various ways.

import fractions

# Output: 3/2
print(fractions.Fraction(1.5))

# Output: 5
print(fractions.Fraction(5))

# Output: 1/3
print(fractions.Fraction(1,3))


#While creating Fraction from float, we might get some unusual results. This is due to the imperfect binary floating point number representation as discussed in the previous section.Fortunately, Fraction allows us to instantiate with string as well. This is the preferred options when using decimal numbers.

import fractions

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1))

# As string
# Output: 11/10
print(fractions.Fraction('1.1'))


#This datatype supports all basic operations. Here are few examples.

from fractions import Fraction as F

# Output: 2/3
print(F(1,3) + F(1,3))

# Output: 6/5
print(1 / F(5,6))

# Output: False
print(F(-3,10) > 0)

# Output: True
print(F(-3,10) < 0)




#Python offers modules like math and random to carry out different mathematics like trigonometry, logarithms, probability and statistics


import math

# Output: 3.141592653589793
print(math.pi)

# Output: -1.0
print(math.cos(math.pi))

# Output: 22026.465794806718
print(math.exp(10))

# Output: 3.0
print(math.log10(1000))

# Output: 1.1752011936438014
print(math.sinh(1))

# Output: 720
print(math.factorial(6))

##Full list of functions available in python 

import random

# Output: 16
print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())
