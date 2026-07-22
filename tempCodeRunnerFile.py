
print("welcome to roll the dice game ")
print("if u want to play tap y or n ")
a=input("enter your choice")

b=r.randint(0,6)

if(a=='y'):
    print("choosing the no")
    c=int(input(" now u can choose a no between 1 to 6"))
    if(c==b):
        print("you won")
        print("number choose by computer",b)
        print("thanks for playing")
    else:
       print("you lost")
       print("number choose by computer",b)
       print("thanks for playing")
else :
    print("choose 