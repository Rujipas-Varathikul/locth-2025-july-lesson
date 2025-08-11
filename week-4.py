##################################################
# 1. Nested Conditioning                         #
# 2. What is loop?                               #
# 3. for loop                                    #
# 4. while loop                                  #
# 5. Action in loops                             #
# 6. Loop and condition                          #
##################################################

# Nested Conditioning
number = 15

# if number > 6 and number < 10: # number < 10: A1, number >= 10: A2
#     print('A')
# else:
#     print('B')

if number > 6:
    if number < 10:
        print('A1')
    else:
        print('A2')
else:
    print('B')

# What is loop?
for _ in range(5):
    print('Hello')

# for loop
# for variable_name in range(5):
#     things_to_do
# range(7) => 0, 1, 2, 3, 4, 5, 6
# range(4) => 0, 1, 2, 3
# range(10) => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# range(2, 7) => 2, 3, 4, 5, 6
# range(3, 9) => 3, 4, 5, 6, 7, 8
# range(2, 5) => 2, 3, 4

# range(3, 10, 2) => 3, 5, 7, 9
# range(1, 6, 4) => 1, 5
# range(2, 8, 3) => 2, 5

for number in range(6):
    print(number)

# range(6) => 0
# number = 0
# print(number)
# range(6) => 1
# number = 1
# print(number)
# ...
# range(6) => 5
# number = 5
# print(number)

for number in range(3, 8):
    print('I count', number + 3)

# range(3, 8) => 3
# number = 3
# print('I count', number + 3) # number + 3 => 3 + 3 => 6

# range(12, 4, -3)

for _ in range(5):
    print('Hello')
