import random as r
def name():
    name=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    a=" "
    print("employee name:",end='')
    for i in range(1,10):

        a=a+r.choice(name)
    print(a.title(),end='')  
    print()

def empid():
    empno=['e-1234','e-4567','e-3848','e-7737']
    print("employee id:",end='')
    print(r.choice(empno),end='')
    print()


def city():
    city=['delhi','bhilwara','up','sirohi']
    print("employee city:",end='')
    print(r.choice(city),end='')
    print()

def desi():
    desi=['hr','team leader','core member','frontend developer','manager']
    print("employee designation:",end='')
    print(r.choice(desi),end='')
    print()

def mobileno(): 
    print('mobile:',end='')
    print(r.randint(6,9),end='')
    for i in range (1,10):
       print(r.randint(0,9),end='')
    print()

def salary():
    print('salary:',end='')
    for i in range(1,7):
        print(r.randint(1,9),end='')

for j  in range(1,10):

    name()
    empid()
    city()
    desi()
    mobileno()
    salary()
    print("\n")




