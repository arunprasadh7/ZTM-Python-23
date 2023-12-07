# Exercise Extending List

class SuperList(list):

    def __len__(self):
        return 1000


s1 = SuperList()
print(len(s1))

s1.append(5)
s1.append(10)
s1.append(15)
print(s1[0])
print(s1[1])
print(s1[2])


# to check if SuperList is subclass of list there is special function
# issubclass(subclass, mainclass)
print(issubclass(SuperList, list))
