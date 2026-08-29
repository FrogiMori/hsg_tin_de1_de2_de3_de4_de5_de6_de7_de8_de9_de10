n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = abs(A[0] + B[0])  

for i in range(n):
    for j in range(n):
        gia_tri = abs(A[i] + B[j])
        if gia_tri < ans:
            ans = gia_tri

print(ans)