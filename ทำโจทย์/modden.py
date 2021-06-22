import sys
import math

n = int(input())
a = input().split()
z = 0
y = 0
for i in a:
    if i == "L":
        z += 1
    elif i == "R":
        z -= 1
    elif i == "F":
        y += 1
    else:
        y -= 1
z = abs(z)
y = abs(y)
g = ((z**2)+(y**2)/2)
print(math.sqrt(g))
