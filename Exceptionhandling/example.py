def takenumber():
    while True: # it never gets break until we mention in else block
        try:
            num = int(input("please enter a valid number--> "))
        except:
            print("Ohh no this is not a number. Please check again")
            continue
        else:
            break
        finally:
            print("Thanks")
takenumber()