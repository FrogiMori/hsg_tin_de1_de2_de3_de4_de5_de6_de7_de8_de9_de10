def tong_uoc(num):
    tong = 0
    i = 1

    while i * i <= num:
        if num % i == 0:
            tong += i

            if i != num // i:
                tong += num // i

        i += 1

    return tong


n = int(input())
X = list(map(int, input().split()))

for num in X:
    s = tong_uoc(num)

    if s >= 2 * num:
        print(1)
    else:
        print(0)