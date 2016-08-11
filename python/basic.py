#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("The if statement is used for conditional execution")

i = 3
while i:
    print("The while statement is used for repeated execution as long as an expression is true")
    i = i - 1

for i in range(3):
    print("The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable objec")

try:
    1 / 0
except:
    print("The try statement specifies exception handlers and/or cleanup code for a group of statements")
finally:
    print("If finally is present, it specifies a ‘cleanup’ handler")

try:
    with open("/dev/input/mice", 'r') as fptr:
        pass
except:
    print("The with statement is used to wrap the execution of a block with methods defined by a context manager")

def func(foo, bar = None):
    print("%s %s" % (foo, bar))

func("foo")

class obj(object):
    def __init__(self):
        print(sys._getframe().f_code.co_name)

    def __del__(self):
        print(sys._getframe().f_code.co_name)

obj1 = obj()
