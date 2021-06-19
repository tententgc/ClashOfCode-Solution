s = input()
z = []
for i in str(s):
    z.append(i)
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        z.pop()
print("".join(z))

