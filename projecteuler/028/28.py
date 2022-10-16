res = 1

for i in range(1, 501):
    A = (2 * i + 1) ** 2
    B = (2 * i) ** 2 + 1
    C = (A + B) / 2
    D = B - (A - B) / 2
    # print("A = " + str(A))
    # print("B = " + str(B))
    # print("C = " + str(C))
    # print("D = " + str(D))
    res = res + A + B + C + D

print(res)

