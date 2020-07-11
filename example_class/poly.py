class Dog():

    def __init__(self,name):
        self.n= name

    def speak(self):
        return (self.n+" says woof!!")

class Cat():
    
    def __init__(self,name):
        self.n=name
    
    def speak(self):
        return (self.n+" says meaw!!")

def pet_voice(pet):
    print(pet.speak())

bruno = Dog('Bruno')
kitty = Cat('Kitty')

pet_voice(bruno)
pet_voice(kitty)

class A():
    #a = 10
    def __init__(self,name):
        print('inside A:',name)

class B(A):
    def __init__(self, name):
        print('inside B:',name)

Aobj = A('megha')
Bobj = B('neha')
