'''
There are 3 types of errors
1)syntax errors(Compile time errors):
before start of program we get these error due to syntax mistakes.
program will not be executed if we have syntax errors.
Developer is responsible

ex:
if n>10         # : is missing
print('hello)   # ' is missing in print statement

2)logical errors:
Syntax of the code is correct and program executes
But gives wrong output due to wrong logic

Ex:
if 2+2 the output is 10

3)runtime errors:
syntax and logic is correct but error occures after execution
runtime errors are called exceptions

Ex:
a=10
b=0
print(a/b)
throws ZeroDivisionError (cant be divided by zero)

Exception:
exceptions is abnormal termination of program,which diturbs normal flow of program.

try block:
try block contains those set of statements whose execution may result in exception,
in such situations exception will be handled by except block.

except block:

1)this block is used to hold or catch the exception raised in try block
2)except block statements will be executed only when exception is generated in try block.
3)if exception is generated in except block then program terminates
4)try block can have multiple except block
5)a default except block will be placed at the end of all except blocks


finally block:

1)statements in finally block will always be executed irrespective of exception or not in try block.
2)within finally block we will write clean-up statements,database connection closing,file closing statements
3)there should be only one finally block
4)if we use sys.exit() then finally block wont be executed.

else block:
1)else statement also used in try-except block,else block will be executed only when there is no exception
2)we cant use else block in exception if we already have finally block.
'''

'''
a=int(input('enter first number'))
b=int(input('enter second number'))
try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print('cant divide a number by zero',e)

print('end')

# try with multiple except

print('start')
try:
    x = int(input('enter first number'))
    y= int(input('enter second number'))
    print(x/y)

except ZeroDivisionError as e:
    print('Cant divide  by zero',e)
except ValueError as e:
    print('Please enter valid integer',e)
print('end')

# try-except and else blocks

print('start')
try:
    x = int(input('enter first number'))
    y= int(input('enter second number'))
    print(x/y)

except ZeroDivisionError as e:
    print(e)
except:                                   # default except block should be always at the end of all except blocks
    print('i am in default except block')

else:                            # will be executed only when no execption occures in try block
    print('no excepetion')
'''
'''
# nested try-except blocks

print('program starts')
try:
    x = int(input('enter first number'))
    y = int(input('enter second number'))

    try:
        print(x/y)
    except ZeroDivisionError as msg:
        print(msg)

except ValueError as msg:
    print(msg)

finally:
    print('Goodbye')


If an exception occurs during execution of the try clause, 
the exception may be handled by an except clause. If the exception is not handled by an except clause, 
the exception is re-raised after the finally clause has been executed.

An exception could occur during execution of an except or else clause. 
Again, the exception is re-raised after the finally clause has been executed.

If the try statement reaches a break, continue or return statement,
 the finally clause will execute just prior to the break, continue or return statement’s execution.

If a finally clause includes a return statement, 
the returned value will be the one from the finally clause’s return statement,
 not the value from the try clause’s return statement.
'''

def divide(a,b):
    try:
        res=a/b
    except (ZeroDivisionError,ValueError) as msg:
        print(msg)
        # if no exception in try else will execute
    else:
        print('division results is =',res)
    finally:
        print('Executing finally block')

divide(10,0)
print('done')

# user defined exception

class InvalidVoter(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input('enter the age of voter'))

try:
    if age>18:
        print('valid voter')
    else:
        raise InvalidVoter ('age is less than 18')

except InvalidVoter as msg:
    print('Not a valid voter')

print('Done')

'''
pylint is used for unittest
'''