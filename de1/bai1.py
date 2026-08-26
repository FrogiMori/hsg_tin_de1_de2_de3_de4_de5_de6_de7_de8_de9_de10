n = int(input())
a = list(map(int,input().split()))
def solution(n,a):
    odd = 0

    for x in a:
        if x % 2 == 1:
            odd += 1

    ans = n * (n - 1) // 2 - odd * (odd - 1) // 2

    return ans 

print(solution(n,a))