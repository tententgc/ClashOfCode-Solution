keep = int(input("your test score = "))
while True:
    while keep > 30 or keep < 0:
        print("sorry it's not true pls repeat one more times")
        break
    midterm = int(input("your midterm score = "))
    while midterm > 30 or midterm < 0:
        print("sorry it's not true pls repeat one more times")
        break
    final = int(input("your final score = "))
    while final > 40 or final < 0:
        print("sorry it's not true pls repeat one more times")
        break

    result = keep + midterm + final
    if result<0:
        break
    if result in range(80, 100):
        print("A")
    elif result in range(75, 79):
        print("B+")
    elif result in range(70, 74):
        print("B")
    elif result in range(65, 69):
        print("C+")
    elif result in range(60, 64):
        print("C")
    else:
        print("F")
    