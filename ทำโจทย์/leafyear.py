def is_leap(y):
    if y % 4 == 0:
        if y%100==0:
            if y%400==0:
                a=True
            else:
                a=False
        else:
            a=True
    else:
        a=False
    return(a)
            

year = int(input())
print(is_leap(year))
