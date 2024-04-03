def main():
    distType = "p"
    while not distType in ("k", "m"):
        distType = input("What kind of distance do you want? American miles (m) or bri'ish Kilometers (k)?\n").lower()
    distance = int(input("How far are you going?"))
    if distType == "m":
        m = distance
        k = m*1.60934
    else:
        k = distance
        m = k*0.621371
    print("Distance in miles:", m, "\nDistance in kilometers:", k)
    time = m/15
    print("it'll take about", int(time), "hours to get there.")
    mtime = time*60
    a = 1+0.15*mtime
    if mtime <= 5:
        b = 2.5
    else:
        b = 2.5+0.12*mtime-5
    c = 5+0.06*mtime
    print("Costs!")
    print("Company A:", a)
    print("Company B:", b)
    print("Company C:", c)
    comps = [a,b,c]
    most = [0,'a']
    for i in comps:
        if i > most[0]:
            most[0] = i
            if most[0] == a:
                most[1] = "A"
            elif most[0] == b:
                most[1] = "B"
            elif most[0] == c:
                most[1] = "C"
    least = [999999999,'a']
    for i in comps:
        if i < least[0]:
            least[0] = i
            if least[0] == a:
                least[1] = "A"
            elif least[0] == b:
                least[1] = "B"
            elif least[0] == c:
                least[1] = "C"
    print("The company with the cheapest offer is", least[1], "with", least[0], "dollars of cost!")
main()