# count = int(input())
# z = []
# for i in input().split():
#     n = int(i)
#     z.append(n)
# for i in z:
#     if i%2 == 0:
#         print("[ ]", i)
#     else:
#         print("[x]", i)
z= []
c = int(input())
for i in input().split():
    n = int(i)
    z.append(n)
for i in range(c):
    if z[i] % 2 == 1:
        print("[x]", z[i])
    else:
        print("[ ]", z[i])
