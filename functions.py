# functions

def oddEven(x):   # function defination
    if x%2==0:
        print('even')
    else:
        print('odd')

oddEven(10)   # function calling
#oddEven(10,20)   # error only one argument accepts



def isPrime(n,m):
    a=m*n
    b=m/n
    return a,b

x,y=isPrime(20,10)
print(x,y)


#  positional arguments
#number of arguments and order should be same

def sum(a,b):
    c=a+b
    return c
res=sum(10,20)
print(res)

# keyword arguments
# order is not important
# number of parameters should be same

def add(x,y):
    z=x+y
    return z
res=add(y=10,x=20)    # order is not important
print(res)

#Default arguments

def sum(a,b=10):     # always default arguments should come at the end
    c=a+b
    print(c)
sum(40)
sum(40,60)   # overrides default value

# variable length argument
# if we are not sure about the number of arguments then we can use variable ength
# working mechanism is based on tuple concept

def varlength(*args):
    print(args)
    for i in args:
        print(i)
varlength(10,20,30)
varlength()           # creates empty tuple

# variable length arguments can be mixed with normal arguments
def sum(i,*j):
    print('normal arg is =',i)
    print('var length arg is =', *j)
    for x in j:
        print(x)

sum(10,20,30)       # i takes 10 as normal variable

# program to find product of variable length
def product(*a):
    res=1
    for i in a:
        res*=i
    print(res)
product(1,2,3,4,5)

# key value pair variable length arguments (**kwargs)
# working mechanism is based on dictionary concept

def sum(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)

sum(k1=10,k2=20,k3=30)
sum()                    # creates empty dictionary

# **kwargs can be mixed with normal arguments

def sum(i,**j):    # normal should be always **kwargs
    print('normal argument is',i)
    print('**kwargs argument is', j)

sum('hi',name='sri',age=25)

# global variable vs local variable

# local variable
# variable defined inside function,cant be used outside

def sum():
    p=10       # local variable
    print(p)
sum()
#print(p)  # error

# global variable
x=20
def g():
    print('inside function =',x)
g()
print('outside function =',x)

# global variable vs local variable in same function

num=100
def f():
    num=200
    print('inside function',num)   # prints 200
    print('global variable inside function =',globals() ['num']) # to call global variable inside function
f()
print('outside function',num)     # prints 100

# global keyword
# used to create global variable inside function

def f():
    global s    # makes s as global variable
    s=50
    print('inside function =',s)
f()
print('outside function =',s)

# example

nums=10     # global variable
def f():
    print('inside f() =',nums)
f()

def g():
    nums=20          # local variable
    print('inside g() =',nums)
g()
print('outside g() =',nums)

def m():
    global nums           # updating nums
    nums=30
    print('inside m() =', nums)
m()
print('outside m() =', nums)

# global scope
print('global =', nums)

