#!/bin/python

import sys
import math

s = raw_input().strip()
count = s.count(" ")
new_s = ""
first,idx = 0,0
'''
while(count):
    occ = s.find(" ",idx)
    new_s += s[first:occ]
    idx = occ+1
    first = occ+1
    count-=1
new_s += s[first:]
''' 
ter = 0
s = s.replace(" ","")
l = int(len(s))
for r in range(int(math.floor(math.sqrt(l))),int(math.ceil(math.sqrt(l)))+1):
    for c in range(r,int(math.ceil(math.sqrt(l)))+1):
        if(r * c >= l):
            ter = 1
            break
    if(ter):
        break
idx = 0
for i in range(c):
    for j in range(r):
        idx = i + j * c
        if(idx <= l - 1):
            sys.stdout.write(s[idx])
    sys.stdout.write(" ")