# Highest even number 
# write a python program to find the hightest even number from the given list

def highest_even(li):
  greater = 0
  for num in li:
    if num % 2 == 0 and num > 0:
      greater = num
  return greater


print(highest_even([10,2,6,5,9,14,17]))


# method 2 

def high_even(li):
  evens = []
  for i in li:
    if i % 2 == 0:
      evens.append(i)
  return max(evens)

print(high_even([1,2,4,12,7,24,5,9,10,11]))