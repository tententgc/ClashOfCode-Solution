import math
a,b =[int(x) for x in input().split()]
if a>b:
    print(2)
else:
    print (math.ceil(b/a))