num_robots = int(input()) # 8
total = 0
# expected_total = 0

# 1 2 3 4 5 6 7 8
# 6 2 4 3 1 5 8
for _ in range(num_robots - 1):
    robot = int(input())
    total += robot # total = total + robot

# for number in range(1, num_robots + 1): # 1 + 2 + 3 + ... + 8
#     expected_total += number

# 1 + 2 + ... + 200 => (ต้น + ปลาย) * จำนวน // 2
expected_total = (1 + num_robots) * num_robots // 2 # / => float
print(expected_total - total)
