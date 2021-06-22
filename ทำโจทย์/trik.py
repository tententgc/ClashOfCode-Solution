a = input()
n = [1, 0, 0]
c=1
for i in a:
    if(i == 'A'):
        n[0], n[1] = n[1], n[0]
    if(i == 'B'):
        n[1], n[2] = n[2], n[1]
    if(i == 'C'):
        n[0], n[2] = n[2], n[0]
for i in n:
    if i==1:
        print(c)
    c+=1