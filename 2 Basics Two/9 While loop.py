# While Loop

i = 0
while i <= 50:
  print(i)
  i += 1
  # break
else: #else will not be printed if there is break statement in while loop
  print('Done with all the work.')

print()

  # for and while use cases
  # for - used when we know how many times the object has to be looped
  # while - more flexibility , used when we do not know how many times the iterable might be looped

my_list = [1,2,3]

# using for loop 
for i in range(len(my_list)):
  print(i)

print('*' * 25)

# using while 
print(len(my_list))
i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1