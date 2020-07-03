

# Q.1)Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
splittedlist = st.split(' ')
findst ='s'

for letter in splittedlist:
    if letter.startswith('s'):
        print(letter)

for word in splittedlist:
    if word[0].lower()=='s':
        print(word)

# to find s anywhere
for word in splittedlist:
    for char in word:
        if char=='s':
            print(word)
#to find substr
for word in splittedlist:
    if (word.find('ord')!=-1):
        print(word)

#Q.2) Use range() to print all the even numbers from 0 to 10.
print(list(range(0,11,2)))
res = [num if num%2==0 else 'odd' for num in range(25)]
print([num if num%2==0 else 'odd' for num in range(25) if num%3==0])
print(res)

#note- In List comprehension it starts from last mentioned condition like in second example its starts from 
# if num%3==0 which filter out the data or change the data
# second if statement num%2==0 don't change the data just apply condition and return values.
# first if statement always needs else condition otherwise it will through syntax error, because condition always comes in last 
# which we use to modify data

#Q.3) Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([num for num in range(1,51) if num%3==0])

#Q.4) Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
spltstr = st.split()
for word in spltstr:
    if (len(word)%2 == 0):
        print('Even length of word-',word)
#Q.5) Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    for j in range(10):
        if(i%3==0):
            print('fizz')
            break
        elif(i%5==0):
            print('buzz')
        elif(i%3==0 and i%5==0):
            print('fizzbuzz')
        else:
            pass
#Q.6) Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])

#Q.7) Give an array of n length contains 1 to 99. print last 2 digit of result after multiplying all n numbers in array
num = [23,56,12,56]
res = 1
for i in num:
    res = res * i
res = str(res)
print(res)
print(res[-2:])

#Q.8) remove duplicates from an array
arr = [1,1,1,1,2,3,234,45]
arr2 = arr.copy()
newarr =[]
for i in arr2:
    if(arr.count(i) > 1):
        arr.remove(i)
print(arr)

for i in arr:
    if i not in newarr:
        newarr.append(i)
print(newarr)

print(list(dict.fromkeys(arr))) 
# Note- Dictionaries in Python cannot include duplicate keys, and so if we convert our list to a dictionary, 
# it will automatically remove any duplicate values.
# fromkeys() is a built-in function that generates a dictionary from the keys you have specified.  
# because dictionaries cannot include duplicate keys, the function will also remove any duplicate values from our list. 
# Then, we can convert our dictionary back to a list.
print(list(set(arr)))

#Q.9) fibonacci serires upto n

num = int(input('Enter the number:'))
a=0
b=1
if(num == 0):
    print(a)
elif(num ==1):
    print(a,b)
else:
    print(a,b,end=' ')
    for i in range(2,num):
        c = a+b
        print(c,end=' ')
        a = b
        b = c

