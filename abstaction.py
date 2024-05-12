'''
1)An abstract method is a method that has declaration but not has any implementation.
2)A class which contains one or abstract methods is called an abstract class
3)we cant create objects of abstract class
4)we can implements abstact methods in its child class
5)concrete class (normal class) can only contain normal methods
6)abstract class can contain both normal and abstract classes
7) we have to override abstract method in sub class otherwise sub class will also be treated as abstract
8)If abstarct class has multiple abstarct methods its child class should implement all abstact
methods otherwise child class is still treated as abstarct class and cant be instantiated.
9)python doesnt support abstrarction but we can implement using ABC module
'''

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print('i can walk and run')

class Snake(Animal):
    def move(self):
        print('I can crawl')

class Dog(Animal):
    def move(self):
        print('I can bark')

h=Human()
s=Snake()
d=Dog()
h.move()
s.move()
d.move()

'''
1)In Multiple inheritance grand child class should implement all abstract methods present
in parent class(if child class implemets one abstract method out of 2 methods in parent class,its
still treated as abstract class then grand child class should implement remaining abstarct method)
2)Interface is a class which contains  all abstract methods
3)In python we dont have interface,if an abstact class have all abstact methods 
then it will be treated as interface.
'''
from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def walk(self):  # abstract method only declaration
        pass

    @abstractmethod
    def eat(self):
        pass


class Son(Father):     # cant create objects Son is still abstract class since both methods not implemented
    def walk(self):
        print('son is walking')


class Daughter(Father):
    def walk(self):
        print('daughter is walking')

    def eat(self):
        print('daughter is eating')

s=Son()  # gives error

d=Daughter()
d.walk()
d.eat()