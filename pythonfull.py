# # this code for print hello 
# print("hello world")

# # add two no
# a=int(input("Enter first number: "))
# b=int(input("enter second no"))
# c=a+b
# print("the sum is",c)


# # to enter int in binary form
# d=0b1010;
# print(d)

# to check boolean data type
# code 1 has output 1
# a=True
# b=False
# c=a+b
# print(c)

# code 2 has output True
# a=10
# b=20
# c=a<b
# print(c)


# string print 
# a="hello world"
# print(a)


# # slicing of string
# k="Arav"

# to print index 0
# print(k[0]) 

# # to print : full string
# print(k[:])

# #  it stat print index with index 1
# print(k[1:])


# # to print till text 
# print(k[:2])


# # to print text in reverse
# print(k[::-1])


# # to print length of string
# print(len(k))

# to print para
# print('''arav
# he is too good''')

# # to print para in reverse
# print('''arav
# he is too good''')

#for print no 1 to 10

# for i in range(0, 11):
#     print(i)


# # for 10 to 1
# for i in range(10,0,-1):
#     print(i)

# to print all even no 1 to 100
# for i in range(2,101):
#     if i%2==0:
#         print(i)

# #  to print od no 1 to 100
# for i in range(1,101):
#     if(i%2!=0):
#         print(i)


# factorial of a no
# n=int(input("enter a no"))
# fact=1;
# for i in range(1,n,1 ):
#     fact=fact*i;

# print(fact)


# to print table

# for i in range(0,71,7):
#     print(i) 

# or 
# n=int(input("enter a no"))
# for i in range (1,11):
#     print(n*i)
#     print('\n')

# while loop
# i=1
# while i<=5:
#     print(i)
#     i=i+1


# type casting
# a=int(input("enter a no"))
# print(float(a))
# print(type(a))
# print(bool(a))



# # to print all prime numbers up to the entered number 
# no = int(input("enter a no: "))

# if no <= 1:
#     print("no prime numbers")
# else:
#     print("prime numbers between 2 and", no, ":")
#     for num in range(2, no + 1):
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)



# bit wise operator
# a=10
# d=12
# b=a>>2
# c=a<<2
# e=0&5
# f=0|0
# print(b)            
# print(c)
# print(bool(e))
# print(bool(f))


# special operator
# identity is
# a=5 is 66
# print(a)
# is not
# a=6 is not 6
# print(a)

# # membership in and not in
# a="arav"
# print('a'in a)
# print("y"not in a)



# # demonstrate the inbuilt data type list tupule set dictionary 
# a=[1,'arya']
# print(type(a))

# b=(1,'arya')
# print(type(b))

# c={1,'arya'}
# print(type(c))

# d={1:'arya'}
# print(type(d))



# examine all arithmetic operator
# a=int(input("enter a no"))
# b=int(input("enter a no 2"))
# print("add",a+b)
# print("sub",a-b)
# print("mul",a*b)
# print("div",a/b)
# print("mod",a%b)
# print("power",a**b)



# wap to find largest of two numbers 
# a=int(input("enter a no"))
# b=int(input("enter a no 2"))
# c= a if a>b else b
# print("largest no is",c)



# wap to find largest of 3 no

# a=int(input("enter a no"))
# b=int(input("enter a no 2"))
# c=int(input("enter a no 3"))

# if( a>b and a>c):
#     print("a is largest ",a)
# elif(b>a and b>c):
#     print("largest no is b",b)    
# else:
#     print("c is largest ",c)    





# compute distance b/w two point
# import math as m
# x1=int(input("enter a no x1 "))
# x2=int(input("enter a no x2 "))
# y1=int(input("enter a no y1 "))
# y2=int(input("enter a no y2 "))

# d=pow((x2-x1),2)+pow((y2-y1),2) 
# print("distance is " ,m.sqrt(d))






# area of circle

