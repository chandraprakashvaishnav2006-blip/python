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

# membership in and not in
a="arav"
print('a'in a)
print("y"not in a)