a=int(input())
q=[]
for i in range(a): 
    if i==0 or i==a-1:
        q.append("#"*a)
    else:
        q.append("#"+" "*(a-2)+"#")
for i in q:
    print(i)