# r=int(input("enter a no"))
# pi=3.14
# area=pi*r*r
# print("area of circle is ",area)








# wap to check year is leap or not 
# year=int(input("enter year"))
# if((year%4==0) and (year%100!=0)):
#     print("leap year")
# else:
#     print("not leap year")



# swap 2 no using assignment operator
# x1=int(input("enter a no"))
# x2=int(input("enter a no 2"))
# print("before swap values" ,x1,x2)
# x1,x2=x2,x1
# print("after swap values" ,x1,x2)




# demonstrate all bit wise operator
# a=int(input("enter a no"))
# b=int(input("enter a no 2"))
# print(a & b)
# print(a | b)
# print(a^b)
# print(a<<2)
# print(a>>2)



# wap to for check inn range 1 of 100

# a=int(input("enter a no"))
# if (a in range(0,101)):
#     print("a")
# else:
#     print("try again")    


# wap to enter name with index
# a=input("enter name")
# for i in range(0,len(a)):
#     print(a[i],"=",i)


# while loop
# a=int(input("enter a no"))
# i=10
# while(i!=0):
    
#     print(i)
#     i-=1





# wap to check no for +ve,-ve and  0
# a=int(input("enter a no"))
# if(a>0):
#     print("positive")
# elif(a<0):
#     print("negative")
# else :
#     print("no is 0")        



# wap to calculate electricity bill
# a=int(input("enter no of unit"))
# sum1=0
# sum2=0
# sum3=0
# for i in range(1,a+1):
#     if(i<=100):
#         sum1=sum1+5
#     elif(i<=200):
#         sum2=sum2+7
#     else:
#         sum3=sum3+10


# total=sum1+sum2+sum3  
# print(total)




# # roll the dice game

# print("welcome to roll the dice game ")
# print("if u want to play tap y or n ")
# a=input("enter your choice")
# import random as r

# b=r.randint(0,6)

# if(a=='y'):
#     print("choosing the no")
#     c=int(input(" now u can choose a no between 1 to 6"))
#     if(c==b):
#         print("you won")
#         print("number choose by computer",b)
#         print("thanks for playing")
#     else:
#        print("you lost")
#        print("number choose by computer",b)
#        print("thanks for playing")
# else :
#     print("choose y to play") 




# wap to take single digit no from keyboard and print its english word
# a=int(input("enter a no between 0 to 9"))
# if(a==1):
#     print("one")
# elif(a==2):
#     print("two")
# elif(a==3):
#     print("three")
# elif(a==4):
#     print("four")
# elif(a==5):
#     print("five")
# elif(a==6):
#     print("six")
# elif(a==7):
#     print("seven")
# elif(a==8):
#     print("eight")
# elif(a==9):
#     print("nine")
# else:
#     print("invalid no")



# basic of operation
# a=input("enter a word")
# b=input("enter word 2")
# c=a+b
# print(c)  
# print(len(c)) 
# d=c.lower()
# e=c.upper()
# f=c.capitalize()
# print(d)
# print(e)
# print(f)

# str replace
# a=input("enter a word")
# b=input("enter word 2")
# c=a+b
# print(c)  
# d=str.replace(c,"a","b")
# print(d)
# e=['a','b']
# e.append('c')
# print(e)




#  to print hollow rectangle 
# n = int(input("enter no: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or i == n - 1 or j == 0 or j == n - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
               


# to print 2 vertical parallel lines
# n = int(input("enter no: "))
# for i in range(n):
#     for j in range(n):
#         if(j==1 or j==n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()                
    

# 10 to 1 in reverse order
# for i in range(10,0,-1):
#     print(i)


# to search element in list
# a=[1,2,"arya","arav"]
# search = input("enter element to search: ")

# for item in a:
#     if str(item) == search:
#         print("item found")
#         break
#     else:
#         print("item not found")
#         break




# to print all positive in a list using continue
# a=[1,2,4,5,-2,3,-5,-6]
# for i in range(len(a)):
#     if(a[i]>0):
#          print(a[i])
#          continue
   

