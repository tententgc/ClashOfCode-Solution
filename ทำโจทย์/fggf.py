n = int(input())
z = []
k=[]
j = 0
while True:
    a = input()
    if a == "py" or a == "mp4":
        k.append(a)
        break    
    else:
        z.append(a)
print("/".join(z[0:])+"."+k[0])

