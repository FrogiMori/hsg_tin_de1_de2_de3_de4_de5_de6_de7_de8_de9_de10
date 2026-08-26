n ,K = map(int, input().split())
binary_num = input()

def binary_mul(binary_num, K):
    num = int(str(binary_num) ,2)
    int_num = num * K
    result = bin(num * K)

    return result[2:]  

print(binary_mul(binary_num, K))