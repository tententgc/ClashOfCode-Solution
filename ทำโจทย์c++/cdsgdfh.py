a = input()
b = int(input())
c = int(input())
g = b+c
q = (b*100)/g
q = str("{:.1f}".format(q))
d = [Hydrochloric, Sulfuric, Nitric, Citric]
if a in d:
    print(q+"%", a, "Acid")
else:
    print(q+"%", "Unknown", "Acid")
