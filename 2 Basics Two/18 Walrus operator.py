# walrus operator

a = 'Arun prasadh'

if (n := len(a)) > 10:
    print(f'Too long {len(a)} elements.')
    print(f'Too long {n} elements.')


while (n := len(a)) > 1:
    print(n)
    a = a[:-1]
print(a)


# eg2
# usual way
foods = []
while True:
    food = input('Enter your food : ')
    if food.lower() == 'quit':
        break
    foods.append(food)

print(f'List of favourite foods : {foods}')

# using walrus operator
foods = []
while food := input('Enter food : ') != 'quit':
    foods.append(food)

print(foods)


def thisis():
    for i in range(5):
        print(i)
