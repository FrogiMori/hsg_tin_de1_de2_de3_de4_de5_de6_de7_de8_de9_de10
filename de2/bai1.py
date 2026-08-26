n = int(input())
N = list(map(int, input().split()))

def solution(N):
    result = 0

    for num in N:
        if num == 0:
            continue

        count = 0

        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                count += 1
                if i != num // i:
                    count += 1

        result += num * count

    return result

print(solution(N))