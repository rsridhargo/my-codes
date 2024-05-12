'''
Polymorphism in Python

What is Polymorphism : The word polymorphism means having many forms.
In programming, polymorphism means same function name (but different signatures)
being uses for different types.

there are 4 ways of implementing polymorphism
1) duck typing
2)operator over loading
3)method overloading
4)method overriding
'''

'''

Duck typing:
1)Duck Typing is a type system used in dynamic languages
2)where the type or the class of an object is less important than the method it defines.
3)Using Duck Typing, we do not check types at all. Instead, 
we check for the presence of a given method or attribute.
4)“If it looks like a duck and quacks like a duck, it’s a duck”
5)no matter whatever the type of object if it has the method we are intended then we can use
6)python gives more importance to method /attributes (BEHAVIOUR) of an object than original type of object.
'''

class Duck:
    def quack(self):
        print('quack quack...')

class Dog:
    def quack(self):
        print('Dog also quacks like quack quack...')

'''
def invoke_quack(object):
    # Non pythonic code
    if isinstance(object,Duck):
        object.quack()

    else:
        print('To quack the object has to be duck')
'''
def invoke_quack(object):
    #  pythonic code         # we will not check instance if of Duck or type
        object.quack()

d1=Duck()
d2=Dog()
invoke_quack(d1)
invoke_quack(d2)   # passing object should have quack method

'''
If the desired method is not present in passing object then it throws error.

Easier to ask forgiveness than permission (EAFP)
'''

class Duck:
    def quack(self):
        print('quack quack...')

class Dog:
    def bark(self):
        print('Dog also barks like quack quack...')

'''
def invoke_quack(object):
    # Non pythonic code
    if hasattr(object,'quack'):    # to check if object has attribute quack
        if isinstance(object,Duck):
            object.quack()

    else:
        print('To quack the object has to be duck')
'''
def invoke_quack(object):
    #  pythonic code         # we will not instance if of Duck or type
    try:                      # handling with an exception
        object.quack()

    except AttributeError as e:
        print(e)

d1=Duck()
d2=Dog()
invoke_quack(d1)
invoke_quack(d2)

'''
Operator Overloading in Python

1)Operator Overloading means giving extended meaning beyond their predefined operational meaning.
2)For example operator + is used to add two integers as well as join two strings and merge two lists. 
3)It is achievable because ‘+’ operator is overloaded by int class and str class.
4)You might have noticed that the same built-in operator or function 
5)shows different behavior for objects of different classes, this is called Operator Overloading.
6) when we use + operator it invokes magic function __add__ is automatically invoked 
in which the operation for + operator is defined.

'''

print(10+20)   # used to add 2 integers
print('hello' + 'world')   # used to concatenate 2 strings
print(5*2)        # multiply of 2 number
print('sri'*2)     # prints twice of sri

# to oveload + operator

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    # oveloading __add__ built in method
    def __add__(self, others):
        m1 = self.m1 + others.m1
        m2 = self.m2 + others.m2
        s4 = Student(m1, m2)
        return s4

s1=Student(50,60)
s2=Student(65,50)
s3=Student(35,50)
s4=s1+s2+s3
print(s4.__dict__)

# # to oveload * operator

class Employee:
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2 = s2

    # oveloading __mul__ built in method
    def __mul__(self, other):
        #s1=self.m1+other.s1
        return (Employee(self.s1*other.s1,self.s2*other.s2))

    def __str__(self):                              # to print object in printable form
        return ('{},{}'.format(self.s1,self.s2))    # otherwise it will print class name and address



e1=Employee(10,20)
e2=Employee(15,30)
e3=e1*e2
print(e3)
# magic function __str__ will print the object in printable form
# (otherwise objects address will be printed

# to overload < operator

class Student:
    def __init__(self,marks):
        self.marks=marks

    # overloading < operator

    def __lt__(self, other):
        if self.marks<other.marks:
            return True
        else:
            return False

s1=Student(55)
s2=Student(95)
if s1<s2:
    print('s1 is smaller than s2')
else:
    print('s1 is greater than s2')

# to overload / operator

class A:
    def __init__(self,sal):
        self.sal=sal

    # overloading / operator
    def __truediv__(self, other):
        return (A(self.sal/other.sal))

    '''
    def __truediv__(self, other):      # same as above
        sal=self.sal/other.sal
        a3=A(sal)
        return a3  '''

    # to overload __str__ magic function
    def __str__(self):
        return '{}'.format(self.sal)

a1=A(1000)
a2=A(500)
a3=a1/a2
print(a3)

# we can override len() and del methods too

'''
Method Overloading
multiple methods with same name but with different parameters

1)Like other languages (C++) do,python does not supports method overloading.
2)We may overload the methods but can only use the latest defined method.
'''

# method overloading in python by setting default none values to arguments

class Sum:
    def __init__(self):
        pass

    def sum(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            s=a+b+c+d
        elif a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s=a
        return s
s1=Sum()
print(s1.sum(10,20,30,40))
print(s1.sum(10,20,30))
print(s1.sum(10,20))
print(s1.sum(10))

# method overloading in python using variable length arguments (*args)

class A:
    def product(self,*args):
        total=1
        for i in args:
            total=total*i
        print('product of entered integers is=',total)


a=A()
a.product(1,2,3,4)

'''
Method Overriding 

Method overriding is an ability of any object-oriented programming language 
that allows a subclass or child class to provide a specific implementation of a
method that is already provided by one of its super-classes or parent classes

1)if the method is present in both parent and child class with same parameters then 
parent class method is overriden by child
2)if the object of parent class is used to invoke the overriden method then 
parent class method will execute
3)if the object of child class is used to invoke the overriden method then 
child class method will execute
4)we can invoke parent method using super() or classname
'''

class Parent:
    def show(self):
        print('Inside parent class')

class Child(Parent):
    def show(self):
        super().show()      # invoking parent class method too
        print('Inside child class')

p=Parent()
c=Child()
p.show()    # parent class show will be invoked
c.show()    # child class show will be invoked






