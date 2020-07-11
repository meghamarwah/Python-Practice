# Define a function called myfunc which returns a list of those arguments whose are even

def myfunc(*args):
    return [x for x in args if x%2==0]

print(myfunc(2,45,6,12,3))

# Define a function called myfunc that takes in a string and returns a matching string where every even letter is uppercase
#and every odd letter is lowercase.\

def myfunc(val):
    st=''
    count = 1
    for i in val:
        if count%2==0:
            st=st+i.upper()
        else:
            st=st+i.lower()
        count = count+1
    return st
print(myfunc('megha marwah'))

# Prime number
def primenum(num):
    for n in range(2,num):
        if num % n == 0:
            return ('not prime')
    else:                      # this else block indentation is same as for loop instead if block bcz it helps to check all posibilities of prime number 
        return ('prime')
print(primenum(9))
# if we pass number as 2 it won't go inside loop bcz in this case range's start and stop value will be same (2,2) which makes false condition 
# as range works stop-1==>2-1

# Q.1)  Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def myfunc(num1,num2):
    if (num1 % 2 == 0 and num2 % 2== 0):
        return min(num1,num2)
    else:
        return max(num1,num2)
print(myfunc(36,10))

#Q.2) Write a function takes a two-word string and returns True if both words begin with same letter

def myfunc(str1):
    word = str1.split()
    return (word[0][0]==word[1][0])
print(myfunc('megha marwah'))

#Q.3 Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def myfunc(num1,num2):
    return ((num1+num2 == 20) or num1==20 or num2==20)
print(myfunc(2,15))

#Q.4 OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    updatedname=''
    for i in range(0,len(name)):
        if (i==0 or i ==3):
            updatedname= updatedname+name[i].upper()
        else:
            updatedname= updatedname+name[i]
    return updatedname
print(old_macdonald('meghamarwah'))
#----OR----
def old_macdonald2(name2):
    if len(name2) > 3:
        return name2[:3].capitalize() + name2[3:].capitalize()
    else:
        return 'Name is too short!'
print(old_macdonald2('meghamarwah'))

#Q.5 MASTER YODA: Given a sentence, return a sentence with the words reversed
def masteryoda(sent):
    word = sent.split()
    return ' '.join(word[::-1])
print(masteryoda('megha marwah is a software tester'))

#q.6 return a count of occurrences of a character/sentence eg:aaabbnn--> a3b2n2 
def countofcharfunc(sentence_val):
    newdict = dict()
    strval = ''
    for i in sentence_val:
        newdict[i]=newdict.get(i,0)+1
    for k,v in newdict.items():
        strval = strval + f'{k}{v} '
    return strval
print(countofcharfunc('my name is megha'))

#Q.7 display most popular URL's survey which was recently conducted for N users. for every user , you are given one url which they have visited. 
#the popularity of url is directly propotional to the no of visits to that url.
# write a program to sort the url in decrease order of popularity.

def url_visit(**user):
    print('input data----> ',user)

    url_dict=dict()
    for key in user.values():
        url_dict[key] = url_dict.get(key,0)+1
    print('url values with count----->  ',url_dict)
   

    def dictvalue(urldata):
        return url_dict[urldata] 
    # above function returns dictionary value eg: url_dict['flipkart']=3

    # return(sorted(url_dict, key=lambda data: url_dict[data], reverse=True))
    return(sorted(url_dict,key=dictvalue, reverse=True)) 
    #sorted() is a built-in function that accepts an iterable(list,str,dictionary,tuple) and returns the sorted values in ascending order by default which contains the iterable items.
    # Both sort and sorted have three keyword arguments: cmp, key and reverse. Where Key should be a function which takes an item and returns a vlaue
    # to compare to sort elements
    # Urldict = iterable (dictionary), key = dictvalue function which returns dictionary values but inside sorted function it's passed as parameter
   

print(url_visit(ram='flipkart',shyam='amazon',abc='flipkart',xyz='flipkart',megha='netflix',naresh='netflix'))



a = [76,4,1,2]
print(a.sort())
print(a) 
# Here sort is a method which accept self value as a parameter, here class is list and obj of list is "a" so by default this list is considered 
# as a parameter for sort() method.

#Q.8) Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.eg: arr=[1,3,3]

def find33(arr):
    for i in range(0,len(arr)):
        if (arr[i:i+2]==[3,3]):
            return True
    return False

print(find33([1,2,3,6,3]))

#Q.9 PAPER DOLL: return a string, from given string which contains some characters  3 times
def PaperDoll(str):
    val = dict()
    data=''
    for i in str:
        val[i] = val.get(i,0)+1
    print(val)
    for k,v in val.items():
        if val[k]==3:
            data = data + f'{k}'
    return(data)
print (PaperDoll('specific character needs to search'))

#q.10 Char Update: Given a string, return a string  for every single character ,three same characters

def CharUpdate(str):
    char=''
    for i in str:
        char = char+i * 3
    return char
print(CharUpdate('Megha'))

#Q.11 BlackJack:Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def BlackJack(a,b,c):
    total = sum((a,b,c))
    if (total <= 21):
        return total
    elif(total <= 31 and 11 in (a,b,c)): 
        # Here total should be 21 even after deducting 10 also so we added 10 into that and compare whether it's lesser or equal to 31 
        return (total-10)
    else:
        return 'BUST'
print(BlackJack(2,11,34))

#Q.12 SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 
#(every 6 will be followed by at least one 9). Return 0 for no numbers.

def another(num):
    total=i=0
    while i<len(num):
        if num[i]!=6:
            total=total+num[i]
            i = i+1
        elif num[i] == 6:
            while num[i]!=9:
                i = i+1
            i=i+1
    return total


print(another([2,6,7,8,9,10,1,6,7,8,9,5]))

#Q.13 SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def Spy_game(numlist):
    i=j=0
    count0=0
    updatedlst = []

    while(i<len(numlist)):
        if (numlist[i]!=0 and numlist[i]!=7):
            i=i+1
        elif (numlist[i] == 0):
            updatedlst.append(numlist[i])
            i=i+1
        elif (numlist[i] == 7):
            updatedlst.append(numlist[i])
            i=i+1
    print(updatedlst)
    while(j<len(updatedlst)):
        if (j<len(updatedlst) and updatedlst[j]==0):
            j=j+1
            count0=count0+1
            if (j<len(updatedlst) and updatedlst[j]==7 and count0>=2 ):
                return True
            elif(j<len(updatedlst) and updatedlst[j]==7 and count0<2):
                j=j+1
            elif (j==len(updatedlst)):
                return False
            
            
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1


def spy_game_nk(nums):
    return True if "007" in ''.join(str(x) for x in nums if x in [0,7]) else False

if __name__ == "__main__":
    print(spy_game_nk([0,1,2,7,0,0, 0, 7]))




