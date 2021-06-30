import math
z=[]
y=[]
g=[]
def print_factors(x):
       for i in range(1,x+1):
           if x%i==0:
              z.append(i)

num =int(input())
print_factors(num)
for i in z:
    g = math.sqrt(i)
    if g % 1 == 0:
        y.append(i)
for i in y:
    g
