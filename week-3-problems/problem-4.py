first_chest = int(input())
second_chest = int(input())
third_chest = int(input())

# b > c a == c => a, b
# a,b => a >= c and b >= c
# b,c => b > a and c > a
# a,c => a > b and c > b

if first_chest >= third_chest and second_chest >= third_chest:
    print(first_chest + second_chest)
elif first_chest >= second_chest and third_chest > second_chest:
    print(first_chest + third_chest)
else:
    print(second_chest + third_chest)
