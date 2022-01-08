g=0
for i in range(int(input())):
    q = input()
    z =[0]
    m=[]
    for j in q:

        if z[-1]=="/" and  j == "\\":
            z.append(j)
            g+=1
        else:
            z.append(j)
print(g)
        
        
