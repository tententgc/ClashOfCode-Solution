import sys
a,b,c = [int (x) for x in input().split()]
for i in range(1, 101):
    for j in range(1, 101):
        if i*j==a:
            for x in range(-100,101):
                for y in range (-100,101):
                    if x*y==c and (i*y) + (j*x) == b:print(i,x,j,y);sys.exit()
print("No Solution")



