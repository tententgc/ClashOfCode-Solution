import math
a, b = input().split()
a = float(a)
b = float(b)
c = math.sqrt((a**2) + (b**2))
print('%.6f' % c)
