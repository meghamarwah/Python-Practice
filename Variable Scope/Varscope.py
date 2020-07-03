# Global Scope
name = 'Hi This is Global area'
def test1():
    # Enclosing function scope
    name = 'Hi This is Enclosing Function area'
    def test2():
        # Local scope
        name = 'Hi This is Local area'
        print(name)
    test2()

def test3():
    # Local reassignment on Global variable using global keyword
    global name
    name = 'actual value got changed now!'
    print('updated val of name is:',name)


if __name__ == '__main__':
    test1()
    print(name)
    test3()
    print(name)
