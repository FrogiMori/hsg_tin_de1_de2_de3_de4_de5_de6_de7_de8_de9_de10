n = int(input())
A = list(map(int, input().split()))

def solution(A):
    freq = {}

    for x in A:
        freq[x] = freq.get(x, 0) + 1

    ans = 0

    for key, val in freq.items():
        if val < key:
            ans += val
        else:
            ans += val - key

    return ans

print(solution(A))
