# Iterable - something that can be looped over. 
#             an object or a collection that can be looped over.
#             eg strings, lists, tuple, set, dict etc

# iterate - one by one check each item in the collection 

user = {
  'name' : 'Arun',
  'age': 500,
  'can_swim':False
}

for item in user:
  print(item)

for key, value in user.items():
  print(key, value)

for values in user.values():
  print(values)

for keys in user.keys():
  print(keys)