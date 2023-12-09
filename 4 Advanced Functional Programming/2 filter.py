# filter()
item_list = [x for x in range(1, 100)]


def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, [1, 2, 3, 4, 5])))

print(list(filter(check_odd, item_list)))
