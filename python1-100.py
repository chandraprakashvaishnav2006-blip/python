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
