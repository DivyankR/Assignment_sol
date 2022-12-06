# Question 1:

# [] is used to represent a list.
l=[]
print(type(l))


# Question 2:

spam = [2,4,6,8,10]
hello = spam[2]
print(hello)


# Question 3:

var = spam[int(int('3' * 2) / 11)]
print(var)

# this will print spam[3] value which is 8.


# Question 4:

print(spam[-1])


# Question 5:

print(spam[:2])


bacon = [3.14, 'cat', 11, 'cat', True]

# Question 6:

print(bacon.index('cat'))

# this will return the first index at which the list contains cat.


# Question 7:

bacon.append(99)
print(bacon)


# Question 8:

bacon.remove('cat')
print(bacon)

# remove will remove the first occurrence of cat from bacon


# Question 9:

# list concatenation is used to put the elements of two lists into one. This can be done via many ways such as +
# operator, entend() function etc.

# list replication is in a way creating a copy of a particular list. This can be done by extend(), = operator(
# assignment operation), using list comprehension, using copy() method etc.

# list concatenation:

l=[1,2,3,4]
l1=[5,6,7,8]
l.extend(l1)
print(l)

# list replication

l=['abc',23,1.2]
d = l.copy()
print(d)


# Question 10:


# append() is used to add an element in the list. it takes the element which is to be added in the list as an argument
# and adds it to the end of the list

l=[2,4,6,14]
l.append(9)
print(l)

# insert() is used to insert an element in the list at a given position. Both the element and the position at which it
# is to be added are given as arguments to insert()

l1=[4,2.3,6,2]
l1.insert(1,"leo")
print(l1)


# Question 11:

# the two methods to remove items from a list are pop() and remove(). pop() takes index as argument and remove() takes
# the element which is to be removed as argument

l=[3,4,7,2,True,234.1]
l.pop(3)
l.remove(True)
print(l)


# Question 12:

# Lists are similar to strings, but list can have elements of different datatypes inside them but string can have only
# one datatype elements inside them. Both are similar because they are collection of items

l=[True,"sdv",-12,12.33]
s="hello"


# Question 13:

# lists are mutable but tuples are not.

# iteration is faster in tuples as compared to lists.

# lists are better at performing operations such as insertion,deletion and tuples are better at accessing elements.


# Question 14:


t = (42,)
print(type(t))


# Question 15:

# tuple's values in a list form

t=(12,42,5)

l = list(t)
print(l)

# list's values in a tuple form

t1 = tuple(l)
print(t1)


# Question 16:

# Variables that contain list elements aren't list themselves. Instead they contain the datatype same as the element
# which the variable has stored.


# Question 17:


# copy.copy():

# It makes copies of the nested objects' reference and doesn't create a copy of the nested objects. So if we make any
# changes to the copy of the object will reflect in the original object

# copy.deepcopy():

# above method is called deepcopying, If we make change to one of child won't affect the original object.
