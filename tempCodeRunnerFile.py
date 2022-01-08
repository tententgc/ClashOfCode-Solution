g=0
for i in range(int(input())+1):
    q = input()
    z =[0]
    for i in q:
        if z[-1]=="/" and i =="/\/":
            z.append(i)
            g+=1
        else:
            z.append(i)
print(g)
        