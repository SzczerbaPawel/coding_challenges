def is_pentagonal(num):
    penTest = ((1 + 24 * num)**0.5 + 1.0) / 6.0;
    return penTest == (int(penTest));


for i in range(2, 2168):
    print(i)
    for j in range(1, i):
        # print(i,j)
        A = i*(3*i-1)/2
        B = j*(3*j-1)/2
        D = max([A, B]) - min([A, B])
        if not is_pentagonal(A+B):
            # print(f"Skipping because sum {A+B} is not pentagonal")
            continue
        if not is_pentagonal(D):
            # print(f"Skipping because difference {A+B} is not pentagonal")
            continue
        print(f"Found {A} {B} {D}")
        break

