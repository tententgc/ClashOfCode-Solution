a = int(input())
b = str(a)
if a <= 24:
    if b[0]==b[1]:
        print(b[0]+b[1]+":"+b[0]+b[1])
    else:
        print(b[0]+b[1]+":"+b[0]+b[1], (b[0]+b[1]+":"+b[1]+b[0]))
else:
    print("NONE")
