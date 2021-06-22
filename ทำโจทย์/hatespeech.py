s = input().split()
words = input().lower().split()
r = []
for e in s:
    if e in words:
        r += ["*"*len(e)]
    else:
        r += [e]
print(*r)
