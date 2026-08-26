MOD = 10**9 + 7

n = int(input())

if n == 1:
    print(3)
    exit()

a1 = 3
a2 = 8

for i in range(3, n + 1):
    a = (2 * a2 + 2 * a1) % MOD
    a1 = a2
    a2 = a

print(a2)