#q.1Write a function that computes the volume of a sphere given its radius.
# sphere = (4/3) *(22/7)*r*r*r
def vol(rad):
    return (4/3)*(3.14)*(rad**3)

#q.2 Write a function that checks whether a number is in a given range (inclusive of high and low)

def rang(num,low,high):
    #return (f'{num} is in range' if num in range(low,high+1) else print('not in range'))
    return num in range(low,high+1)

#q.3 Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters
def uppandlow(string):
    Ucount=0
    Lcount=0
    for i in string:
        if i.isupper()==True:
            Ucount+=1
        elif i.islower()==True:
            Lcount+=1
    return f'Upper case letters count->{Ucount}, Lower case letters count->{Lcount}'

#q.4 Write a Python function that takes a list and returns a new list with unique elements of the first list.
def new_old(lst):
    return list(set(lst))

#Q.5 Write a Python function to multiply all the numbers in a list.
def mul(lst):
    res = 1
    for num in lst:
        res = res*num
    return res

#Q.6 Write a Python function that checks whether a word or phrase is palindrome or not.
def pal(wrd):
    # newwrd=''
    # for i in wrd:
    #     newwrd=i+newwrd
    # if newwrd == wrd:
    #     return('palindrome')
    # else:
    #     return('not palindrome')
    return wrd[::-1]==wrd
 
#Q.7 Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string

def pangram(sentence,alphabet=string.ascii_lowercase):
    setalpha = set(alphabet)
    sentlow = sentence.lower()
    sentspace = sentlow.replace(' ','')
    setsent = set(sentspace)
    if setsent == setalpha:
        return 'pangram'
    else:
        return 'not pangram'



if __name__=='__main__':
    print(pangram('The quick brown fox jumps over the lazy dog'))
