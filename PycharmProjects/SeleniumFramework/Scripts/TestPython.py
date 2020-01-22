def logo (n,m):
    c = ".|."
    mhalf = (((m+1)-len(c)) // 2)
    nhalf = ((n-1) // 2)
    counter = 0
    w = "WELCOME"
    fill = "-"
    for i in range(n):
        if i < nhalf:
            print((i*c).rjust(mhalf,fill)+c+(i*c).ljust(mhalf,fill))
            counter = i
        if i == nhalf:
            print(w.center(m,fill))
        if i > nhalf:
            print((counter * c).rjust(mhalf, fill) + c + (counter * c).ljust(mhalf, fill))
            counter -=1


logo(9,27)