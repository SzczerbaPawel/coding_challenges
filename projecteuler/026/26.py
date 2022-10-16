def reciprocal_cycles(denuminator):
    numinator = 10 ** len(str(denuminator))
    lst = []
    counter = 0
    while True:
        rest = numinator % denuminator
        if rest == 0:
            return 0
        if rest in lst:
            return counter
        else:
            lst.append(rest)
            counter = counter + 1
        numinator = rest * 10


cycles=[]
for i in range(1, 1000):
    temp = reciprocal_cycles(i)
    print(i, temp)
    cycles.append(temp)

print(max(cycles))