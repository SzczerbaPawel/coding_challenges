res = 0

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        if a**5 + b**5 + c**5 + d**5 + e**5 + f**5 == a*100000+b*10000+c*1000+d*100+e*10+f:
                            print("Number found: " + str(a*100000+b*10000+c*1000+d*100+e*10+f))
                            res = res + a*100000+b*10000+c*1000+d*100+e*10+f

print(res)