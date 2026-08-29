n = int(input())

warn = ['H', 'S', 'G', 'P', 'T']

name = []

for _ in range(n):
    player = input()

    if player[0] in warn:
        name.append(player)

H = S = G = P = T = 0

for player in name:
    if player[0] == 'H':
        H += 1
    elif player[0] == 'S':
        S += 1
    elif player[0] == 'G':
        G += 1
    elif player[0] == 'P':
        P += 1
    else:
        T += 1

ans = (H*S*G + H*S*P + H*S*T + H*G*P + H*G*T + H*P*T + S*G*P + S*G*T + S*P*T + G*P*T)

print(ans)