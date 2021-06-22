import datetime
d, m = [int(n) for n in input().split(' ')]
time = datetime.datetime(2009, m, d)
print(time.strftime('%A'))
