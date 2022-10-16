values = [1, 2, 5, 10, 20, 50, 100, 200]

goal = 200

a = [[0 for i in range(0, goal+1)] for j in range(0, len(values))]
print(a)

for i in range(0, len(values)):
    for j in range(0, goal+1):
        print(i, j)
        if j == 0:
            a[i][j] = 1
        elif values[i] > j:
            a[i][j] = a[i-1][j]
        else:
            a[i][j] = a[i-1][j]+a[i][j-values[i]]

print(a)
