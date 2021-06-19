n = int(input())
for i in range(n):
    t = input().split(':', 3)
    ti = (int(t[0])*3600)+(int(t[1])*60)+int(t[2])
    h = int(ti/3600)
    ti %= 3600
    m = int(ti/60)
    ti %= 60
    print(f"{h: 02}: {m: 02}: {ti: 02}")
