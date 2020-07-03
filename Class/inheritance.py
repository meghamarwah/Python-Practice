class Parent():
    name='abc'

    def __init__(self, fname, lname):
        self.name=fname
        self.last_name =lname

    def print_name(self):
        print(self.name,self.last_name)

class Kid(Parent):

    def __init__(self,fname,lname):
        Parent.__init__(self,fname,lname)
        print('in a kid class')
        
    def print_name(self):
        print('kid class method')

if __name__ == '__main__':
    obj1 = Kid('Megha','Marwah') # once create an obj of kid class __init__ get called automatically
    obj1.print_name() # if we have created a same name method in both (base/derived) class in this case derived class method override this method.


# If we are defining __init__ method inside child class then it overrides Parent's __init__, so to access Parent class method 
# we have to use Parent.__init__()