n = int(input())
z = input()
y = input()
max_num = n
i = 0
while i < max_num:
    i += 1
    space = max_num - i
    for s in range(space):
        print(y, end='')

    for n in range(1, (max_num - space) + 1):
        print(z, end='')

    for n in reversed(range(1, i)):
        print(z, end='')
 

    print("")
