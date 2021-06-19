s = input()
z = 9999999999
v=[]
for i in s:
    if ord(i) < z:
        z = ord(i)
        v.append(i)
    else:
        v.append(i)
a = chr(z)
v.pop(a)
print("".join(v))


# s = input()
# m = min([ord(x) for x in s if ord(x) > 90])
# print("".join([x for x in s if ord(x) != m]))
