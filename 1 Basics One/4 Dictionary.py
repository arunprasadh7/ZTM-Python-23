#Dictionaries in python - hashtables, objects
# dict keyword

dictionary = {
  'a' : 1,
  'b' : 2,
  'c' : 3
}

print(dictionary['a'])
print(dictionary['c'])

print()

# dict can have any value inside them
multivalue_dict = {
  'a':[1,2,3],
  'b':2,
  'c':5.5,
  'd':True
}

# dictionary inside a list 
my_list = [
  {
    'a':1,
    'b': 2,
    'c':3
  },
  {
    'd':4,
    'e':5,
    'f':6
  }
]

print(my_list[0]['a'])
print(my_list[0]['b'])
print(my_list[0]['c'])

print(my_list[1]['d'])
print(my_list[1]['e'])
print(my_list[1]['f'])
print()

# DICT METHODS 

user = {
  'basket' : [1,2,3],
  'greet' : 'hello',
  'password' : 'arun'
}

print(user.get('age',))
print(user.get('password', 'password not set'))

# alternate way to create a dict
user2 = dict(fname = 'arun', lname = 'prasadh', age = 27)
print(user2)
print()


# to check if item is in dict 
print('basket' in user)

# some frequently used methods
# keys - returns all keys
# values - returns all values
# items - returns both keys and values in form of a tuple
# clear - clears the entire dict
# copy - makes a copy of a dict
# pop  - removes the specified key from the dict 
# popitem() -  removes the last key/value from the dict
# update - updates the existing value if present, else enters a new value into the dict
