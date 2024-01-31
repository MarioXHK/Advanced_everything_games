cases = int(input())

for i in range(cases):
    year = int(input())
    a = year%19
    b = year%4
    c = year%7
    k = year//100
    p = (13+8*k)//25
    q = k//4
    m = (15-p+k-q)%30
    n = (4+k-q)%30
    d = (19*a+m)%30
    e = (2*b+4*c+6*d+n)%7
    f = (11*m+11)%30
    day = 22+d+e
    month = "Undecember"
    if day <= 31:
        month = "march"
    if day > 31:
        day -= 31
        month = "april"
    if day == 25:
        day = 18
    elif day == 26:
        day = 19

    print(year,month,day)