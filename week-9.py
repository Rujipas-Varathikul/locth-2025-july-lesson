##################################################
# 1. List                                        #
# 2. List Property                               #
# 3. List Action.                                #
##################################################
# data structure
# 'hello'.split('l') -> ['he', '', 'o']
# | | | | | | |
# my_list = [3, 'hello', True, False, 2.54, -0.21, [1, 2, 3]]
# student = ['John', 'Anna', 'Logan', 'Wednesday']
# empty_list = list()
# empty_list = []

example = ['egg', 'meat', 'carrot']
# add element to list
print(example)
example.append('cucumber')
print(example)
example.extend(['noodle', 'orange'])
print(example)

# delete elements
example.pop(2)
print(example)
example.remove('noodle')
print(example)

if 'ham' in example:
# if 'ham' not in example:
    example.remove('ham')

# del example
# print(example)

# example = []

print(len(example))
print(example[3])
print(example[1:3])

# print([0] * 20)
# print(['hello'] * 20)

print(example)
example[3] = 'lime'
print(example)

for index in range(3):
    print(example[index])

# loop 1 -> index = 0
# print(example[index])
# loop 2 -> index = 1
# print(example[index])
# loop 3 -> index = 2
# print(example[index])

print('-------------------')

for product in example:
    print(product)

# ['egg', 'meat', 'cucumber', 'lime']
# loop 1 -> product = 'egg'
# print(product)
# loop 2 -> product = 'meat'
# print(product)

print('---------------')

for index, product in enumerate(example):
    print(index, product)

# enumerate -> 0 => index, 'egg' => product
# print(index, product)
# enumerate -> 1 => index, 'meat' => product
# print(index, product)

