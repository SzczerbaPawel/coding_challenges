result = 0
max_counter = 0

for p in range(10, 1001):
    counter = 0
    for a in range(p // 3, p - 1):
        ran = p-a
        for b in range(-(ran // -2), min(a, ran)):
            c = p - a - b
            if (b ** 2 + c ** 2) == a ** 2:
                counter += 1
    print(f"Found {counter} matches for {p}")
    if counter > max_counter:
        max_counter = counter
        result = p

print(result)
