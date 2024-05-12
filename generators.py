'''
PYTHON ITERATORS
1)for inbuilt objects like list,tuple,set and string we use for loop to iterate over an object
2)to create iterator for our own object we need to override 2 methods( iter() and __next__)
'''
class TopTen:

    def __init__(self,num,limit):
        self.num=num   # num is to have limit
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num>=self.limit:
            raise StopIteration
        else:
            self.num+=1
            return self.num

value=TopTen(0,15)

for i in value:   # now we have overriden iter and next methods and can use for loop on iterable object value
    print(i)

# WAP to iterate over string words
class Sentence:
    def __init__(self,s):
        self.s=s
        self.index=0  # start index
        self.words=self.s.split()  # to split string to list of words
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.s):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.words[index]

ss=Sentence('my name is sri')
for i in ss:
    print(i)
'''
1)A generator-function is defined like a normal function, but used  to generate a sequence of values
2)If the body of a def contains yield, the function automatically becomes a generator function.
3)generators saves memory while handling large files
4)generator returns iterable
5)yield is similar to return
'''
'''
def gen():
    yield 1    # yields single value at a time
    yield 2
    yield 3
    yield 4

g=gen()
print(g.__next__())   # gives 1
print(g.__next__())   # gives 2
print(g.__next__())


# program to find first 10 squares using generator

def squares():
    n=1
    while n<=10:
        sq=n*n
        n+=1
        yield sq

sq1=squares()
print(sq1.__next__())   # prints first value 1
for i in sq1:
    print(i)

# fibonacci program using generators

def fib(n):
    x,y=0,1
    while x<=n:
        yield x
        x,y=y,x+y

for i in fib(10):
    print(i,end=',')

'''
# generator to iterate over string words
def g(s):
    for i in s.split():   # generator is just like normal function with yield
        yield i

x=g('my name is')
for i in x:
    print(i)


'''
Difference b/w list comprehension and generator
1)when we are creating list we are actually building collection of values,
whereas when we create generator we are building collection of values but a recipe for that

2)generator expression doesnt really produces values until its needed this not only leads to 
memory efficiency also computational efficiency

3)size of list is limited to available size of memory,whereas size of generator is unlimited

4)A LIST CAN BE ITERATED MULTIPLE TIMES; A GENERATOR EXPRESSION IS SINGLE ITERATION ONLY

5)
'''