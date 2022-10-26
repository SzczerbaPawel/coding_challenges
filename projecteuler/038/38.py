def check_pandemical(cat):
    for digit in range(1, 10):
        if cat.count(str(digit)) != 1:
            return False
    return True


result = 0
for i in range(1, 10000000):
    mult = 1
    cat = ""
    while len(cat) < 9:
        cat += str(i*mult)
        mult += 1
    if len(cat) == 9 and check_pandemical(cat):
        print(i, cat)
        if int(cat) > result:
            result = int(cat)
print(result)
