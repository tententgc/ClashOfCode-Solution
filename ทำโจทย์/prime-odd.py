n = int(input())
z=[]
for i in range(n):
    x=int(input())
    if x % 2 == 1:z.append("T")
    elif x == 2:z.append("T")
    else:z.append("F")
for i in z:print(i)
