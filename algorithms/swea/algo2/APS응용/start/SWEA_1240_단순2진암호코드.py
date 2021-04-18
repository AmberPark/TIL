import sys
sys.stdin = open("1240.txt", "r")

pas = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
       '0110111': 8, '0001011': 9}

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    ans = 0
    # print(arr)
    stk = []
    # 열로 내려가면서 1이 있는 행 뽑아오기
    for i in range(n):
        if '1' in arr[i]:
            for j in range(m):
                stk.append(arr[i][j])
            break
    # print(stk)

    new = []
    # 해당 행에서 암호 부분 뽑아오기
    for i in range(len(stk) - 1, -1, -1):
        # 뒤에서 부터 탐색하면서 1 있는 곳부터 거꾸로 뽑아오기
        # 뒤에서 부터 보다가 1이 있으면?? 쭉 가져오기
        if stk[i] == '1':
            # print(i)
            # 얼마나 뽑을 것인가?
            # 뒤에서 부터 56개 뽑아오기
            new = stk[i:i-56:-1]
            break
    # print(new)
    # print(len(new))

    sp = []
    for i in range(len(new) // 7):
        # 뒤에서 부터 뽑아줘서 거꾸로 뒤집어줘야한다
        sp.append(reversed(new[i * 7:i * 7 + 7]))

    p = []
    for i in range(len(sp) - 1, -1, -1):
        a = ''.join(sp[i])
        for k, v in pas.items():
            if a == k:
                p.append(v)

    # 여기서는 if len(p) > 0: 뺏어!
    result1 = 0
    result2 = 0
    for i in range(len(p) // 2):
        result1 += p[i * 2] * 3
        result2 += p[i * 2 + 1]
        ans = result1 + result2
    if ans % 10 == 0:
        result = sum(p)

        print('#{} {}'.format(tc, result))
    else:
        print('#{} {}'.format(tc, 0))