n = int(input())
l = ['-'*((n-1)//2)+'*'+'-'*((n-1)//2)]
for i in range(1, n-1, 2):
    l.append('-'*((n-i)//2-1) + '*' + '-'*i + '*' + '-'*((n-i)//2-1))
if n % 2 == 1:
    l = l[:-1]+l[::-1]
else:
    l = l+l[::-1]
for e in l:
    print(e)
