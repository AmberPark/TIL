def Bbit_print(i):
    output = ""
    for j in range(31, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    binn = Bbit_print(m)
    ans ='OFF'
    end = binn[len(binn) - n:]
    cnt = 0
    for i in end:
        if i == '1':
            cnt += 1
    if cnt == n:
        ans = 'ON'

    print('#{} {}'.format(tc, ans))