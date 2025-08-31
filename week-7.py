##################################################
# 1. Nested Loop.                                #
# 2. String Declaration                          #
# 3. Multiline string                            #
# 4. Concatenation                               #
# 5. String Action                               #
##################################################
number = 5

while number > 1:
    print(number)
    number -= 1 # number = number -1

print('Hello')
# number = 5
# print(5)
# number = 4
# print(4)
# number = 3
# print(3)
# number = 2
# print(2)
# number = 1

# Nested Loop: range นับเลข => ตัวแปรเก็บค่าที่นับ => ทำกระบวนการใน loop
for i in range(2, 5): # 2, 3, 4
    print('inner loop start')
    for j in range(1, 6, 3): # 1, 4
        print(i, j)
    print('out of inner loop')

apple_price = 50
pocket_money = 100
total_price = 0

for multiplier in range(1, 4):
    while total_price < pocket_money * multiplier:
        total_price += apple_price
        if total_price == 150:
            break

    print(total_price)
    total_price = 0

# String Declaration
# '23', "Hello"
print('''Hello
World''')
print("I'm hungey")
print('She said, "you will be late to school."')
# She said, "I'm hungey."
print('She said, "I\'m hungey."')
# Escaped Character \', \", \n
print('She said, \n"I\'m hungey."')

# Concatenation
print('Hello' + ' ' + 'World')
print('Hello' * 5) # 3 * 4 => 3 + 3 + 3 + 3, 'Hello' * 5 => 'Hello' + 'Hello' + 'Hello' +'Hello' + 'Hello'

sentence = 'Hello World'
# String Actions
print(len('Hello'))
print(len(sentence))

# indexing
print('Hello'[1])
print(sentence[8])

# slicing
print('Hello'[1:4])
print(sentence[2:7]) # 'lo Wo'
print(sentence[5:9])
print(sentence[1:7:2]) # 1 3 5
print(sentence[7:1:-2]) # 7 5 3
print(sentence[:7]) # 0, 1, 2, 3, 4, 5, 6
print(sentence[:7:3]) # 0, 3, 6
print(sentence[4:]) # 4, 5, 6, ..., string end
print(sentence[:])

# Negative index
print(sentence[-2])
print(sentence[-1:-7:-1])
print(sentence[:-7:-1])
print(sentence[-2::-1])