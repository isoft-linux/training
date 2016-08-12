#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

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

pi = 3.1415926
print(pi)
print(int(pi))
print(float(pi))
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
print(~x)       # INV   11111101
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
    print i
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
def func(c=None):
    return {
            'a': "case a",
            'b': "case b",
            }.get(c, "default:")
print(func("c"))

class obj(object):
    def __init__(self):
        print(sys._getframe().f_code.co_name)

    def __del__(self):
        print(sys._getframe().f_code.co_name)

obj1 = obj()
del obj1
obj1 = None
