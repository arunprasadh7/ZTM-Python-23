# Return in functions

def sum(a,b):
  return a + b

print(sum(5,5))

answer = sum(10,10)
print(sum(5, answer))

# ex2
def sum(num1, num2):
  def another_function(n1,n2):
    return n1 + n2
  return another_function(num1,num2)

print(sum(5,5))