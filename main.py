import random
randNo=random.randint(1,100)
guess=0
a=None
while(randNo!=a): 
 guess=guess+1
 a=int(input("your guess"))
 if(a>randNo):
     print("Number is lower")
 if(a<randNo):
     print("No. is higher ")
 if(a==randNo):
     print(a)
     print(guess)
