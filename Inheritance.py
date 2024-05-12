'''
Inheritance in Python

Inheritance is the capability of one class to derive or inherit the properties from some another class.
The benefits of inheritance are:
1) It represents real-world relationships well.
2)It provides reusability of a code. We don’t have to write the same code again and again. Also,
it allows us to add more features to a class without modifying it.
3)It is transitive in nature, which means that if class B inherits from another class A,
 then all the subclasses of B would automatically inherit from class A.
4) class from which we are deriving another class is called super / parent class and other sub /child
'''

class A:
    def __init__(self,name):
        self.name=name
        print('A constructor')

    def info(self):
        print('welcome')

class B(A):                 # B is sub class of A
    def __init__(self,age,city):
        self.age=age
        self.city=city
        print('B constructor')


a1=A('sri')
b1=B(25,'bangalore')
b1.info()

# constructor in inheritance

# we have to invoke constructor of super class.
# if we create object in sub class then sub class constructor will be called
# if constructor is not present in sub class then parent class constructor will be called
# If we forget to invoke the __init__() of the parent class then
# its instance variables would not be available to the child class.
# super() is used to call all methods of parent class

class A:
    def __init__(self,name):
        self.name=name
        print('In A construction')

    def info(self):
        print('name is=',self.name)

class B(A):
    def __init__(self,age,city):
        self.age=age
        self.city=city
        print('In B construction')
        super().__init__('sri')        # super() is used call parent class methods

    def info(self):
        super().info()    # super() is used to call parent class method
        print('age is {} and city is {}'.format(self.age,self.city))

b1=B(25,'mangaluru')
print(b1.__dict__)      # printing b1 details in dictionary form
b1.info()

# only parameters from parent class init method should be passed inside super init
'''

Different forms of Inheritance:

1)Single inheritance
When a child class inherits from only one parent class, it is called as single inheritance
'''
class A():
    def show1(self):
        print('show of A')

class B(A):
    def show2(self):
        print('show of B')

b=B()
b.show1()
b.show2()

'''
2) Multiple inheritance
When a child class inherits from multiple parent classes, it is called as multiple inheritance.
Unlike Java and like C++, Python supports multiple inheritance.
 We specify all parent classes as comma separated list in bracket.
'''

class Parent:
    def show1(self):
        print('show() of parent')

class Child1:
    def show2(self):
        print('show() of child1')

class Child2(Parent,Child1):
    def show3(self):
        print('show() of child2')

c2=Child2()
c2.show1()
c2.show2()
c2.show3()

# if both parent class have same name method then based on priority it will execute
# If Class C(A,B) then methods of A will be executed first followed by B

'''
3) Multilevel inheritance 
When we have child and grand child relationship.
'''

class A:
    def __init__(self,a):
        self.a=a

    def square(self):
        print('square of a is =',self.a**2)

class B(A):
    def __init__(self,b):
        self.b=b
        super().__init__(5)

    def cube(self):
        print('cube of b is =',self.b**3)
        super().square()

class C(B):
    def __init__(self,c):
        self.c=c
        super().__init__(10)

    def product(self):
        print('product of b and c is',self.b*self.c)
        super().cube()

b=B(10)
c=C(15)

c.product()

# We can make instance variables of parent class as private by adding 2 underscore

'''
class A:
    def __init__(self,x,y):
        self.__x=x              # both x and y are private to child class
        self.__y=y
        print('In class A')

class B(A):
    def __init__(self):
        super().__init__(10,20)
        print('In class B',self.x+self.y)    # x and y are private cant be accessed by child

b=B()

'''

class Animal:
    def __init__(self):
        print('hi welcome')

    def info(self,a):
        print('i am in animal class',a)

class Dog(Animal):
    def __init__(self):
        print('i am in sub class')

    def info1(self, a):
        print('i am in  animal class', a)
        super().info(a*2)              # a value is doubled here and same reflects in info method

d=Dog()
d.info1(15)


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('in constructor A')

    def info(self):
        return 'i {} and am {} old'.format(self.name, self.age)


class B(A):
    def __init__(self, name, age, company):  # adding new argument applicable to only B
        self.company = company
        print('in constructor B')
        super().__init__(name, age) # all arguments in parent class should be passed to super

    def info_b(self):
        return self.name
b=B('sri',20,'tcs')

b.__dict__   # {'company': 'tcs', 'name': 'sri', 'age': 20}


# example code for multiple inheritance

class Employees:
    raise_amount=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=self.pay*Employees.raise_amount


class Developer(Employees):
    def __init__(self, first, last, pay, prog_lang):
        self.prog_lang = prog_lang
        super().__init__(first, last, pay)


class Manager(Employees):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def emp_list(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1=Developer('sri','r',10000,'python')
dev_2=Developer('chethu','s',20000,'C++')

mng_1=Manager('sri','r',10000,[dev_1])
mng_1.add_emp(dev_2)
mng_1.emp_list()
