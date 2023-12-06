# functions - reusable blocks of code

def greet():
  print('Hello')

greet()

# parameters 

def greet(name, emoji):
  print(f'Hello {name} {emoji}.')

# arguments - values provided to the parameters
# positional args
greet('Arun', 'XD')
greet('Arc', 'Weweweweeww')

# default parameters
def greet(name='arun', age=25):
  print(f'Hello {name}. You are turning {age + 1} next year.')

greet()
greet('Arc', 15)

# keyword args 
def greet(name, age):
  print(f'Hello {name}. You are {age} years old.')

greet(age = 50, name='Storm')