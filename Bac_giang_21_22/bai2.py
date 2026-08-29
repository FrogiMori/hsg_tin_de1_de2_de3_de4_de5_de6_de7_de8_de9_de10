n = int(input())
h = int(input())

is_composite = [False] * (n + 1)
if n >= 0:
    is_composite[0] = True
if n >= 1:
    is_composite[1] = True

i = 2
while i * i <= n:
    if not is_composite[i]:
        for j in range(i * i, n + 1, i):
            is_composite[j] = True
    i += 1

def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

result = []
for num in range(2, n + 1):
    if not is_composite[num] and digit_sum(num) == h:
        result.append(num)

for p in result:
    print(p)
print(len(result))