# to print all even no between 1 to 100 using while loop
# i=1
# while(i!=101):
#     if(i%2==0):
#         print(i)
#     i+=1    



# cube of no 1 to 10 
# i=1
# while(i!=11):
#     print(i*i*i)
#     i+=1




# to practice loops 

# print * in one line
# n=int(input("enter a no"))
# for i in range(n):
#     print("*",end="")


# to print * in multiple line
# n=int(input("enter a no"))
# for i in range(n):
#     print("*",end="")
#     print("\n")


# to print sq using *
# n=int(input("enter a no"))
# for i in range(n):
#     for j in range(n):
#      print("*",end="")
#     print()


#  to print hollow square
# n=int(input("enter a no"))
# for i in range(n):
#     for j in range(n):
#      if(i==0 or i==n-1 or j==0 or j==n-1):
#         print("*",end="")
#      else:
#         print(" ",end="")
#     print()
 

 
# to print rectangle
# row=int(input("enter a no"))
# col=int(input("enter a no"))
# for i in range(row):
#     for j in range(col):
#         print("*",end="")
#     print("\n")



#   hollow rectangle
# row=int(input("enter a no"))
# col=int(input("enter a no"))
# for i in range(row):
#     for j in range(col):
#         if(i==0 or i== row-1 or j==0 or j== col-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("\n")


#  to print pyramid
# for i in range (1,5):
#     for j in range(1,5-i):
#         print(" ",end="")    
#     for j in range((2*i)-1):
#         print("*",end="")
#     print("\n")    


# reverse pyramid

# for i in range (1,10): 
    
#     for j in range(i):
#         print(" ",end="")       
#     for j in range(2*(9-i)-1):
#         print("*",end="")
#     print("\n")    


#  to print reverse pyramid
# for i in range (1,5):
#     for j in range(1,5-i):
#         print(" ",end="")    
#     for j in range((2*i)-1):
#         print("*",end="")
#     print("\n")  
    
#     for j in range(i):
#         print(" ",end="")       
#     for j in range(2*(9-i)-1):
#         print("*",end="")
#     print("\n")    



#  wap to print both diagonal of sq matrix
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==j or i+j==n+1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("\n")



# wap to print plus pattern
# n=int(input("enter a no"))
# for  i in range (1,n+1):
#     for j in range(1,n+1):
#         if (i==(n//2)+1 or j==(n//2)+1):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()            


# wap to print star pattern right triangle
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()

# #  wap to print star pattern right triangle in reverse
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,n-i):
#         print("*",end='')
#     print()



# wap to print hollow triangle
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         if(j==1 or j==i-1 or i==n):
#          print("*",end='')
#         else:
#            print(" ",end='') 
#     print()


# wap to print revese hollow triangle
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,n-i):
#         if(j==1 or i==1 or j==n-i-1):
#             print("*",end='')
#         else:
#             print(" ",end='')    
#     print()


# wap to print to vertical parallel lines
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j==1 or j==n):
#          print("*",end='')
#         else:
#             print(" ",end='') 

#     print()



# wap to print two horizontal parallel lines
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()



#  wap to print hollow square
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==1 or i==n or j==1 or j==n):
#          print("*",end='')
#         else:
#          print(" ",end='') 
#     print()


#  wap to give grade to student based on marks
# marks = int(input("enter the marks: "))
# if marks >= 90:
#     print("Grade: A")       
# elif marks >= 80:
#     print("Grade: B")       
# elif marks >= 70:           
#     print("Grade: C")       
# elif marks >= 60:   
#     print("Grade: D")
# else:   
#     print("Grade: F")


