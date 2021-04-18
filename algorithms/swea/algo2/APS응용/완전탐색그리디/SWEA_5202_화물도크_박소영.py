for tc in range(1, int(input()) +1):
    n = int(input())
    t = []
    for _ in range(n):
        start_end = list(map(int, input().split()))
        t.append(start_end)

    # 끝나는 시간 기준으로 오름차순 정렬
    for i in range(n):
        for j in range(i, n):
            if t[i][1] > t[j][1]:
                t[i], t[j] = t[j], t[i]

    # print(t)
    res = []
    first = t.pop(0) # 처음 시작 시잔
    res.append(first)
    while t:
        next_one = t.pop(0)
        if next_one[0] >= first[1]:
            res.append(next_one)
            first = next_one #  갱신
    #
    # print(res)
    ans = len(res)

    print('#{} {}'.format(tc, ans))