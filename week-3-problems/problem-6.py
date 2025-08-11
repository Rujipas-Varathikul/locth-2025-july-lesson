num_orange_cake = int(input())
num_apple_cake = int(input())
bag_1_size = int(input())
bag_2_size = int(input())

if bag_1_size >= num_orange_cake and bag_2_size >= num_apple_cake:
    print('YES')
elif bag_1_size >= num_apple_cake and bag_2_size >= num_orange_cake:
    print('YES')
else:
    print('NO')

if bag_1_size >= num_orange_cake:
    if bag_2_size >= num_apple_cake:
        print('YES')
    elif bag_1_size >= num_apple_cake:
        if bag_2_size >= num_orange_cake:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else: # bag_1_size < num_orange_cake
    if bag_1_size >= num_apple_cake:
        if bag_2_size >= num_orange_cake:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    