#  wap to make atm simulation
# print("Welcome to the ATM Simulation")
# print("Please insert your card and enter your PIN.")
# a=input("enter your card and write 'yes' to continue ")
# if(a=='yes'):
#     b=int(input("enter your pin "))
#     if(b==1234):
#         print("Enter the amount you want to withdraw")
#         c=int(input("enter the amount"))
#         if(c<=10000):
#             print("Please take your cash")
#             print("Thank you for using the ATM Simulation")
#         else:
#             print("Insufficient balance")
#             print("recharge your account")
#     else:
#         print("Invalid PIN")
#         print("retry again")
# else:
#     print("Invalid card") 
#     print("retry again")  


# wap to print tringle in no pattern
# no=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(no,end='')
#         no+=1

#     print()


# wap to print diamond patten
# n=int(input("enter a no"))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end='')
#     for k in range(1,2*i):
#         print("*",end='')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,n-i+1):
#         print(" ",end='')
#     for k in range(1,2*i):
#         print("*",end='')
#     print()




# function practice
# def add(a,b):
#     return a+b
# x=int(input("enter a no"))
# y=int(input("enter a no 2"))    
# result = add(x,y)
# print(result)


# print heloo from fn
# def greet(name):
#     print("hello ",name)

# a=input("enter your name")
# greet(a)



# return square of a no 
# def sq(a):
#     return a*a
# x=int(input("enter a no"))
# print("square is ",sq(x) )


# to return  multiple vlaues
# def calc(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div

# w,x,y,z=calc(10,5)
# print(w,x,y,z)    


# positional argument
# def sub(a,b):
#     print(a-b)
# sub(20,10)
# sub(10,20)


# keyword argument
# def sub(a,b):
#     print(a-b)
# sub(b=5,a=10)
# sub(a=10,b=5)    


# default argument
# def wish(a="abhinav"):
#     print("hello",a)
# wish()
# wish("arav")
# note: default argument should be at last in function definition if we are using positional argument and keyword argument in same function call
 

# wap to find factorial of a no using return
# wap to check the given no is even and odd using return
# wap to cal area of rectangle
# wap to cal simple intrest
# wap to cal electicity bill by taking default argument of prize =6 rupee per unit and taking no of unit as input from user




# q1
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# n=int(input("enter a no"))
# print("factorial of ",n,"is ",fact(n))


# q2
# def check(a):
#     if  a%2==0:
#         return "even"
#     else:
#         return "odd"
# a=int(input("enter a no"))
# print("no is ",check(a))



# q3
# def area(l,b):
#     print("area of rectangle is ",l*b)
# l=int(input("enter a length"))
# b=int(input("enter a breadth"))
# area(l,b)    


# q4
# def sim(p,r,t):
#     print("simple intrest =",(p*r*t)/100)
# p=float(input("enter a no"))
# r=float(input("enter a no"))
# t=float(input("enter a no"))    
# sim(p,r,t)    

# q5
# def bill(u,p=6):
#     print("bill is ",u*p)
# u=float(input("enter unit consumed"))
# p=float(input("enter prize"))
# bill(u)
# bill(u,p)



# to print reverse of string
# a="abhinav"
# print(a[::-1])
# print(len(a))

# for i in range (len(a)-1,-1,-1):
#     print(a[i],end='')



# to count no 
# def count(a):
#     ct=0
    
#     while(a>0):
#         a=a//10
#         ct+=1
#     print(ct)    

# a=int(input("enter a no"))
# count(a)



# function that reverse of a number
# def reverse(num): 
#     rem=0
#     rev=0

#     while(num>0):
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10
#     return rev

# k=int(input("enter a no"))
# print(reverse(k))     


# to give variable no of argument 
# def calc(*n):
#     print(n)

# calc()
# calc(10)
# calc(1,2,3,4,5)
  


# wap to print sum of variable no of argument as tuple
# def add (*n):
#     sum=0
#     for i in n:
#         sum+=i
#     print("sum is ",sum)


# add(1,2,3,4,5)



# wap to print variable no of argument in dictionary
# def add (**n):
    
#     print(n)


