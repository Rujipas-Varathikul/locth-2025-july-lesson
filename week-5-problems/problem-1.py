# 2, 9 => 2, 4, 6, 8
# 2, 6 => 2, 4, 6
start = int(input())
stop = int(input())

# range
for number in range(start, stop + 1): # 2, 3, ..., 8
    if number % 2 == 0:
        print(number)
