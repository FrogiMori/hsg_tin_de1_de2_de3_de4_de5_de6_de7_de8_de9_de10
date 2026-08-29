import math
a, b = map(int, input().split())
n = math.isqrt(b)

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, math.isqrt(n) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False


def doi_xung(num):
    s = str(num)
    return s == s[::-1]


left = math.isqrt(a)
if left * left < a:
    left += 1

right = math.isqrt(b)

count = 0

for num in range(left, right + 1):
    if is_prime[num] and doi_xung(num):
        count += 1

print(count)