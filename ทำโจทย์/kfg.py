n = int(input())
p = []
for i in range(n):
    row = input()
    p.append(row)
for i in p:
    for x in i:
        if x == '0':
            print("-", end ='')
        else:
            print(x, end='')
    print()
