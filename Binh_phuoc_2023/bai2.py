S = input()

def solution(S):
    count = 0
    max_count = 0

    for i in range(len(S)):
        if S[i] == "0":
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    if count > max_count:
        max_count = count

    return count 

print(solution(S))
