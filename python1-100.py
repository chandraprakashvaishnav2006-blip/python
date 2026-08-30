# 1_program
# print("Hello, World!",7)
# print(5)

# \r move cursor to the beginning 
# print("hello \rhi")
# output: hillo


# \b backspace
# print("hello\bhi")
# output: hellhi

# to seperate the values with a custom separator, we can use sep parameter in print function
# print( "Hey", 6, 7, sep="~")
# output: Hey~6~7


# end parameter is used to specify what to print at the end of the output. By default, it is a newline character.   
# print( "Hey", 6, 7, sep="~", end="009")
# print("hardik")



# 14 types of data types in python
# a1=2
# a2=3.5
# a3="hello"
# a4=True
# a5=2+3j
# a6=[1,2,3]
# a7=(1,2,3)
# a8={1:2,3:4}
# a9={1,2,3}  
# a10=None
# a11=bytearray(5)
# a12=bytes(5)
# a13=frozenset([1,2,3])
# a14=range(5)
# print(type(a1))
# print(type(a2))
# print(type(a3))
# print(type(a4))
# print(type(a5))
# print(type(a6))
# print(type(a7))
# print(type(a8))
# print(type(a9))
# print(type(a10))
# print(type(a11))
# print(type(a12))
# print(type(a13))
# print(type(a14))


# make calculator using if else in python
# a=int(input("Enter first number: "))
# b=int(input("enter no 2: "))
# c=input ("Enter operator: ")
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)    
# elif c=="*":
#     print(a*b)
# elif c=="/":
#     print(a/b)
# else:
#     print("Invalid operator")

# to print all string function
# a="hello world"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("world", "universe"))
# print(a.split())
# print(a.find("world"))
# print(a.capitalize())
# print(a.replace("hello","hi"))
# print(a.count("l"))
# print(a.title())
# print(a.startswith ("hello"))
# print(a.endswith("world"))
# print(a[0])


# multiline string
# a=""" heloo world"""
# for characters in a:
#     print(characters)

# for item in a:
#     print(item)    


# question
# nm="arnav"
# print(nm[-4:-2])
 

#  slicing in python
# a="arav"
# print(a[:])
# print(a[:6])
# print(a[:1])
# print(a[::-1])
# print(a[-1:-5:-1])


# center fn
# a="hello"
# print(a.center(20," "))
# print(a.center(20,"*"))


# if else in py
# # q1
# a=int(input("enter a no"))
# print("value of a is", a)
# if(a>18):
#     print("eligible for vote")
# else:
#     print("not eligible for vote")    


# greet user with respect to time
# import time
# t=time.strftime("%H")
# d=(int(t))
# print("time is ",d)
# print(type(d))
# if(d<12):
#     print("good morning")
# elif(d>12 and d<17):
#     print("good afternoon")

# elif(d>17 and d<19):  
#     print("good evening")     

# elif(d>19):
#     print("good night")



# match case code in python
# print("1.addition\n2.subtraction\n3.multiplication\n4.division")
# a=int(input("enter your case"))

# b=int(input("enter first number"))
# c=int(input("enter second number"))
# match a:
#     case 1:
#         print("add",b+c)
#     case 2:
#         print("sub",b-c)    
#     case 3:
#         print("mul",b*c)
#     case 4:
#         print("div",b/c)    


# for loop ex
# for i in range(1,11):
#     print(i)


# while loop ex
# i=1
# while(i<=5):
#     print(i)
#     i=i+1


# len fn uses in loops
# name="python"
# for i in range(len(name)):
#     print(name[i])


# enumerate() fn ex
# fruits=['apple','banana','cherry']
# for index,fruit in enumerate(fruits):
#     print(index,fruit)


# zip fn ex
# a=["ram","shyam"]
# b=[90,95]
# for i,j in zip(a,b):
#     print(i,j)


# reversed fn
# for i in reversed(range(5)):
#     print(i)


# sorting of list
# numbers = [5, 2, 4, 1]

# for i in sorted(numbers):
#     print(i)


# for code ex
# a="arav"
# for i in reversed(a):
#     print(i)


# more ex
# a=[1,2,3,4,5]
# for i in a:
#     print(i)


# while code ex
# i=1
# while(i<=5):
#     a=int(input("enter a no"))
#     print(a)
#     i+=1


# ex 2
# a=5
# while(a>0):
#     print(a)
#     a-=1
# else:
#     print("no is less than 0")f

# emulate do while 
# i= 0
# while True:
#     print(i)
#     i = i + 1
#     if(i%100 == 0):
#         break


# argument of fn
 

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
 


import calendar as c
year=int(input  ("enter year"))
month=int(input("enter month"))
print(c.month(year,month))
