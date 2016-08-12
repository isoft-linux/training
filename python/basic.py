#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys, math
from numpy import double

def divline():
    print("\033[32m--------------------------------------D.I.V.I.D.I.N.G.L.I.N.E-----------------------------------------\033[0m")

'''
The following tokens are operators:
+       -       *       **      /       //      %
<<      >>      &       |       ^       ~
<       >       <=      >=      ==      !=      <>

The following identifiers are used as reserved words, or keywords of the language, and cannot be used as ordinary identifiers. They must be spelled exactly as written here:
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try
'''

'''
double precision
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
'''
def testFloat():
    a = float(1.0 / 81)
    b = float(0.0)
    for i in range(729):
        b += a;
    print("%.15g" % (b));   # *NOT* 9.00002288818359

testFloat()

def testDouble():
    a = double(1.0 / 81)
    b = double(0.0)
    for i in range(729):
        b += a;
    print("%.15g" % (b));

testDouble()

print(complex(1, 1))
divline()

x = int(2)      #       00000010
y = int(3)      #       00000011
#------------------------------------------------------------------------------
print(x | y)    # OR    00000011
print(x ^ y)    # XOR   00000001
print(x & y)    # AND   00000010
print(x << y)   # LS    00010000
print(x >> 1)   # RS    00000001
'''
Two's complement
https://en.wikipedia.org/wiki/Two%27s_complement
'''
print(~x)       # INV   11111101 <- 11111100 + 1 <- NEG(00000011)
'''
Signed number representations
https://en.wikipedia.org/wiki/Signed_number_representations
'''
n = int(-37)
print(bin(n))   # 10100101
print(n.bit_length())
m = int(-1)
print(bin(m))   # 11111111
print(m.bit_length())
divline()

print(x ** y)   # POW
print(x // y)   # MOD
divline()

lists = []
for i in range(13):
    lists.append(i)
lists.append(12)
lists.append(12)
print(lists)
print(set(lists))
lists.reverse()
print(lists)
lists.sort()
print(lists)
lists.pop()
print(lists)
lists.pop()
print(lists)
print(len(lists))
lists[:] = []
print(lists)

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
print(matrix)
divline()

tup = ('Python', 83, ('Linux', 'KDE'))
print(tup)
print(tup * 3)
divline()

sets = {'Martin Gräßlin', 'David Faure', 'Sebastian Kügler'}
print(sets)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
divline()

dict = {'Name': 'Martin Gräßlin', 'Age': 27, 'Project': 'KWin'}
print(dict)
dict['Age'] = 21
print(dict)
print(dict.has_key('Home'))
dict['Home'] = 'Germany'
print(dict.has_key('Home'))
for k, v in dict.items():
    print(k, v)
divline()

if __name__ == "__main__":
    print("The if statement is used for conditional execution")
else:
    print("Being imported from another module")
divline()

i = 3
while i:
    if i == 1:
        break
    print("The while statement is used for repeated execution as long as an expression is true")
    i = i - 1
divline()

def generator(r=3):
    for i in range(r):
        if i == 0:
            continue
        print("The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable objec")
        yield i * i

for i in generator():
    print(i)
divline()

try:
    1 / 0
except:
    print("The try statement specifies exception handlers and/or cleanup code for a group of statements")
finally:
    print("If finally is present, it specifies a ‘cleanup’ handler")
divline()

try:
    with open("/dev/input/mice", 'r') as fptr:
        pass
except:
    print("The with statement is used to wrap the execution of a block with methods defined by a context manager")
divline()

# Replacements for switch statement
c = "c"
if c == 'a':
    print("case 'c':")
elif c == 'b':
    print("case 'b':")
else:
    print("default:")

def func(c=None):
    return {
            'a': "case 'a':",
            'b': "case 'b':",
            }.get(c, "default:")
print(func("c"))
divline()

class obj(object):
    def __init__(self):
        print(sys._getframe().f_code.co_name)

    def __del__(self):
        print(sys._getframe().f_code.co_name)

obj1 = obj()
del obj1
obj1 = None
