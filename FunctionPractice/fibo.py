def fibonac(n):
    res = 0
    a = 0
    b = 1
    count = 1
    while count<=n:
        res = a
        a = b
        b = res+a
        if res < n: # to get upto nth number if want till nth number then remove this if
            print(res)
        else:
            break
        count = count+1

fibonac(33)

        