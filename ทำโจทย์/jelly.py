a,b,c = [int(x) for x in input().split()]
count=0

while(a != 1):
    a //=2
    count += 1
while(b != 1):
    b //=2
    count += 1
while(c != 1):
    c //=2
    count += 1
print(count)
        
