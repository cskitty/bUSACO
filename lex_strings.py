def rearrangedString(olds):
    s = ""
    for x in olds:
        if x.isalpha() or x.isdigit():
            s += x

    s = sorted(s)
    i = 0
    d = {}
    while i < len(s):
        try:
            d[s[i]] += 1
        except:
            d[s[i]] = 1
        i += 1
    reversedD = {}
    for k in d:
        try:
            reversedD[d[k]] += k
        except:
            reversedD[d[k]] = str(k)
    r = False
    output = ''
    for k in sorted(reversedD.keys(), reverse=True):
        output += str(k)
        for item in sorted(reversedD[k], reverse=r):
            output += item
        output += ","
        if r:
            r = False
        else:
            r = True

    return output[:-1]