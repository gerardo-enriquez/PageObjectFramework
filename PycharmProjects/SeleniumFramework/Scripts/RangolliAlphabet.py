def print_rangoli(size):
    l = []
    alphabet = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m',
                   '14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y',
                   '26':'z'}
    for e in range(1,size+1):
        x = str(e)
        s = alphabet.get(x)
        l.append(s)

    # Calculate middle line width
    maxletters = ((len(l)-1) * 2)+1
    maxsymbol = maxletters-1
    maxwidth = maxletters + maxsymbol
    letterPerLine = size

    rl = []
    rl2 = []
    for x in range(1,maxletters+1):
        counter = int(x)
        counter = -counter
        if x <= size:
            for y in range(counter, 1):
                if y == 0:
                    if len(rl) == 1:
                        print(rl[0].center(maxwidth, "-"))
                        rl = []
                    else:
                        for r in range(counter+1, 1):
                            if r == 0:
                                pass
                            else:
                                rl.insert(0, l[r])
                        rl2 = "-".join(rl)
                        print(rl2.center(maxwidth, "-"))
                    rl = []
                else:
                    rl.append(l[y])
        if x > size:
            for y in range(-1,-letterPerLine,-1):
                rl.append(l[y])
            for t in range(-letterPerLine+2, 0):
                rl.extend(l[t])
            rl2 = "-".join(rl)
            print(rl2.center(maxwidth, "-"))
            letterPerLine -= 1
            rl = []


print_rangoli(2)