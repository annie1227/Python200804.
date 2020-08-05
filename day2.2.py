number=int(input("please enter a number: "))
a=2
while a<number:
   if number%a==0:
        print("not prime number")
        break 
        a=a+1
if a==number:
        print("prime number")
    
