import random
number =random.randint(1,50)
while True:
    num=int(input ("please enter a number you like\nbetween 1 to 50: "))    
    if num>50 or num<0:
        print("please enter again")
    else:
        if num>number:
            print("try a smaller number")
        elif num<number:
            print("try a bigger number")
        else:
            print("BINGO!")
            break