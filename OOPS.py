# class= A class is a user-defined blueprint or prototype from which objects are created,its any idea
# object= An Object is an instance of a Class,A class is like a blueprint while an instance is a copy of the class with actual values.
# Object is not an idea anymore, it’s an actual
'''
 ex: The drawing of the house is a class which contains details about door,windows and
 if we construct house using that drawing its like creating object out of class and we can create many houses
'''

'''
An object consists of :

State : It is represented by attributes of an object. It also reflects the properties of an object.
Behavior : It is represented by methods of an object.
 It also reflects the response of an object with other objects.
Identity : It gives a unique name to an object and enables one object to interact with other objects.

example:

identity====name of dog
state/attributes ====breed,age,colour,weight
behavior==== bark,sleep,eat
'''

class Dog():

    # defining 2 attributes

    attribute1='dog'
    attribute2=20

    # defining simple method

    def fun(self):
        print('i am a',self.attribute1)
        print('my weight is',self.attribute2)

# creating an object using Dog class
dog1=Dog()
dog2=Dog()

# accessing attributes and methods through object

Dog.fun(dog1)    # same as line 46

print(dog1.attribute2)
dog1.attribute1
dog1.fun()
dog2.fun()

'''
# __init__ method

1)The __init__ method is similar to constructors in C++ and Java. 
2)Constructors are used to initialize the object’s state (variables)
3) init method will be called automatically,need not to call explicitly like other methods
4) for every object we create init will be called automatically
5)The __init__ method gets called when memory for the object is allocated:

'''

class Employee():

    # init method
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # new method
    def hello(self):
        print('my name is {} and my salary is {}'.format(self.name,self.salary))

# object creation
e1=Employee('sri',10)
e2=Employee('muki',20)

print(e1.name)   # we need not to use self as we are calling using object name
print(e2.salary)
e1.hello()   # method caling
e2.hello()

class A:
    def __init__(self,name,age):
        self.n=name    # n will be the attribute class A is having
        self.a=age      # a can be anything and that will become the attribute

a1=A('sri',20)

#  its preferred to have same name for convention in self....self.name=name
'''
self
1)self represents the instance of the class.
2) By using the “self” keyword we can access the attributes and methods of the class in python
3)It binds the attributes with the given arguments.

class variables or static variables

1)Class or static variables are shared by all objects
2)variables which are assigned a value in class declaration are class variables.
3)declared inside class and outside class methods
4) class variables can be invoked using either class or object name

instance variables or non static variables

1)instance or non-static variables are different for different objects (every object has a copy of it).
2)And variables which are assigned values inside class methods are instance variables.
'''

class CseStudent:
    stream='CSE'     # class or static variable

    def __init__(self,name,id):    # instance or non static variables
        self.name=name
        self.id=id

s1=CseStudent('sri',101)
s2=CseStudent('muki',102)
print(s1.name)
print(s2.stream)         # invoked using object name
print(CseStudent.stream)    # class variable can be invoked using either class or object name

# updating static and non static variables

class Dog:
    kingdom='mamal'

    def __init__(self,colur,age):
        self.colour=colur
        self.age=age
        Dog.kingdom='animal'    # updating static / class variable inside constuctor


d1=Dog('white',10)
d2=Dog('red',20)
d1.age=15              # updating non static variable
Dog.kingdom='nayi'   # updating static variable
print(d1.kingdom)
print(Dog.kingdom)
print(d2.age)
print(d1.age)

# deleting static and non static varaibles
# static variable can be deleted inside method/constuctor  (syntax  ; del self.variable
#static variable can be deleted outside method/constuctor  (syntax  ; del obeject reference.variable
# non static variable can be deleted inside method/constuctor  (syntax  ; del classname.variable


class Dog:
    kingdom='mamal'

    def __init__(self,colur,age):
        self.colour=colur
        self.age=age


    def delete(self):
        del self.age

#del Dog.kingdom     # deleting static variable using class name
d1=Dog('white',10)
d2=Dog('red',20)

print(d1.__dict__)   # to represent attributes in dictionary form
d1.delete()
print(d1.__dict__)
print(d2.kingdom)
print(Dog.__dict__)


class Employee:
    emp_count = 0
    loc = 'Bangalore'

    def __init__(self, first, age, salary):
        self.first = first
        self.age = age
        self.salary = salary
        Employee.emp_count += 1
# # to keep count of objects created since init method called every time objects craeted
    def info(self):
        return 'i am {1} and i am {0} old and my salary is {2}'\
            .format(self.age, self.first, self.salary)

e1 = Employee('sri', 20, 50000)
e2 = Employee('muki', 30, 60000)
Employee.emp_count

Employee.loc='Chennai'     # we can update class level variable with class name

e1.loc='Kolar'    # e1 objects value will become kolar rest other objects will point same class var
'''
Types of methods
1)instance methods
2)class methods
3)Static methods

instance methods

1)deals with instance variables
2)An instance method receives the self as implicit first argument
3)instance method is related to the object of the class
4)need an object to call instance method

Syntax:

class C(object):

    def fun(self, arg1, arg2, ...):
       ....


class methods

1)Deals with class level variables
2)A class method receives the class as implicit first argument, 
just like an instance method receives the instance
3)A class method is a method which is bound to the class and not the object of the class.
4)It can modify a class state that would apply across all the instances of the class. 
For example it can modify a class variable that will be applicable to all the instances.
5)@classmethod function decorator is used
6)we can call the class method without object

Syntax:

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.

static method

1)Doesnt deals with neither instance nor class variables
2)A static method does not receive an implicit first argument.
3)A static method is also a method which is bound to the class and not the object of the class.
4)A static method can’t access or modify class state.
5)@staticmethod function decorator is used
6)when a method doesnt deals either with instance or class variables we can use

Syntax:

class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.
'''
class Student:
    school='VTU'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):    # self is used
        avrg=(self.m1+self.m2+self.m3)/3
        print(avrg)

    # class method
    @classmethod
    def schoolinfo(cls):
        print('student is from scholl {}'.format(cls.school))

    # static method
    @staticmethod
    def info():
        print('welcome to VTU')

s1=Student(56,68,74)
s2=Student(86,48,34)

print(s1.school)
print(s2.school)
print(s2.m2)
print(Student.school)
print(Student.info())

# class method can be used as alternative to constructor
class A:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    @classmethod
    def from_str(cls,s):
        n,s=' '.join(s).split(' ')   # coverting list to string and splitting string
        return cls(n,s)    # returning object of A
a=A.from_str(['sri','20'])

a.__dict__  # {'name': 'sri', 'sal': '20'}

# inner class in python

'''
if without exsting one type of object if 
there is no chance of exsting other type of object we can go for inner class concept

ex1: engine cant exists without car
ex2: head cant exists without human

class Outer:
    class Inner:
        def m1(self):
        pass
        
o=Outer()     # creating object of outer class
i=o.Inner()   # creating object of inner class 
i.m1()
'''

class Person:
    def __init__(self,name):
        self.name=name
        self.dob=self.DOB()

    def display(self):
        print('name :',self.name)
        self.dob.display()

    class DOB:
        def __init__(self):
            self.dd=8
            self.mm=7
            self.year=1994

        def display(self):
            print('DOB id= {}/{}/{}'.format(self.dd,self.mm,self.year))

p=Person('sri')
p.display()
dob=Person.DOB()
dob.display()
# help(Person)            # to get more help


