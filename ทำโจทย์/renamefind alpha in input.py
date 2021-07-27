i = input().lower()
c="abcdefghijklmnopqrstuvwxyz"
l=[]
for x in c :
    if x not in i:
        l.append(x)
if l == [] : print("Pangram")
else : print(*l)
