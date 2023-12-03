# lists in python 

li = [1,2,3,4,5]
li2 = [ 'arun', 'prasadh',True, 2.5]

amazon_cart = ['notebook', 'pen']
print(amazon_cart[0])

# list slicing 

number_list = ['one', 'two','three', 'four', 'five', 'six', 'seven']
print(number_list[0:3])
print(number_list[2:])
print(number_list[::2])

# list are mutable
amazon_cart[0] = 'laptop'
print(amazon_cart)
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)

# 2d lists - Matrix 

matrix =  [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print(matrix[0])
print(matrix[0][1])
print(matrix[1][2])
print(matrix[2][2])