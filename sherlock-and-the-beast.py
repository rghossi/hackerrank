#!/bin/python

import sys
import itertools

def is_decent_number(number):
    n_str = str(number)
    if n_str.count('3') % 5 != 0: return False
    if n_str.count('5') % 3 != 0: return False
    return True

def next_n(n):
    for number in itertools.product('35', repeat=n):
        yield long(''.join(number))

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    dn = -1
    for number in next_n(n):
        dn = number if (number > dn and is_decent_number(number)) else dn
    print dn