def tong_uoc(num):
    tong = 0
    i = 1

    while i * i <= num:
        if num % i == 0:
            tong += i

            if i != num // i:
                tong += num // i

        i += 1

    return tong - num

n = int(input())
A = list(map(int,input().split()))

count = 0
qua = []

for num in A :
    if tong_uoc(num) == num :
        count += 1
        qua.append(num)

    else :
        continue

print(count)
for i in qua :
    print (i , end = '  ')