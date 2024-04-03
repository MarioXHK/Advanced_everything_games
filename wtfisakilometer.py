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
main()