
for i in range (1,5):
    for j in range(1,5-i):
        print(" ",end="")    
    for j in range((2*i)-1):
        print("*",end="")
    print("\n")  
    
    for j in range(i):
        print(" ",end="")       
    for j in range(2*(9-i)-1):
        print("*",end="")
    print("\n")    