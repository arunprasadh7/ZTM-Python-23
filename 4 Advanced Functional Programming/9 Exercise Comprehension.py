# Comprehension exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = set{[char for char in some_list if some_list.count(
    char) > 1]}
print(duplicates)
