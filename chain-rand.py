#!/usr/bin/python3

import random

n=10

x = 0
y = -16
for i in range(n):
    print('"$c_%d$"[x=%dmm,y=%dmm] <-' % (i, x, y),end='')
    x += random.randrange(5,30)

print()
