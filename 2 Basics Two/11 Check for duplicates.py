# Exercise - check for duplicates in the list 

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplictes_list = []

for char in some_list:
  if some_list.count(char) > 1:
    if char not in duplictes_list:
      duplictes_list.append(char)

print(duplictes_list)