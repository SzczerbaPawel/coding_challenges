import datetime

res = 0

for i in range(1901, 2001):
    for j in range(1, 13):
        if datetime.datetime(year=i, month=j, day=1).weekday() == 6:
            res += 1

print(res)
