import random
number =random.randint(1,10)
num=int(input ("please enter a number you like\nbetween 1 to 10: "))
if num>10 or num<0:
    print("please enter again")
elif num==number:
    print("BINGO!")
else:
    print("you're wrong!")
    
