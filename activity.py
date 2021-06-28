n = int(input())
if n%2==1:n+=1
a=b=1
z=n//2 +1
for i in range (z,n+1):a*=i
for i in range (1,z):b*=i
print(a//b)
