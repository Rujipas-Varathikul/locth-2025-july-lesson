# create 2 variables: alice_win_number, bob_win_number
# loop string and increase number of win for Alice or Bob
game_result = input()
num_a = 0
num_b = 0

for result in game_result:
    if result == 'A':
        num_a += 1
    else:
        num_b += 1

if num_a > num_b:
    print('ALICE')
elif num_b > num_a:
    print('BOB')
else:
    print('DRAW')
