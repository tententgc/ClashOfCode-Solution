n= input().lower()
a= int(input())
z=[]
if a>26:print("ERROR")
else:
    for i in range(a):
        if n=="upper":z.append(chr(65+i))
        else:z.append(chr(97+i))
    print(" ".join(z))