# add(name="alice",age=10)




# def add (**n):
    
#     print(n)


# add(name="alice",age=10)

# add(name="bob",age=15) 






# wap to find max no using variable no of argument
# def max(*r):
#     no=0
#     for i in r:
#         if(i>no):
#             no=i
#     print(no)        


# max(1,2,3,4,5)

# print ("hello")







# file handling

# f = open('arya.txt','r')
# print(f.read())
# f.close()


# f=open("arya.txt",'a')
# f.write("vaishnav")
# f.close()


# f=open("arya.txt",'r')
# line=0
# while f.readline():
#     line+=1
# print(line)    


# f = open("arya.txt",'r')
# content=f.read()

# f=open("student.txt",'w')
# f.write(content)
# f.close()



# f=open("arya.txt",'r')
# print(f.read())


# f=open("arya.txt",'r')
# line=0
# while f.readline():
#     line+=1
# print(line)
# 
# 

# f=open("abhi.txt",'r')
# print(f.read())    


# f=open("abhi.txt",'r')
# print(f.read())

# f=open("pythonfull.py",'r')
# content=f.read()
# f=open("abhi.txt",'w')
# f.write(content)
# f.close()



# print("hello time changing")
# print("nxt world opening")





# import random as r
# k='no:'
# for i in range(5):
#    print(r.randint(1,10))



# import pickle as p
# f=open("abc.dat",'bw')
# l=[10,11,12,13,14,15,16,17]
# p.dump(l,f)
# f.close()



# f=open("abc.dat",'br')
# d1=p.load(f)
# print(d1)


# f=open("mg.jpeg",'br')
# d1=p.load(f)
# print(d1)


# wap to generate a random pass of 6character length where 1,3,5 th position is alfabet and 2,4,6 are digit 
# import random as r
# l=['a4b5c6','d4e7f8','g7h8k9']
# print(r.choice(l))


# import random as r
# passlen=int(input("enter password length"))
# l=['a','b','c','d']
# for i in range(1,passlen):
#     if(i%2==0):
#         print(r.randint(1,9) ,end=' ')
#     elif(i%2==1):
#         print(r.choice(l),end=' ')


# import random as r
# name=['akash','abhi','arav','asur']
# print("employee name:",end='')
# print(r.choice(name),end='')
# print()
# empno=['e-1234','e-4567','e-3848','e-7737']
# print("employee id:",end='')
# print(r.choice(empno),end='')
# print()
# city=['delhi','bhilwara','up','sirohi']
# print("employee city:",end='')
# print(r.choice(city),end='')
# print()
# desi=['hr','team leader','core member','frontend developer','manager']
# print("employee designation:",end='')
# print(r.choice(desi),end='')
# print()


# print('mobile:',end='')
# print(r.randint(6,9),end='')
# for i in range (1,10):
#    print(r.randint(0,9),end='')
# print()

# print('salary:',end='')
# for i in range(1,9):
#     print(r.randint(1,9),end='')

    
# f=open('mg.jpeg','bw')
# f.write("hello")
# f.close()




# f=open("arya.txt",'a')
# f.write("vaishnav")
# f.close()



# f=open('mg.jpeg','br')
# content=(f.read())
# print(content)
# f.close()






# import random as r
# def name():
#     first=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     name=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
#     print("employee name:",end='')
#     print(r.choice(first),end='')
#     for i in range(1,10):

#         print(r.choice(name),end='')
#     print()

# name()









# import random as r
# def name():
#     name=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     a=" "
#     print("employee name:",end='')
#     for i in range(1,10):

#         a=a+r.choice(name)
#     print(a.title(),end='')  
#     print()

# def empid():
#     empno=['e-1234','e-4567','e-3848','e-7737']
#     print("employee id:",end='')
#     print(r.choice(empno),end='')
#     print()


# def city():
#     city=['delhi','bhilwara','up','sirohi']
#     print("employee city:",end='')
#     print(r.choice(city),end='')
#     print()

