c = 0
n = int(input())
for i in range(n):
    k = input().split()

    if not ('apple' in k or 'apples' in k):
        continue

    for i in k:
        if i.isnumeric():
            c += int(i)

print(c)
