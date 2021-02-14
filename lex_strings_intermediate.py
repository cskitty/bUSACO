def rearrangeString(s, n):
    d = {}
    i = 0
    counter = 1
    while i  < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            counter += 1
        else:
            try:
                d[counter].append(s[i] * counter)
            except:
                d[counter] = [s[i] * counter]
            counter = 1
        i += 1

    print(d)
    ns = ""
    prevC = " "
    prevS = 0
    for k in sorted(d.keys(), reverse=True):
        for item in sorted(d[k]):
            if k > n and not (item[0] == prevC[0] and len(item) + prevS > n):
                ns += n * item[0]
                prevS = n
                prevC = n * item[0]

            elif item[0] == prevC[0] and len(item) + prevS >= n and not k > n:
                ns += (n - prevS) * item[0]
                prevS = n
                prevC = n * item[0]

            elif item[0] == prevC[0] and len(item) + prevS >= n and k > n:
                prevS = n
                prevC = item

                pass

            else:
                ns += item
                if item[0] == prevC[0]:
                    prevS = prevS + len(item)
                else:
                    prevS = len(item)
                prevC = item

            print(ns, item, prevS, prevC)


    return ns
print(rearrangeString("MISSISSIPPI", 3))