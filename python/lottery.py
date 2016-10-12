#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from os.path import expanduser
from random import randint

MAX = 100
MIN = 1
TMP_FILE = expanduser("~") + "/.kde20years.lot"
picks = []

print("\n\033[32mHappy birthday KDE 20 years!\033[0m\n")

try:
    picks = [int(line.rstrip('\n')) for line in open(TMP_FILE)]
except:
    pass

def __gen():
    if len(picks) > MAX - MIN:
        return 0
    r = randint(MIN, MAX)
    if r in picks:
        __gen()
    return r

r = __gen()
if r < MIN:
    print("Bye ;-)")
else:
    print("Congratulate \033[31m%d!\033[0m\n" % r)

try:
    with open(TMP_FILE, 'a') as fptr:
        fptr.write("%d\n" % r)
except:
    print("\033[31mERROR!\033[0m")
