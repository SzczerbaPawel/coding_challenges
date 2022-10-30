def is_triangular(num):
    triTest = ((1 + 8 * num)**0.5 - 1.0) / 2.0;
    return triTest == (int(triTest))


def is_pentagonal(num):
    penTest = ((1 + 24 * num)**0.5 + 1.0) / 6.0;
    return penTest == (int(penTest))


def is_hexagonal(num):
    hexTest = ((1 + 8 * num)**0.5 + 1.0) / 4.0;
    return hexTest == (int(hexTest))


iter = 286
while True:
    number = iter * (iter + 1) / 2
    if is_pentagonal(number) and is_hexagonal(number):
        print(number)
        break
    iter += 1