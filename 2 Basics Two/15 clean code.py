# clean code - using smaller lines of code to get the job done

# normal code 
# def is_even(num):
#   if num % 2 == 0:
#     return True
#   elif num % 2 != 0:
#     return False
  

# clean code 
def is_even(num):
  return num % 2 == 0



print(is_even(50))
print(is_even(5))