#Ternary operator - conditional expressions

# condition_if_true if condition else condition_if_else

is_friend = True

message = 'Hello friend' if is_friend else 'Hello Stranger'

print(message)

# case 2
is_hot = True
date = 'Lets go on a date' if is_hot else 'Lets be friends XD'
print(date)

# case 3
litre_class = True
bike = 'Dream bike' if litre_class else 'Meh.. thats an ordinary bike.'
print(bike)

# case4
diesel = False
fuel = 'This is a petrol car' if diesel else 'This is a diesel car'
print(fuel)



# exercise 

is_magician = False
is_expert = True

if is_magician and is_expert:
  print('You are a master!')

elif is_magician and not is_expert:
  print('Atleast you are getting there')

elif not is_magician:
  print('You need magic powers')