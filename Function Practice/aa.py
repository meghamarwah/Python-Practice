def url_visit(**user):
    print('input data----> ',user)

    url_dict=dict()
    for key in user.values():
        url_dict[key] = url_dict.get(key,0)+1
    print('url values with count----->  ',url_dict)

def primenum(num):
    for n in range(2,num):
        if num % n == 0:
            return ('not prime')
    else:                      # this else block indentation is same as for loop instead if block bcz it helps to check all posibilities of prime number 
        return ('prime')
print(primenum(9))

def prime_upto_num(num):
    n = 2
    count = 0
    primenum = []
    while(count < num):
        isprime = True
        for i in range(2,n):
            if n%i == 0:
                isprime = False
                break
        else:
            count = count+1
            primenum.append(n)
        n = n+1
    return primenum 

print(prime_upto_num(5))