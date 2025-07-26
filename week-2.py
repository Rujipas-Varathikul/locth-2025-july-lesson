##################################################
# What are we talking about today?               #
# 1. Variables                                   #
# 2. How to receive input?                       #
# 3. Arithmetic Operators                        #
# 4. Variable Adjustment                         #
# 5. Comparison Operators                        #
# 6. Boolean Operators                           #
# 7. Basic Logic                                 #
# 8. Built-In Python Functions for Numbers       #
##################################################

# syntax of variable => variable_name = value
name = 'Due'
age = 23
height = 170
chair_price = 590 # snake_case, camelCase, PascalCase

print(name, age)

name = 'Bear'
age = 13
print(name, age)

# age = input('Enter your age: ')
# print(age)
# print('Thank you')

# Arithmetic Operators
print(7 + 12) # 7 + 12 => 19 => print
print(6 - 5)
print(5 * 4)
print(5 / 2) # 2.5
print(5 // 2) # 2
print(5 % 2) # 1
print(2 ** 3) # 2 * 2 * 2 => 8

# order of operation/precedence
# () => ** => * / // % => + -
print(3**2 + 5*6//2) # 24
print(4*(3 + 2) - 3%6) # 17 [3 / 6 = 0 R 3]

price = 500

print(price + 300)
print(price*3 - 250)

# Adjustment Operation
number_of_student = -5

number_of_student = number_of_student + 5
print(number_of_student)

# += -= *= /= //= %= **=
number_of_student += 5
print(number_of_student)
