def prime(n):
    for j in range(2, int(n ** (1 / 2)) + 1):
        if n % j == 0:
            return False
    return True


num = 2000000

ans = 2
for i in range(3, num + 1, 2):
    if prime(i):
        ans += i
        print(i, ans)
    # //for j in range(2, int(i ** (1 / 2)) + 1):
    #     //if i % j == 0:
    #         //break
    # //ans += i
    # //print(i)

# //print(ans)
