t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    apt = [i for i in range(1, n+1)] # 0층
    # k층 n호 = k층 n-1호 인원 + k-1층 n호 인원
    for j in range(k):
        for h in range(1, n):
            apt[h] += apt[h-1]

    print(apt[-1])
