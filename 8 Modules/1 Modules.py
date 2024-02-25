# Modules in python - used to organize code
# whenever module is imported python editor generates a cache file of that module and the next time the module is called it loads from the cache file .
# - if the main file is modified the cache file is regenerated

# lets create a temp py file that performs addition and subtraction

import sample

a = sample.addition(10, 5)
print(a)

b = sample.subtraction(10, 5)
print(b)
