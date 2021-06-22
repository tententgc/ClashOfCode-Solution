c = 0
for i in range(int(input())):
    c += sum(map(int, str(i))) == 10
print(c)
