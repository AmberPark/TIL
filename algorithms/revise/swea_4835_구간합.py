for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    result = []
    for i in range(N-M+1):
        s = lst[i:i+M]
        result.append(sum(s))

    ans = max(result) - min(result)

    print(f'#{tc} {ans}')
