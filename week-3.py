##################################################
# 1. Comparison Operators                       #
# 2. Boolean Operators                          #
# 3. Basic Logic                                #
# 4. Built-In Python Functions for Numbers      #
# 5. if, else, elif statement                   #
##################################################

# Comparison Operators เปรียบเทียบ 2 + 2 (Binary Operator) => 2.add(2)
# >, <, ==, >=, <=, !=
from math import ceil, floor


print(2 < 3) # True -> Boolean
print(4 > 8) # False

print(3 >= 3)
print(3 >= 1)
print(3 >= 6)

print('---------------------')

print(13 < 5) # False
print(12 >= 4) # True
print(6 != 3) # True
print(2 + 3 < 5) # False

# Conditioning
# if condition:
#   thing_to_do

print('-----------------')

if 20 < 4:
    print('Condition is working')
    print('Second line inside condition')
print('Outside of condition')

print('------------------')
pocket_money = 1200

if pocket_money < 30:
    print('I will buy coffee from vending matchine for lunch.')
elif pocket_money < 100: # else if
    print('I will buy chicken for lunch.')
elif pocket_money < 1000:
    print('I will buy Beef Wellington for lunch.')
else:
    print('I am not hungry.')

print('----------------------')
number = 10

if number < 5: # 10 < 5 False
    print('A')
elif number % 2 == 0: # 0 == 0 True
    print('B')
elif number == 10: # 10 == 10 True
    print('C')

print('------------------------')
# Logical Operators
# and or not

# T and T => T
# T and F => F
# F and T => F
# F and F => F

# T or T => T
# T or F => T
# F or T => T
# F or F => F

# not T => F
# not F => T

print(3 < 5 and 6 > 4) # T and T
print(3 != 5 and not 5 > 2) # T and F
print('--------------------')
print(not(4 < 6 or 3 > 4) and 5 <= 5) # Aim => F
print(3 > 3 and 4 < 1 or 4 > 2) # Utt F => T
print(4 < 2 and not 5 > 6) # Bear F => F
print(2 < 6 or 3 != 8 and not 5 < 3) # Ik-Q T => T
print(4 < 5 and 3 > 6 and 4 > 2) # Mai F => F

print('--------------------')
# Built-In Python Functions for Numbers
# int() => int('35')
# float() => float('35')
# str() => str(22.54) => '22.54'

print(abs(-5)) # absolute
print(ceil(4.32))
print(floor(5.78))
print(round(4.357, 1))

print(bin(12)) # base 2
print(oct(58)) # base 8
print(hex(257)) # base 16

print('--------------------')
number = 15

if number > 5:
    print('A')
elif number > 10:
    print('B')

if number > 10:
    print('C')

