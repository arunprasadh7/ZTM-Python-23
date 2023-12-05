# range ()

print(range(5))
print(range(2,5))

for i in range(5):
  print(i)

for i in range(2,5):
  print(i)

# range with step 
for i in range(0,10,2):
  print(i)

print('*' * 25)

#range with negative step- reverse
for i in range(10,0,-1):
  print('Negative step',i)

print('-' * 25)
#special case
for _ in range(10):
  print(_)

print('-----------------------------------------------')

# range with list 
for _ in range(2):
  print(list(range(10)))