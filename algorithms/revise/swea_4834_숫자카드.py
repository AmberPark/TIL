T = int(input())
for i in range(1, T+1):
    tc = int(input())
    box = list(map(int, input()))
    cnt_lst = [0] * 10
    for j in range(tc):
        cnt_lst[box[j]] += 1

    max_v = max_num = 0
    for k in range(len(cnt_lst)-1, -1, -1): # 카드 장수가 같으면 숫자가 큰 쪽을 출력해야 하므로
        if cnt_lst[k] > max_v:
            max_v = cnt_lst[k]
            max_num = k

    print('#{} {} {}'.format(i, max_num, max_v))

