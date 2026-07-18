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
# if(year%400==0)or(year%4==0 and year%100!=0):
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

