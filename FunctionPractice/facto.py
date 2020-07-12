class Fact():
    
    def __init__(self,n):
        self.n = n

    def mul(self):
        self.fact = 1 
        for i in range(1,self.n+1):
            self.fact = self.fact * i
        return self.fact

factobj = Fact(6)
print(factobj.mul())
            

