'''
Encapsulation is an idea of wrapping data and methods within a unit.
1)This puts restrictions on accessing variables and methods directly
and can prevent the accidental modification of data.
2)we can modify that data only by object methods defined inside the class
3)It hides data from user
4)Ex: if there are many depa in company and if finance officer wants a data of sales team
then directly person from finance cant access sales dept data,
first he has to ask sales team and then get dat
5)_ is used to say attribute is protected and cant be accessed but it is for just for
 convention and can be accessed in real
6) __ double underscore used to say atribute is private cant be accessed,it can be modified inside the
class methods only(it can be accessed outside class using object_name._class name__attribute)
'''
class C(object):
    def __init__(self):
        print('c constructor')
        self.a = 123    # OK to access directly
        self._a = 123   # should be considered protected can be accessed
        self.__a = 123  # considered private, cant be accessed

    def __info(self):                       # private method
        print('hello in private method')

    def get__a(self):     # private member can be accessed outside class using method inside class
        print(self.__a)

    def set__a(self,new__a):   # to modify private member value using set method defined inside class
        self.__a = new__a

c = C()
print(c._a)
#print(c.__a)  # gives error
print(c.get__a())
c.set__a(200)
print(c._C__a)   # can be used to access private member

#c.__info()    # throws error


class A:
    def __init__(self, a, b):
        self.__a = a   # private variables
        self.__b = b

    def setting(self, a, b):
        self.__a = a
        self.__b = b

    def getting(self):
        return self.__a, self.__b

    def __addition(self):          # private method
        return self.__a + self.__b

a1=A(20,10)
a1.__a       # throws error since cant be accessed

a1.setting(100,200)  # updating private variables using setter method
a1.getting()         # getting values

a1._A__a   # accessing private variables using name mangling technique

# name mangling--<object name>_<class name>__<variable name>

a1._A__addition()   # accessing private methods