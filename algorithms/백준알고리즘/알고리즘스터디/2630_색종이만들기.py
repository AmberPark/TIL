import sys
sys.stdin = open("2630.txt", "r")
# 4등분 한게 모두 같은 색일때까지 반복 => 재귀를 써야할듯 ?

def divide(arr, N):
    global total_blue, total_white
    # 첫번째 구역
    one = []
    for i in range(N//2):
        lst = []
        for j in range(N//2):
            lst.append(arr[i][j])
        one.append(lst)
    cnt1 = 0
    for a in range(len(one)):
        for b in range(len(one)):
            if one[a][b] == 1:
                cnt1 += 1
    if cnt1 == (len(one)) ** 2:
        total_blue += 1

    elif cnt1 == 0:
        total_white += 1

    else:
        divide(one, N//2)


    # 두번째 구역
    second = []
    for i in range(N//2):
        lst2 = []
        for j in range(N//2, N):
            lst2.append(arr[i][j])
        second.append(lst2)
    cnt2 = 0
    for a in range(len(second)):
        for b in range(len(second)):
            if second[a][b] == 1:
                cnt2 += 1
    if cnt2 == (len(second)) ** 2:
        total_blue += 1

    elif cnt2 == 0:
        total_white += 1

    else:
        divide(second, N//2)

    # 세번째 구역
    third = []
    for i in range(N//2, N):
        lst3 = []
        for j in range(N//2):
            lst3.append(arr[i][j])
        third.append(lst3)
    cnt3 = 0
    for a in range(len(third)):
        for b in range(len(third)):
            if third[a][b] == 1:
                cnt3 += 1
    if cnt3 == (len(third)) ** 2:
        total_blue += 1

    elif cnt3 == 0:
        total_white += 1
    else:
        divide(third, N//2)


    #네번째 구역
    forth = []
    for i in range(N//2, N):
        lst4 = []
        for j in range(N//2, N):
            lst4.append(arr[i][j])
        forth.append(lst4)
    cnt4 = 0
    for a in range(len(forth)):
        for b in range(len(forth)):
            if forth[a][b] == 1:
                cnt4 += 1
    if cnt4 == (len(forth)) ** 2:
        total_blue += 1

    elif cnt4 == 0:
        total_white += 1
    else:
        divide(forth, N//2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total_blue = 0
total_white = 0

tmp = 0
for row in range(N):
    for col in range(N):
        if arr[0][0] == 1:
            if arr[row][col] == 0:
                tmp = 1
        else:
            if arr[row][col] == 1:
                tmp = 1

# 한가지 색이 아니면 함수 시작
if tmp ==1:
    divide(arr, N)
# 한가지 색이면 그 색 카운드!
else:
    if arr[0][0] == 1:
        total_blue += 1
    else:
        total_white += 1
print(total_white)
print(total_blue)