numerator = 1
denominator = 1

for a in range(1, 10):
    for b in range(1, 10):
        for x in range(1, 10):
            n1 = 10 * a + x
            n2 = 10 * x + b
            if n1 / n2 == a / b and a != b:
                print(f"n1={n1} n2={n2}")
                numerator = numerator * a
                denominator = denominator * b

print(f"{numerator} {denominator}")
