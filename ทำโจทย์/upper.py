# for i in input():
#     if i.isupper():print(i, end="")

# import re
# print(re.sub('[^A-Z]', '',input()))


print(''.join(c for c in input()if c.isupper()))
