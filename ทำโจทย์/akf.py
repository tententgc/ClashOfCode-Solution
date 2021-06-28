n = input()
z = []
y = 0
for i in n:
    if i.isalpha():z.append(ord(i))
    else:y+=1
if sum(z)% 2 == 1:y += 1
print(y)
