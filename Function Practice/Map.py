from pytest_practice.app import mysum


def myfunc(*numbers):
  for num in numbers:
    return num**2

# print(myfunc(1,2,3,4))

# def square(num):
#     return num**2
# # Return only uses inside function and using map built in method we can use written functions and map on provided values
# #inside map we don't use () as map takes values as parameters
# val=[1,2,3,4]
# for i in map(square,val):
#     print(i) 

# print(list(map(square,val)))
# #print(map(square,val))--> returns <map object at 0x000001D0EA6F0B70>

# #Lambda--> one time use anonymous function, can never reference again
# even= lambda num: num%2==0
# print(even(6))

# sq = lambda n : n**2
# print(sq(4))

# print(list(map(lambda num:num**2,val)))
print(__name__)
if __name__ == "__main__":

    print(mysum(2,2))

# we use __name__ bcz there are few statements which we want to run only in current file but if we are importing any function/file that moment __Name__ 
# value would be differ as in same file it returns __main__ 
# but when we are accessing this into another file in that case it returns file name which would be differ ,as per need we can apply 
# conditional statements on this


