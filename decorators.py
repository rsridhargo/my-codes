'''
1)Decorators can be thought of as functions which modify the functionality of another function.
They help to make your code shorter and more "Pythonic".
2)Decorators as the name suggests is used for decorating the other functions without changing their
functionality
3)In Decorators, functions are taken as the argument into another function
and then called inside the wrapper function.
4)we use decorators when we cant change the third party functions to change functionality
'''
def info():
    print('in hello')
a=info     # assigning copy of info to variable a
a()
del info    # deletes info
#info()      # but throws error as we deleted info
a()         # still callable as it is copy of info

# we can have function under function and can return function also

def hello(name):
    print('in hello() function')

    def greet():
        print('\tin greet() function ')   # nested functions

    def weclome():
        print('\tin welcome() function ')   # \t for tab

    if name=='sri':
        return greet
    else:
        return weclome
    print('done with hello()')

my_func=hello('sri')    # hello returns greet function which is assigned to my_func and can be callable
my_func()

# we can also pass function as an argument

def myfunc():
    print('Hi welcome sri')

def other(some_func):           # some_func  is argument
    print('in other function')
    print(some_func())

(other(myfunc))   # passign myfunc to another function


# creating decorator

def new_decorator(original_function):          # passing function as an argument

    def wrap_fun():   # in wrap function we have to pass arguments that we pass in original function
        print('code before the execution of original func')

        original_function()    # executing the passed original func

        print('code after the execution of original func')

    return wrap_fun     # returning wrap fun after doing modification

# creating original function

def fun_needs_decorated():
    print('i want to be decorated')

# calling functions

decorated_function=new_decorator(fun_needs_decorated)
# function is decorated

decorated_function()    # new_decorator function returns wrap function which can be called


# if we place @ decorator function it will be automatically calls original function with modification

@new_decorator
def fun_needs_decorated():
    print('i want to be decorated')

fun_needs_decorated()

# decorator for dividing 2 numbers
def div_dec(fun):

    def wrap(x,y):
        print('if x is less than y then swapping numbers')
        if x<y:
            x,y=y,x
        fun(x,y)

    return wrap

@div_dec
def div(a,b):
    return (a/b)

print(div(10,50))


