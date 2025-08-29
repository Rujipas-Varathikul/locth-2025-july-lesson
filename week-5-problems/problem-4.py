num_game = int(input()) # 5
best_score = 0

for _ in range(num_game):
    score = int(input())
    if score > best_score:
        best_score = score

print(best_score)