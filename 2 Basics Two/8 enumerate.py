# enumerate() - returns the index for iterable object

for i, char in enumerate(range(1,10)):
  print(i, char)

print()

for i, char in enumerate([1,2,3,4,5]):
  print(i, char)

print()

# exercise - print the index for the number 50 
for index,number  in enumerate(list(range(100))):
  if number == 50:
    print(index)