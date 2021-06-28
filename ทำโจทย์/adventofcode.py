z=[]
while True:
    x=int(input())
    if x==1662:
        break
    else:
        z.append(x)
z.sort()
print(z[0]*z[-1])