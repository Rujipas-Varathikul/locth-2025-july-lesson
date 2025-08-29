num_inputs = int(input()) # ??
counter = 0

for _ in range(num_inputs):
    number = int(input())

    if number == 0:
        counter += 1

print(counter)
