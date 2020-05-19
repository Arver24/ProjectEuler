n = 200000
c = 0
tn = 0
end = 0
stop = n
for i in range(1, stop):
    c = 0
    tn = (i * (i + 1)) / 2
    if (tn ** (1 / 2)) == int(tn ** (1 / 2)):
        end = int(tn ** (1 / 2))
    else:
        end = int(tn ** (1 / 2)) + 1
    for j in range(1, end):
        if tn % j == 0:
            c += 1

    if ((c * 2) + 1) > 500:
        break


# print(tn, n, i, stop)
print(tn)
# print(end)
