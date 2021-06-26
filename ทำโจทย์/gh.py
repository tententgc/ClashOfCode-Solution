n = int(input())
line = input()
z=[]
y=[]
for i in line:
    z.append(i)
for i in input().split():
    x=int(i)
    print(z[x-1],end="")