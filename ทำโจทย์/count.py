z = [0,0, 0, 0, 0, 0, 0, 0, 0, 0]
y =[0,1,2,3,4,5,6,7,8,9]
for i in range(5):
    a = int(input())
    z[a] += 1
for i in range(10):
    if z[i]>=4:
        print(y[i])
