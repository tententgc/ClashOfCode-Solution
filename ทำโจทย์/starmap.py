n = int(input())
z = n-4
a = ("-*-")
a1 =("*-*")
a2=("*---*")
if n==1:
    print(a)
elif n==2:
    print(a)
    print(a1)
elif n==3:
    print(a)
    print(a1)
    print(a1)
else:
    print(a)
    print(a1)
    for i in range(z):
        print(a2)
    print(a1)
    print(a)