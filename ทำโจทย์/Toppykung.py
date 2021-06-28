n = int(input())
z=[]
for i in range(n):z.append(input())
q = list(dict.fromkeys(z))
q.sort()
for i in q:
    print(i)
