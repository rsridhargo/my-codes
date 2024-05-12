'''
1)-class which is used to count hashable objects.
It implicitly creates a hash table of an iterable when invoked.
2)its imported from collection module
3)if the key is not present in counter it will not throw error but shows count as 0
4) Inside of counter elements are stored as dictionary keys and the counts of the objects are stored as the value.
'''

from collections import Counter

l=[1,2,3,4,5,6,7,8,9,3,23,1,6,5,4,9,7,8,7,2,5,6,8,8,7,1,1,5]
print(Counter(l))

print(c.most_common(5))   # to get most common 5 items

# to get counter of words in sentence

s = 'How many times does each word show up in this sentence word times each each word'
l=s.split()
c=Counter(l)
print(c)

# list(c)  is used to get list of key values
#set(c)  to get unique set of keys
#c.elements()  to get all key items

for i in c.elements():
    print(i)

# if we use counter to dictionary it will return the same dictionary
# if we use counter for sets it will return count value as 1 by default
# since set doesnt support duplicate items.
# Counter is mostly used for list,tuples and strings

'''
defaultdict
1)defaultdict is sub class of dictionary
2)only difference is it never raises keyError if the key is not present
3)instead it will add the key to dict with values as zero(unless explicitly) mentioned
4)if we pass int as default factory 0 will be the default value
5)default_factory: A function returning the default value for the dictionary defined. 
If this argument is absent then the dictionary raises a KeyError
'''
from collections import defaultdict
d=defaultdict(object)
d['k1'] # k1 will be added to dictionary

d['k2']=2

for i in d:
    print(i)

# to add each character of string to dictionary
s='sridhar'
d=defaultdict(int)  # passing int will set default values as 0
for i in s:
    d[i]+=1

for i in d:    # prints all keys
    print(i)

# using lambda to set default values

d=defaultdict(lambda:0)  # we can use any default values,if we use 1 and key is added for first time its value is 1
l=[1,2,3,4,5,6,1,5,4,2]
for i in l:
    d[i]+=1
c=Counter(d)
print(c)

'''
OrderedDict 
1)OrderedDict is sub class of dictionary which is unordered
2)only difference b/w dictionary and ordered dictionary is ordered dictionary maintains insertion order
3)orderedDict with same key and value is equal to each other
'''

d1={}
d1['a']=1
d1['b']=2
d1['c']=3
d1['d']=4
d1['e']=5
for k,v in d1.items():
    print (k,v)

from collections import defaultdict,Counter,OrderedDict
od1=OrderedDict()
od1['a']=1
od1['b']=2
od1['c']=3
od1['d']=4
od1['e']=5
for k,v in od1.items():
    print (k,v)
'''
1)if we change the value of a key then key order will remain same
2)after deleting the key and re-inserting it again it will be added at the last on order
'''

from collections import defaultdict, Counter, OrderedDict

od1 = OrderedDict()
od1['a'] = 1
od1['b'] = 2
od1['c'] = 3
od1['d'] = 4
od1['e'] = 5
for k, v in od1.items():
    print(k, v)

del od1['d']

print('\n after deletion')
for k, v in od1.items():
    print(k, v)

print('\n after re-insertion')
od1['d'] = 4
for k, v in od1.items():
    print(k, v)
'''
output is
a 1
b 2
c 3
d 4
e 5

 after deletion
a 1
b 2
c 3
e 5

 after re-insertion
a 1
b 2
c 3
e 5
d 4
'''

'''
namedtuples()

1)It is ike dictionary which contains key and values
2)it can be accessed using both key and index unlike dict where order is not fixed
3)_make() is used to create namedtuple from list of values
4)consumes less memory
'''
from collections import namedtuple

Student=namedtuple('Student','name age') # similar to create object from class,space separated b/w 2 attributes
s1=Student('sri',25)   # s1 is namedtuple of Student class with name and age attributes
print(s1)
print(s1[1]) # can be called using index
print(s1.name)   # can be called using attribute name also

print(getattr(s1,'name'))   # getattr(object_name,attribute) also used to access

#._make(iterable) is used to create namedtuple from iterables
Dog=namedtuple('Dog','breed age colour')
l=['jully',20,'black']
n=Dog._make(l)
print(n)

# to get orderedDict from namedtuples we use_asdict() method
print(n._asdict())

'''
A double-ended queue, or deque
1)deque is similar to list but deque allows both ends operation
2)Deque is preferred over list in the cases where 
we need quicker append and pop operations from both the ends of container
3)all methods applicable to list holds good for deque 
for left side operations we add left keyword with method

'''
from collections import deque
de=deque([1,2,3])
de.append(4)
print(de)
de.appendleft(0)