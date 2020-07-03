class Snake:
    name='xyz'  # This is Class Object Attribute, here we have defined the attribute and it's value .
    # and we can't create different objects of this class with different values for same attribute

s = Snake()


class Snake2():
    name='xyz'
    def __init__(self,color,height):   # This is User Defined Attributes, here we can create multiple objects of class to initialize 
        #diferent values to attributes
        self.c=color
        self.h=height
obj1 = Snake2('Black',10)
obj2 = Snake2('Gray',20)

if __name__ == '__main__':
    print(obj1.name)
    print(obj2.name)
    print(obj1.c)
    print(obj2.c)
    #print(s.name)
