def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

print(methodception(add_two_numbers))
my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x % 2 == 0, my_list)))

res = (lambda x: x * 3)(5)
print("Res", res)
