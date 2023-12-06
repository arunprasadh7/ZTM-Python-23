# *args **kwargs

def super_fun(*args):
  return sum(args)

print(super_fun(1,2,3,4,5))



# kwargs 
def super_dict(**kwargs):
  # return (kwargs)
  for k,v in kwargs.items():
    return k, v

print(super_dict(name = 'arun', age = 26, gender = 'male'))


# combining args and kwargs

def combination(*args, **kwargs):
  total = 0
  for val in kwargs.values():
    total += val
  return sum(args) + total

print(combination(1,2,3,4,5,n1=5, n2=10))