# a = input()
# v=["0","1","2","3","4","5","6","7","8","9"]
# z=[]
# for i in a:
#     if i not in (v):
#         z.append(i)
# print("".join(z))


n = input()
a = ""
for i in n:
    if i.isalpha() or i == " ":
        a += i
print(a)
