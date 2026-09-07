n, x = map(int, input().split())


def solution_sub1(n, x):
    ans = 0

    i = 1
    while i * i <= x:
        if x % i == 0:
            j = x // i

            if i <= n and j <= n:
                if i == j:
                    ans += 1
                else:
                    ans += 2

        i += 1

    return ans


print(solution_sub1(n, x))