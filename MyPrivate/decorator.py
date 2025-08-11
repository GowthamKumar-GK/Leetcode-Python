def College(n):
    def NAAC():
        print("Nandha Engineering  College")
    return NAAC


@College
def location():
    print("located in Erode")
location()
