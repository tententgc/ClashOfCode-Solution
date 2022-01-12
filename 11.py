w=sum(ord(i)for i in input())
print(*((w*i)%256 for i in[1,2,3,4]),sep='.')