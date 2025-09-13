##################################################
# 1. String Action (continue)                    #
# 2. Condition and Loop in String                #
# 3. Format String                               #
##################################################

# Condition in String
if 'ab' in 'abcd': # True
    print('Hello 1')

if 'ac' in 'abcd': # False
    print('Hello 2')

if 'AB' not in 'abcd': # True
    print('Hello 3')

# Mr. Ms. Mrs.
# Mr. John Oolanlaa
# fullname = input('Enter your full name with title: ')

# if 'Mr.' in fullname:
#     print('Man')
# elif 'Ms.' in fullname or 'Mrs.' in fullname:
#     print('Women')
# else:
#     print('Incorrect title')

# Loop in String
string = 'keyboard '

# 'apple' => 0, 1, ... ,4 => range(5)
# 'school' => 0, 1, ... , 5 => range(6)
# 'applebobo' => 0, 1, ... , 8 => range(9)
for index in range(len(string)): # 0, 1, 2, ..., 8
    print(index, string[index])
# 'apple'[3]
for character in string:
    print(character)

# character = 'k
# ...
# character = 'e'
# ...
# character = 'y'
# ...
# keyboard 
# for index, character in enumerate(string):
#     print(index, character)

# for index in range(4, len(string)):
#     print(index, string[index])

# format string
# name = input('Name: ')
# age = input('Age: ')

# Hi, my name is Due. I am 23 years old.
# print('Hi, my name is', name + '. I am', age, 'years old.')
# print(f'Hi, my name is {name}. I am {age} years old. 2 + 2 = {2 + 2}')
# print(f'Hi, my name is {name}. I am {age} years old. 3 > 5 is {3 > 5}.')

# split
# substring
sentence = 'How are you?'
print(sentence.split()) # method => list
print(sentence.split('o'))
print(sentence.split('re'))
print('hello'.split('l')) # ''

# ASCII -> UTF8 -> 1001
print(ord('a'))
print(ord('A'))
print(ord(' '))
print(ord('ก'))