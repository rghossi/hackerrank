#!/bin/python

import sys
from itertools import combinations

def isValid(s):
    if (len(s) < 2 or s[0] == s[1]): 
        return False
    a = s[0]
    b = s[1]
    for i in range(len(s)):
        if (i%2 == 0 and s[i] == a):
            continue
        elif(i%2 == 1 and s[i] == b):
            continue
        else:
            return False
    return True

s_len = int(raw_input().strip())
s = raw_input().strip()

if (isValid(s)): 
    print len(s)
    sys.exit()
elif (len(s) < 2):
    print 0
    sys.exit()

list_s = list(set(s))
num_of_deleted_chars = len(list_s) - 2

if (num_of_deleted_chars < 1) :
    print 0
    sys.exit()

maximum_length = 0

for item in combinations(range(len(list_s)),num_of_deleted_chars):
    temp_s = s
    for i in item:
        temp_s = temp_s.replace(list_s[i], "")
    if isValid(temp_s) and len(temp_s) > maximum_length : maximum_length = len(temp_s)

print maximum_length