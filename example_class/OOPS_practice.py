# #Q.1 Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
# # distance = square root ((x2-x1)2 + (y2-y1)2)
# # slope = (y2-y1)/(x2-x1)
# class Line:
    
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
    
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return (((x2-x1)**2 + (y2-y1)**2)**.5)
    
#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2
#         return (y2-y1)/(x2-x1)

# coordinate1 = (3,2)
# coordinate2 = (8,10)

# li = Line(coordinate1,coordinate2)
# print(li.distance())
# print(li.slope())

# #Q.2 Fill in the below class
# # V= π**r*h
# # A =2πrh + 2π**r

# class Cylinder():

#     def __init__(self,rad=1,height=1):
#         self.rad = rad
#         self.height = height

#     def volume(self):
#         return (self.height*3.14*(self.rad)**2)
    
#     def surface_area(self):
#         top = 3.14 * (self.rad)**2
#         return (2*top) + (2*3.14*self.rad*self.height)

# c = Cylinder(3,2)
# print(c.volume())
# print(c.surface_area())

# Q.3 create a bank account class that has two attributes:

#     owner
#     balance

# and two methods:

#     deposit
#     withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Bank_account():
    
    def __init__(self,owner,balance):

        self.name = owner
        self.total_amt = balance

    def deposit(self, dep_amt):

        self.dep_amt = dep_amt
        self.total_amt = self.total_amt + self.dep_amt
        return(f'now total bal is: {self.total_amt}')
    
    def withdraw(self,deducted_amt):

        self.deducted_amt = deducted_amt
        if (self.deducted_amt < self.total_amt):
            self.total_amt = self.total_amt - self.deducted_amt
            return (f'now total bal is: {self.total_amt}')
        else:
            return('Withdraw amount is exceeding more than Total Balance ')

    def __str__(self):
        return f'owner name is : {self.name} and total balance is : {self.total_amt}'

acct = Bank_account('Megha', 5000)
print(acct)
print(acct.deposit(1000))
print(acct.withdraw(7000))

print(__name__)
