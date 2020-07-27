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

# Q.4 Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers

arr = [5,2,-1,3,-4,6,1,-3,-2]
a= [1, -6, 4, 2, -1, 2, 0, -2, 0]

def 

if __name__=='__main__':
  print(three_sum(arr))
  print(three_sum(a))
