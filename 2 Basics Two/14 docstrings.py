# Docstrings inside function

def test(a):
  '''Info : This is test for docstrings in python.'''
  print(a)

test('hello')

# ways to read docstrings
help(test) #displays the text inside the docsting

print(test.__doc__)