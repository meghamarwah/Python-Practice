def fibo_till_n(n):
    res = 0
    a = 0
    b = 1
    while res<=n:
        res = a
        a = b
        b = res+a
        if res <= n: 
            print(res)
        else:
            break


def fibo_first_n(num):
    res = count = 0
    a = 0
    b = 1
    while (count<num):
        res = a
        a = b
        b = res + a
        print(res)
        count = count + 1


if __name__ == '__main__':
    fibo_till_n(2)
    fibo_first_n(2)