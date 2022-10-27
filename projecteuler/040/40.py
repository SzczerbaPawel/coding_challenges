res = ""
iter = 1
while len(res) < 1000000:
    res += str(iter)
    iter += 1


result = 1
for i in range(1, 7):
    result *= int(res[10**i - 1])
print(result)
