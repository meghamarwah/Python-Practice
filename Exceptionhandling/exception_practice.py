import math
#Q.1 Handle the exception thrown by the code below by using try and except blocks.
#for i in ['a','b','c']:
#    print(i**2)

def listnum():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print("You are making a square of alphabets.")
    finally:
        print('Thanks')

#Q.2 Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
# x = 5
# y = 0
# z = x/y
def div():
    x = 5
    y = 0
    try:
        z = x/y
    except ZeroDivisionError:
        print("can't divide")
    finally:
        print("Thanks for trying")
    
#Q.3 Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def numsquare():
    while True:
        try:
            num = int(input("Enter a valid number--> "))
        except:
            print("Plase check again this is not a valid format.")
            continue
        else:
            print("square of num-",int(math.pow(num,2)))
            break
        finally:
            print("Thanks")


if __name__ == '__main__':
    numsquare()