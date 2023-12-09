# Dictionary comprehension

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)
print()

mydict2 = {key: value**3 for key, value in simple_dict.items()}
print(mydict2)
print()

mydict3 = {k: v**3 for k, v in simple_dict.items() if v % 2 == 0}
print(mydict3)
print()

mydict4 = {num: num*2 for num in [1, 2, 3]}
print(mydict4)
print()
