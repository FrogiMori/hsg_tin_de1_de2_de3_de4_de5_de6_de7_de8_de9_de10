N, M = map(int, input().split())
A = []
for _ in range(M):
    a, b = map(int, input().split())
    A.append((b, a))

A.sort(reverse=True)


def solution(A,N) :
    ans = 0

    for b, a in A:
        take = min(N, a)

        ans += take * b
        N -= take

        if N == 0:
            break

    return ans 

print(solution(A,N))