'''
 pass by reference vs pass by value

# x = [10]
#[10 ] is the  list,
# x is a variable that points to the  list, but x itself is not the empty list
#Consider the variable (x, in the above case) as a box,
# and 'the value' of the variable ( [10] ) as the object inside the box.

 PASS BY REFERENCE:

The box from the calling function is passed on to the called function.
Implicitly, the contents of the box (the value of the variable) is passed on to the called function.
Hence, any change to the contents of the box in the called function will be 
reflected in the calling function.

PASS BY VALUE:

A new box is created in the called function, 
and copies of contents of the box from the calling function is stored into the new boxes.
'''
'''
# PASS BY OBJECT REFERENCE (Case in python):

#f you pass immutable arguments like integers, strings or tuples to a function,
# the passing acts like Call-by-value

#f you pass mutable arguments like list, dictionary  to a function,
# the passing acts like Call-by-reference

def append_one(li):
    li.append(1)
x = [0]
append_one(x)
print x

Here, the statement x = [0] makes a variable x (box) that points towards the object [0]

On the function being called, a new box li is created. 
The contents of li is the SAME as the contents of box x. Both the boxes contain the same object. 
That is, both the variables point to the same object in memory. Hence,
any change to the object pointed at by li will also be reflected by the object pointed at by x.

In conclusion, the output of the above program will be:

[0, 1]

If the variable li is reassigned in the function, then li will point to a seperate object in memory.
x however, will continue pointing to the same object in memory it was pointing to earlier.

Example:

def append_one(li):
    li = [0, 1]
x = [0]
append_one(x)
print x
The output of the program will be:

[0]
'''
'''
# recursive function

# In programming terms a recursive function
# can be defined as a routine that calls itself directly or indirectly.

#recursive function program to find factorial

import sys
sys.setrecursionlimit(2000)   # to set higher recursion limit
print(sys.getrecursionlimit())
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(10)
print('factorial is =',result)

# lambda function
# This function can have any number of arguments
# but only one expression, which is evaluated and returned.

# normal function to find cube

def cube(n):
    print('using normal function =',n**3)
cube(10)

# above program using lambda
cube=lambda n:n**3
print('using lambda',cube(5))

# note ; lambda always takes one expression or condition
# program to find max of 3 nums
max=lambda a,b,c:a if a>b and a>c else b if b>c else c
print('max is =',max(100,20,30))


'''
'''
n=int(input('enter number'))
check = {True: "Weird", False: "Not Weird"}

print(check[n%2==1 or n in range (6,21)])
'''
'''

def fibonacci(n=int(input('enter the number'))):
    a=0
    b=1
    if n<=0:
        print('pease enter valid number')
    else:
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n+1):

                c=a+b
                a=b
                b=c
                if c>100:
                    break
                print(c)
fibonacci()

'''
# filter()
#The filter() method filters the given sequence
# with the help of a function that tests each element in the sequence to be true or not.
# takes 2 parameters first one is function and second one as iterable(list,tuple)

def f(n):
   return n%2==0

res=f(10)
print(res)

nums=[10,11,12,13,14,16,15]
evens=list(filter(f,nums))    # using user defined function
print(evens)

# same program using lambda funtion

even=list(filter(lambda x:x%2==0,nums))
print('using lambda function',even)


# map() function returns a map object(which is an iterator) of the results
# after applying the given function to each item of a given iterable (list, tuple etc.)
# for every input value generates output
# syntax is map(funtion, iterable)
# map(f, iterable)  is same as [f(x) for x in iterable]

# NOTE : You can pass one or more iterable to the map() function.

def add(x):
    return x+x

res=add(5)
print(res)

t=[10,20,30,40]
sum=list(map(add,t))    # using user fuction
print('using user defined function',sum)

# using lambda

nums={1,2,3,4,5}
squares=set(map(lambda x:x*x,nums))
print(squares)

# program to add 2 lists using map and lambda

l1=[1,2,3]
l2=[4,5,6]

result=list(map(lambda a,b:a+b,l1,l2))    # here we passed more than one iterable (l1 and l2)
print('addition of 2 list using map and lambda =',result)

# # map() can listify the list of strings individually

l = ['sat', 'bat', 'cat', 'mat']
test=map(list,l)
print(list(test))    # [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]

a=' '.join(map(str,l))      # converting list to string
print(type(a))
print(a)

# reduce() in Python

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result
# and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

from _functools import reduce
l1=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l1))    # sum of the list

# to find maximum number in list
l1=[1,2,3,4,5,6]
print(reduce(lambda a,b:a if a>b else b,l1))

# import operator function and use built in add,sub and mul methods

from operator import *

print(reduce(add,[10,20,30,40,50]))   # addition
print(reduce(sub,[10,20,30,40,50]))    # substarction
print(reduce(mul,[10,20,30,40,50]))    # multiplication


'''
accumulate()
1)similar to reduce but gives list of interrmidate results
2)gives iterator containing intermidate results
3)imported from itertools
syntax is 
    itertools.accumulate(iterable,function)
'''
l=(1,2,3,2,5,4)
from itertools import *
for i in accumulate(l,add):
    print(i)
# 1 3 6 8 13 17