# def desi():
#     desi=['hr','team leader','core member','frontend developer','manager']
#     print("employee designation:",end='')
#     print(r.choice(desi),end='')
#     print()

# def mobileno(): 
#     print('mobile:',end='')
#     print(r.randint(6,9),end='')
#     for i in range (1,10):
#        print(r.randint(0,9),end='')
#     print()

# def salary():
#     print('salary:',end='')
#     for i in range(1,7):
#         print(r.randint(1,9),end='')

# for j  in range(1,10):

#     name()
#     empid()
#     city()
#     desi()
#     mobileno()
#     salary()
#     print("\n")






# import math as m
# print(m.sqrt(9))
# print(m.pow(2,3))
# print(m.factorial(5))






# import time as t
# # print(t.ctime())
# print(t.strftime("%H:%M:%S"))



# import time

# print("Hello")
# time.sleep(5)
# print("After 5 seconds")


# import os

# print(os.getcwd())
# print(os.listdir())



# import statistics

# marks = [70, 80, 90, 85, 75]

# print(statistics.mean(marks))
# print(statistics.median(marks))




# import sys

# print(sys.version)
# print(sys.platform)



# import calendar as c
# print(c.month(2026, 3))



# import string
# a=string.ascii_letters
# print(a)


# import getpass
# password = getpass.getpass("Enter password: ")
# print(password)




# import webbrowser
# webbrowser.open("https://google.com")




# import json

# data = '{"name": "Abhi", "age": 20}'

# x = json.loads(data)

# print(x["name"])
# print(x["age"])



# import re

# text = "My number is 9876543210"

# x = re.findall("[0-9]+", text)

# print(x)




# from collections import Counter

# data = ["apple", "banana", "apple", "mango", "apple"]

# print(Counter(data))



# import itertools

# items = ["A", "B", "C"]

# print(list(itertools.combinations(items, 2)))




# import uuid

# print(uuid.uuid4())


# import hashlib

# text = "hello"

# x = hashlib.sha256(text.encode())
# print(x.hexdigest())



# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# f = Fernet(key)

# text = "hello"

# encrypted = f.encrypt(text.encode())
# print(encrypted)

# decrypted = f.decrypt(encrypted).decode()
# print(decrypted)



# import textwrap

# text = "Python is a very easy programming language"

# print(textwrap.fill(text, 10))



# from decimal import Decimal

# a = Decimal("0.1")
# b = Decimal("0.2")

# print(a + b)


# import requests

# url = "https://api.github.com"

# data = requests.get(url)

# print(data.status_code)



# from pathlib import Path

# file = Path("arya.txt")

# print(file.exists())



# print("ramkishan hello ")


# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello sir , how can i help you")
# engine.runAndWait()





# print("hello world")


# class display:
#     def __init__(self):
#         print("name : Arav")
#         print("age : 20")
#         print("branch : cse")
#         print("roll no : 20")


#     def area(self, l, b):
#         print("area of rectangle is ",l*b)    

# obj=display()
# obj.area(10,20)

# class area:
#     def __init__(self,l,b):
       
#         print("area of rectangle is ",l*b)
# obj=area(10,20)        



class movie:
    def __init__(self, title, actor, actress, year):
        self.title = title
        self.actor = actor
        self.actress = actress
        self.year = year

    def display(self, title, actor, actress, year):
        print("movie name is", self.title)
        print("movie actor is", self.actor)
        print("movie actress is", self.actress)
        print("movie year is", self.year)


movies = []

for i in range(5):
    title = input("enter movie name")
    actor = input("enter movie actor")
    actress = input("enter movie actress")
    year = input("enter movie year")
    print("\n")
    movies.append(movie(title, actor, actress, year))

for movie in movies:
    movie.display(title, actor, actress, year)
    print()

print([movie.title for movie in movies])


print ("hel")