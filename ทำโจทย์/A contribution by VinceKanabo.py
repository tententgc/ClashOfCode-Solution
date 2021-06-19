a = [int(x) for x in input().split()]
if (a[0]+a[1]==a[2]+a[3]):
    print("+ +")
if (a[0]+a[1] == a[2]-a[3]):
    print("+ -")
if (a[0]-a[1] == a[2]+a[3]):
    print("- +")
if (a[0]+a[1] == a[2]*a[3]):
    print("+ *")
if (a[0]*a[1] == a[2]+a[3]):
    print("* +")
if (a[0]*a[1] == a[2]*a[3]):
    print("* *")
if (a[0]-a[1] == a[2]-a[3]):
    print("- -")
if (a[0]-a[1] == a[2]*a[3]):
    print("- *")
if (a[0]*a[1] == a[2]-a[3]):
    print("* -")
else:
    print("-1")