# Question 1:

d = {}
print(type(d))



# Question 2:

d = {'foo':42}
print(d.values())


# Question 3:

# a dictionary is a collection which consists of key-value pairs with unique keys, whereas lsit is a collection of
# objects which can be of same or different datatypes.


# Question 4:

spam = {'bar':100}
print(spam['foo'])
# this statement will result in KeyError because the specified key doesn't exist


# Question 5:

# There is no difference. The in operator checks whether a value exists as a key in the dictionary.


# Question 6:

# 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there
# is a value 'cat' for one of the keys in spam.


# Question 7:

spam.setdefault('color','black')


# Question 8:

# we can use pprint module and pprint function