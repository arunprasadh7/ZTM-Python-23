# Sets - unordered collection of unique objects 
# unordered - cant use index to find things
# unique - no duplicates are allowed 

my_set = {1,2,3,4,5}
print(my_set)

my_set2 = {1,2,3,4,4,4,4,5}
print(my_set2)
my_set2.add(100)
print(my_set2)


new_set = my_set2.copy()
new_set.clear()
print(new_set)
print()

# common set methods
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

# difference 
print(set1.difference(set2))
print(set2.difference(set1))

# discard
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

set1.discard(5)
print(set1)

# difference update 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

set1.difference_update(set2)
print(set1)
set2.difference_update(set1)
print(set2)

# intersection 
set1 = {1,2,3,4,5} 
set2 = {4,5,6,7,8,9,10}

print(set1.intersection(set2))
print(set2 & set1)

# isdisjoint - returns true if two sets have nothing in common 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

print(set1.isdisjoint(set2))

# union - combines two sets elements into a single set
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
print(set1.union(set2))
print(set1 | set2)

# subset and superset 
set1 = {4,5}
set2 = {4,5,6,7,8,9,10}

print(set1.issubset(set2))
print(set2.issuperset(set1))