# number of flowers in the k days = number of flowers in day 0 * 3 ** day
num_starting_flowers = int(input())
num_day = int(input())

print(num_starting_flowers * 3**num_day)
