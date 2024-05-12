'''
list comprehension

1)list comprehension is an elagant way of creating list based on existing lists
2)list comprehension is more compact and faster than normal function and loops
for creating lists
3)faster than map function
4)user friendly

'''
l1=[i for i in range(10)]

lst=[10,15,20,25,30,35]
l1=[i*2 for i in lst if i%2==0]    # using conditional statements for filtering elements from list


# generator comprehension

l1=[1,2,3,4,5]
s='abcde'
lst=((i,j) for i in l1 for j in s)    # () is used for generator

# set comprehension
l1=[1,2,3,4,5]
ss={i for i in l1}

# dictinary comprehension
l1=[1,2,3,4,5]
s='abcde'
d={l1:s for l1,s in zip(l1,s)}  # zip matches same index values from different iterators

d={l1:s for l1,s in zip(l1,s) if l1!=3}  # ignores key 3
