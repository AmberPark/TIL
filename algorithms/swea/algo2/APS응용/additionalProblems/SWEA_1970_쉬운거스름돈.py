for tc in range(1, int(input()) + 1):
    money = int(input())
    # 각 단위별 돈 ( 50000원 권이 맨 앞)
    m = [0] * 8
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        if money // lst[i] != 0:
            m[i] = money // lst[i]
            # 갱신
            money = money % lst[i]
    print('#{}'.format(tc))
    print(*m)
