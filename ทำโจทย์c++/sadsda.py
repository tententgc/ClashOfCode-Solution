n=int(input())
for i in range(n):
    a=input().split("/")
    if "jpg" or "png" in a:
        print(a[0])
    else:
        print(a)
