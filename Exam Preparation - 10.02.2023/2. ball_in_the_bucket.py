size = 6
matrix = [input().split(" ") for _ in range(size)]
hits = []
total_points = 0

for _ in range(3):
    points = 0
    coordinates = list(map(int, input().strip("()").split(", ")))  # [1, 1]
    r, c = coordinates
    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == "B" and (r, c) not in hits:
            for row in matrix:
                if row[c] == "B":
                    hits.append((r, c))
                    continue
                points += int(row[c])
    total_points += points

if total_points < 100:
    diff = 100 - total_points
    print(f"Sorry! You need {diff} points more to win a prize.")

elif 100 <= total_points <= 199:
    prize = "Football"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
elif 200 <= total_points <= 299:
    prize = "Teddy Bear"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    prize = "Lego Construction Set"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")