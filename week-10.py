##################################################
# 1. List Action.                                #
# 2. Tuple                                       #
# 3. Set                                         #
##################################################
# map(function, list)
number1 = ['2', '3', '5', '10']

number2 = list(map(int, number1)) # [2, 3, 5, 10]
# int('2') -> 2
# int('3') -> 3
# int('5') -> 5
# int('10') -> 10

print(number1)
print(number2)
print(type(number1[0]))
print(type(number2[0]))
# print(map(int, number1))

another_list = [2.0, 5.18, 3.55]
another_list2 = list(map(str, another_list)) # ['2.0', '5.18', '3.55']

print(another_list2)

another_list3 = [[], [1, 2], [7, 5, 3, 1]]
element_length = list(map(len, another_list3)) # [0, 2, 4]
print(element_length)

number = [5, 12, 27, 32, 18]
# number.sort()
# print(number)

sorted_number = sorted(number)
print(number)
print(sorted_number)

names = ['alfred', 'labubu', 'Ant Man', 'aom', 'Bobby']
# reverse -> keyword argument
names.sort(reverse=True)
print(names)

number = [2, 5, 1, 2, 5, 5, 1, 5]
print(number.count(5))
print(number.count(1))
print(number.count('Hello'))

# copy
list_a = [1, 2, 3, 4]
list_b = list_a

# list_b -> [1, 2, 20, 4] <- list_a

list_b[2] = 20
print(list_a) # [1, 2 ,3, 4]
print(list_b) # [1, 2, 20, 4]

list_a = [1, 2, 3, 4]
list_b = list_a.copy()

# [1, 2, 3, 4] <- list_a
# [1, 2, 20, 4] <- list_b

list_b[2] = 20
print(list_a) # [1, 2 ,3, 4]
print(list_b) # [1, 2, 20, 4]

# List Extraction
my_list = [1, 2, 3, 4, 5]

print(my_list) # print([1, 2, 3, 4, 5])
print(*my_list) # print(1, 2, 3, 4, 5)

# tuple
my_tuple = (1, 2, 3, 7, 9)
empty_tuple = tuple()
empty_tuple = ()
one_element_tuple = (6, )
print(one_element_tuple)

# Tuple VS List
# Mutability

# Cannot do
# add element
# delete element
# sort

# Can do
# index
print(my_tuple[3])
# len
print(len(my_tuple))
print('----------------')
# loop
for element in my_tuple:
    print(element)
print('----------------')
# count
print(my_tuple.count(3))
# slice
print(my_tuple[1:3])
# for index in range(3):
#     my_tuple[index] = 20 -> Error
# in
if 3 in my_tuple:
    print('Ha ha ha')
    
a, b, c = 1, 2, 3
d = 1, 2, 3
print(a, b, c)
print(d)

for element in enumerate(my_list):
    print(element)

