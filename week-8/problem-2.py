expression = input() # '5-7'
# เลขโดด 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# _ + _
# 0 1 2
# index 0, 2 -> number
# index 1 -> operation +/-
# 'banana'[2] -> 'n'
first_number = int(expression[0]) # '5' -> 5
second_number = int(expression[2]) # '7' -> 7

if '+' in expression:
    # expression.split('+') # ['3', '4']
    print(first_number + second_number) # print(3 + 4)
elif '-' in expression:
    print(first_number - second_number)
