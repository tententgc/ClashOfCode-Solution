import sys
import math
z = 0
a = ("cookies")
h = int(input())
for i in range(h):
    inputs = input().split()
    w = int(inputs[0])
    if w>80:
        t = int(inputs[1])
        t*=2
        z+= t
    else:
        t = int(inputs[1])
        z += t
    if input[2] == "chocolate_chip_cookies" and input[3] == "hot_milk" :
        z+=1


print(z)
