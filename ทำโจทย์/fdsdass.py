text = input()
v = ""

for i in range(len(text)-1):
    v += text[i] + " "*(abs(ord(text[i])-ord(text[i+1])))

v += text[-1]

print(v)
