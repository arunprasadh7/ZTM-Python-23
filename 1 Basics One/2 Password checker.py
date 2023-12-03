# Password checker 

username = input('Enter your username : ')
password = input('Enter your password : ')
passLen = len(password)
star = '*'

print(f'Hello {username}!! Your {password[:2]+ ((passLen-3) * star)} has {passLen} characters.')

