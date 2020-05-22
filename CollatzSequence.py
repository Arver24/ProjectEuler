n = 999999
c = 0
maxcount = 0
maxnum = 0
for i in range(1, 1000000):
    c = 0
    n = i
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            c += 1

        else:
            n = 3 * n + 1
            c += 1

    if c > maxcount:
        maxcount = c
        maxnum = i
print(maxnum)
