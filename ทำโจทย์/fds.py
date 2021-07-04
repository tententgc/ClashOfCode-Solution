n=int(input())
for i in range(1,100000):
    s=str(i)+str(n)
    summ = sum([int(c) for c in s])
    if (summ==n-i) or (summ==i-n):
        print(i)
        break
    
