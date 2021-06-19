distance = int(input())
time = int(input())
velocity = int(input())
fuel = int(input())
fuel_consumption = int(input())
a = distance/time
b = distance/fuel_consumption
if a <= time:
    print("Failure, Not enough fuel")
if b <= fuel:
    print("Failure, Not enough time")
else:
    print("Welcome to Mars")
