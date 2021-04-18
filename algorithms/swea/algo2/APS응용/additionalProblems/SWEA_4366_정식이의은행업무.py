def binn_dec(binn):
    ans = 0
    for i in range(len(binn)-1, -1, -1):
        ans += int(binn[i]) * (2 ** ((len(binn)) - i - 1))
    return ans

def tri_dec(tri):
    ans = 0
    for i in range(len(tri)-1, -1, -1):
        ans += int(tri[i]) * 3**((len(tri)) - i - 1)
    return ans

# 이진수 숫자 하나씩 바꾼거 넣은 리스트랑  삼진수 숫자 하나씩  바꾸면거 넣은 리스트
# 그중에 같은 값 있으면 그거 출력하도록
for tc in range(1, int(input()) +1):
    binn = list(input())
    tri = list(input())
    new_b = []
    new_t = []
    for i in range(len(binn)):
        if binn[i] == '1':
            new_b.append(binn_dec(binn) - 2 ** (len(binn)- i - 1))
        else:
            new_b.append(binn_dec(binn) + 2 ** (len(binn)- i - 1))


    for i in range(len(tri)):
        if tri[i] == '0':
            # 1로 바꿀때
            new_t.append(tri_dec(tri) + 1 * 3**(len(tri) -i-1))
            # 2로 바꿀때
            new_t.append(tri_dec(tri) + 2 * 3**(len(tri) -i-1))
        elif tri[i] == '1':
            # 0으로 바꿀때
            new_t.append(tri_dec(tri) - (1 * 3**(len(tri) -i-1)))
            # 2로 바꿀때
            new_t.append(tri_dec(tri) + 1 * 3**(len(tri) -i-1))
        elif tri[i] == '2':
            # 0으로 바꿀 때
            new_t.append(tri_dec(tri) - (2 * 3**(len(tri) -i-1)))
            # 1로 바꿀 때
            new_t.append(tri_dec(tri) - (1 * 3**(len(tri) -i-1)))

    for i in range(len(new_b)):
        for j in range(len(new_t)):
            if new_b[i] == new_t[j]:
                ans = new_b[i]

                break

    print('#{} {}'.format(tc, ans))
