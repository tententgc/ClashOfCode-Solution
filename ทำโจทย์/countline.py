a = 0
b = 0
c = 0
d = 0
num = int(input())
for i in range(num):
    line = input()
    b += line.count(" ")
    c += line.count(":")
    d += line.count(";")
    a += len(line)
b1 = b//4
b2 = b % 4
b = b1+b2
print(((a-b)-c)-d)
