# Q.1 Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))

# Q.2 Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import random
charlist = ['a','e','i','o','u']
random.shuffle(charlist)
print(''.join(charlist))

# Q.3 Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

numlist = [10,20,30,40,50,60,70,80,90]
i = 0
j = 2
while (numlist!=[]):
  i=i+j
  while i >= len(numlist):
    i = i - len(numlist)
  print(numlist.pop(i))

# Q.4 Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.

txt = 'Hi this is megha world, megha is a software test engineer..'
txt_list = txt.split()
txt_occurence = dict()
for word in txt_list:
  txt_occurence[word] = txt_occurence.get(word,0)+1
print(txt_occurence.items())

# Q.5 Write a Python program to count the number of each character of a given text of a text file.

with open("C:\\Users\\Megha\\Desktop\\txtfile.txt",'r') as filedata:
# filedata = open("C:\\Users\\Megha\\Desktop\\txtfile.txt",'w+')
# if filedata.mode == 'w+':
  # filedata.write("hi this is new data.")
  content = filedata.read()
  print(content)
  filedata.close()