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

# list methods

basket = [1,2,3,4,5]

# adding methods 
basket.append(6)
print(basket)

basket.insert(2,'two')
print(basket)

basket.extend(['one','two','three'])
print(basket)

# removing methods 

basket.pop()
print(basket)
basket.pop(2)
print(basket)

basket.remove('two')
print(basket)
basket.remove(6)
print(basket)

basket.clear()
print(basket)


# finding items 
basket2 = ['a','b','c','d','e','a']
print(basket2.index('a'))
print(basket2.index('a',2))
# print(basket2.index('a',1,4)) #throws error if char is not in index

print('d' in basket2)
print('z' in basket2)
print('i' in 'i am arun')

print(basket2.count('a'))


# sorting items 
basket3 = ['a','x','f','e','b','d','t']
basket3.sort() #sort modifies the existing list
print(basket3)

basket3 = ['a','x','f','e','b','d','t']
print(sorted(basket3))
print(basket3)

bask3 = basket3.copy()
print(bask3)
bask2  = basket3[:]
print(bask2)

bask3.reverse()
print(bask3)

# common list patterns

sentence = '!'
sentence.join(['hi', 'my', 'name', 'is', 'Arun'])
print(sentence)

sentence2 = '*'
new_sentence = sentence2.join(['hi', 'how', 'are', 'you'])
print(new_sentence)

new_sentence2 = ' '.join(['Hello', 'World', 'Future', 'Billionaire', 'Here!!'])
print(new_sentence2)


# list unpacking 
numbers = [1,2,3]
print(numbers)

a,b,c = [1,2,3]
print(a)
print(b)
print(c)
print()

a,b,c,*others = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(others)
print()

a,b,c,*others,d,e = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(others)
print(d)
print(e)

# None - represents absence of value



