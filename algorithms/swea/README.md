# 알고리즘

코딩 체력 키우기!!

## 과제

### 1206번(21.02.08)

- 조망권 확보한 세대 구하기

```python
import sys
sys.stdin = open("hw1_input.txt", "r") # input 텍스트 저장한 파일을 불러오는 것.

for i in range(1,11):
    total = 0
    arr = []
    buildings = int(input()) # 테스트 케이스 길이 입력받기
    box = list(map(int, input().split())) # 빌딩들 리스트로 만들기
    for j in range(2, buildings-2):
        arr = [box[j-2], box[j-1], box[j+1], box[j+2]] # 최댓값 구해서 빼는거
        max_value = arr[0]
        for k in range(len(arr)): # 최댓값 구하기
            if max_value <= arr[k]:
                max_value = arr[k]
        if box[j] - max_value > 0: # 최댓값이 box[j] 보다 작을 경우만 봐야하니까
            total += box[j] - max_value

    print('#{} {}'.format(i, total))
```



### 1945(21.02.09)

- 간단한 소인수 분해

```python
def get_a(n):
    a = 0
    while n % 2 == 0:
        a += 1
        n //= 2
    return a
def get_b(n):
    b = 0
    while n % 3 == 0:
        b += 1
        n //= 3
    return b
def get_c(n):
    c = 0
    while n % 5 == 0:
        c += 1
        n //= 5
    return c
def get_d(n):
    d = 0
    while n % 7 == 0:
        d += 1
        n //= 7
    return d
def get_e(n):
    e = 0
    while n % 11 == 0:
        e += 1
        n //= 11
    return e

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{} {} {} {} {} {}'.format(tc, get_a(N), get_b(N), get_c(N), get_d(N), get_e(N)))
```



### 1208

- 평탄화

```python
def get_max(lst):
    max_value = lst[0]
    for i in range(len(lst)):
        if max_value < box[i]:
            max_value = box[i]
    return max_value

def get_min(lst):
    min_value = lst[0]
    for i in range(len(lst)):
        if min_value > box[i]:
            min_value = box[i]
    return min_value

for tc in range(1, 11):
    dump_case = int(input())
    box = list(map(int, input().split()))

    for i in range(dump_case):
        maxx = get_max(box) # 최댓값 구하기
        minn = get_min(box) # 최솟값 구하기
        idx_maxx = box.index(maxx) # 최댓값의 인덱스
        idx_minn = box.index(minn) # 최솟값의 인덱스
        box[idx_maxx] -= 1 # 제일 높은거에서 하나씩 줄여나가는 걸로 요소 갱신
        box[idx_minn] += 1 # 제일 낮은거에서 하나씩 올라가는 걸로 요소 갱신

    print('#{} {}'.format(tc, get_max(box) - get_min(box)))

```



### 5789

- 현주의 상자..

```python
T = int(input())
for k in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0]*N # 0 적힌 박스들 만들고
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R): # L에서 R만큼
            box[j] = i # 그 요소는 i로 바꾸기


    print('#{}'.format(k), *box) # 검색해보고 알았다!! 리스트 그냥 1 2 2 2 0 이런식으로 나타내는 방법 *list ! (언퍀)
```



### 1209 (21.02.15)

```python
N = 100
for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ss = []

    # 행
    for i in range(N):
        r_sum = 0
        for j in range(N):
            r_sum += arr[i][j]
            ss.append(r_sum)

    # 열
    for j in range(N):
        c_sum = 0
        for i in range(N):
            c_sum += arr[i][j]
            ss.append(c_sum)

    # 대각선
    d_sum = 0
    for i in range(N):
        d_sum += arr[i][i]
        ss.append(d_sum)

    maxx = -987654321
    for i in range(len(ss)):
        if maxx < ss[i]:
            maxx = ss[i]

    print('#{} {}'.format(tc, maxx))

```

> 이 문제는 그래도 쉬웠던 편!! 후딱 풀었다! 처음에 t를 전체 포문 밖에 잡아서 (이놈의 습관;;) 출력이 제대로 안나왔었는데 문제 다시 제대로 읽고 포문 안에 t잡고 출력 했더니 제대로 나왔당 ㅎㅎ

```python
N = 100
for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ss = []

    # 행
    for i in range(N):
        r_sum = 0
        for j in range(N):
            r_sum += arr[i][j]
            ss.append(r_sum)

    # 열
    for j in range(N):
        c_sum = 0
        for i in range(N):
            c_sum += arr[i][j]
            ss.append(c_sum)

    # 우하대각선
    d_sum = 0
    for i in range(N):
        d_sum += arr[i][i]
        ss.append(d_sum)

    # 좌하 대각선
    dd_sum = 0
    for i in range(N):
        dd_sum += arr[i][99-i]
        ss.append(dd_sum)

    maxx = -987654321
    for i in range(len(ss)):
        if maxx < ss[i]:
            maxx = ss[i]

    print('#{} {}'.format(tc, maxx))
```

> 대각선 하나를 안했었음 ㅋㅋㅋ 채점 테스트 케이스가 허술해서 pass 했나보다 ㅎㅎ 다시 풀었당



### 1954 달팽이 숫자

너무 어려웟음 ㅜㅜ

```python

```



### 1210 Ladder

```python
for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 좌 우 상
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
    c = 0
    for i in range(100):
        if ladder[99][i] == 2: # 2 인 c 찾기
            c = i
            break

    # 밑에서 올라오면서 찾기
    r = 99
    col = c
    dirr = 2
    while r >= 0:
        if dirr == 2: # 방향 위쪽일 때
            if 0 <= col-1 < 100 and ladder[r][col-1] == 1: # left
                r += dr[0]
                col += dc[0]
                dirr = 0 # 방향 왼쪽
            elif 0 <= col+1 < 100 and ladder[r][col+1] == 1: # right
                r += dr[1]
                col += dc[1]
                dirr = 1 # 방향 오른쪽
            else: # 그냥 위로
                r += dr[2]
                col += dc[2]

        elif dirr == 0: # 방향 왼쪽일때
            if 0<= r - 1 <= 100 and ladder[r-1][col] == 1:
                r += dr[2]
                col += dc[2]
                dirr = 2 # 방향 다시 위
            else: # 없으면 쭉 왼쪽으로
                r += dr[0]
                col += dc[0]

        else: # 방향 오른쪽 일때
            if 0 <= r-1 <= 100 and ladder[r-1][col] == 1:
                r += dr[2]
                col += dc[2]
                dirr = 2
            else: # 없으면 쭉 오른쪽으로
                r += dr[1]
                col += dc[1]

    print('#{} {}'.format(tc, col))
```







## Studying individually

### 2072번

- 홀수만 더하기

```python
tc = int(input())
for i in range(1, tc+1):
    answer = 0
    numbers = list(map(int, input().split()))
    for j in range(len(numbers)):
        if numbers[j] % 2:
            answer += numbers[j]
    print('#{} {}'.format(i, answer))
```



### 4828 min max

- 입력 받고 최대 최소 차이 출력하기

```python
def get_max(lst):
    max_value = lst[0]
    for i in range(len(lst)):
        if max_value < box[i]:
            max_value = box[i]
    return max_value

def get_min(lst):
    min_value = lst[0]
    for i in range(len(lst)):
        if min_value > box[i]:
            min_value = box[i]
    return min_value

T = int(input())
for tc in range(T):
    N = int(input())
    box = list(map(int, input().split()))
    answer = 0
    for i in range(len(box)):
        max_v = get_max(box)
        min_v = get_min(box)
        answer = max_v - min_v

    print('#{} {}'.format(tc+1, answer))
```



### 4834 숫자카드

```python

T = int(input())
for i in range(1, T+1):
    tc = int(input())
    box = list(map(int, input()))
    cnt = 0
    number_answer = 0
    for j in range(10):
        if box.count(j) >= cnt:
            cnt = box.count(j)
            number_answer = j

    print('#{} {} {}'.format(i, number_answer, cnt))

```

```python
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
```

> 이건 count 내장함수 안쓰고..

### 4835 구간합

```python
def my_sum(lst):
    s = 0
    for i in range(len(lst)):
        s += lst[i]
    return s

T = int(input()) # 인풋받기

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 인풋받기
    box = list(map(int, input().split())) # 인풋받은거 리스트로 만들기 
    max_value = min_value = my_sum(box[:M]) # 부분합 초기화
    answer = 0

    for i in range(0, N-M+1):
        small_sum = 0
        for j in range(M): # M만큼 부분합 구하기
            small_sum += box[i+j] # i 에서 j만큼 M까지 더하는 거니까

        if max_value < small_sum:
            max_value = small_sum
        if min_value > small_sum:
            min_value = small_sum

    answer = max_value - min_value

    print('#{} {}'.format(tc, answer))

```

```python
# 다른방법
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))
    max_value = min_value = my_sum(box[:M])
    # 중복 연산을 피하자

    # 첫구간 구해놓기
    small_sum = 0
    for i in range(M):
        small_sum += box[i]

    for i in range(M, N):
        small_sum = small_sum + box[i] - box[i - M]

        if max_value < small_sum:
            max_value = small_sum
        if min_value > small_sum:
            min_value = small_sum
    print('#{} {}'.format(tc, max_value - min_value))
```



### 4831 전기버스

```python
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # K: 이동할 수 있는 정류장 개수, N : 마지막 정류장 위치, M : 충전소 개수
    box = list(map(int, input().split())) # 충전기가 설치된 정류장 리스트
    bus_stop = [0] * (N+1)
    for i in box:
        bus_stop[i] = 1 # 충전소 표시

    bus = 0 # 버스 위치
    ans = 0 # 충전 횟수

    while True:
        bus += K # 버스가 이동할 수 있는 만큼 이동.
        if bus >= N: break # 종점에 도착하거나 더 나아가면 종료.

        for i in range(bus, bus-K, -1): # 최대한 이동 해놓고 한칸씩 뒤로 오면서 확인
            if bus_stop[i] == 1:
                ans += 1
                bus = i
                break
        else: # 충전기를 못찾았을때
            ans = 0
            break

    print('#{} {}'.format(tc, ans))

```

```python
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # K: 이동할 수 있는 정류장 개수, N : 마지막 정류장 위치, M : 충전소 개수
    box = list(map(int, input().split())) # 충전기가 설치된 정류장 리스트
    ans = 0

    box = [0] + box + [N] # = box.inser(0,0) , box.append(N)
    last = 0

    for i in range(1, M+2): # 출발점, 도착지 두칸 늘려놨으니까 M+2
        if box[i] - box[i-1] > K: # 차이가 K 보다 크면 아예 못가니까 충전 횟수 0
            ans = 0
            break # 끝나는거니까 break

            # 갈수 있다면 아무 작업 X, 갈수 없다면 내 바로 직전 충전소로 위치 옮기고 횟수 1 증가
        if box[i] > last + K:
            last = box[i-1]
            ans += 1

    print('#{} {}'.format(tc, ans))
```

> 밑에 풀이가 내가 생각했던 로직! 로직은 생각했는데 코드를 구현을 잘 못하고 있었는데 수업 들으면서 이해했다.



### 6485 삼성시 버스노선

```python
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     AB_all = []
#     for i in range(N):
#         A, B = map(int, input().split())
#         AB_all.append(list(range(A, B+1))) # 마지막으로 인풋값만 리스트돼서 값이 안나옴.. 인풋 값 다 리스트로 만들기는 못하는건가
#     P = int(input())
#     bus_stop_num = []
#     for j in range(P):
#         C = int(input())
#         bus_stop_num.append(C) # 버정 번호 리스트
#         cnt = [0] * P # 같은거 카운트할꺼
#         for k in AB_all:
#             for i in k:
#                 for h in bus_stop_num:
#                     if i == h:
#                         cnt[bus_stop_num.index(i)] += 1
#
#     print('#{}'.format(tc), *cnt)
```

> 처음에 생각했던 로직. 문제를 너무 어렵게 생각했다. 그냥 C번 정류장에 있는거 가져오면 되는거였음.

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    bus_stop = [0] * 5001 # 초기화 위치!!! 항상 잘 생각하기
    for i in range(N):
        A, B = map(int, input().split())

        for i in range(A, B+1):
            bus_stop[i] += 1

    P = int(input())
    cnt = []
    for i in range(P):
        C = int(input())
        cnt.append(bus_stop[C])

    print('#{}'.format(tc), *cnt)
```



### 1966 숫자정렬

```python
def BubbleSort(arr):
    for i in range(len(arr)-1, -1,-1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    BubbleSort(numbers)

    print('#{}'.format(tc), *numbers)
```



### 1959 두개의 숫자열

```python
def check(long, short):
    max_value = -987654321
    for i in range(len(long)-len(short)+1):
        result = 0
        for j in range(len(short)):
            result += long[i+j]*short[j]
        if max_value < result:
            max_value = result
    return  max_value

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        ans = check(A, B)
    else:
        ans = check(B, A)

    print('#{} {}'.format(tc, ans))
```



### 4836 색칠하기

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    co_plane = [[0] * 10 for _ in range(10)] # 평면좌표
    color = []
    cnt = 0 # 전체 좌표 에서 cnt 구해야 하니까 cnt 초기화는 여기서 !!
    for i in range(N):
        color.append(list(map(int, input().split())))

        for j in range(color[i][0], color[i][2] + 1): # x 좌표
            for k in range(color[i][1], color[i][3] + 1): # y 좌표
                if color[i][4] == 1: # 빨강이면
                    co_plane[j][k] += 1

                elif color[i][4] == 2: # 파랑이면
                    co_plane[j][k] += 10

                if co_plane[j][k] % 11 == 0:
                    cnt += 1


    print('#{} {}'.format(tc, cnt))
```



### 4839 이진탐색

```python
def bi_search(lst,key):
    left = 0
    right = len(lst)-1
    cnt = 0
    while left <= right:
        middle = (left+right)//2
        if lst[middle] == key:
            break
        elif key < lst[middle]: # if 말고 elif ! 아니라면 이어야 하니까
            right = middle
            cnt += 1
        elif key > lst[middle]:
            left = middle
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    book = [0] * P
    for i in range(0, P):
        book[i] = i+1

    if bi_search(book, Pa) < bi_search(book, Pb):
        ans = 'A'
    if bi_search(book, Pa) == bi_search(book, Pb):
        ans = 0
    if bi_search(book, Pa) > bi_search(book, Pb):
        ans = 'B'


    print('#{} {}'.format(tc, ans))
```



### 4837 부분집합의 합

```python
def get_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << len(A)):
        arr = []

        for j in range(len(A)):
            if i & (1 << j):
                subset = A[j]
                arr.append(subset)  # arr 은 부분집합

        if len(arr) == N and get_sum(arr) == K: # 부분집합 중 N개의 원소 갖고 있고 합이 K 이면
                cnt += 1

    print('#{} {}'.format(tc, cnt))

```



### 4838 특별한 정렬

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 정렬
    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        tmp = lst[i]
        lst[i] = lst[min_idx]
        lst[min_idx] = tmp

    ans = [0] * len(lst)
    for i in range(len(lst)):
        if i % 2: # 홀수 인덱스에 lst 인덱스 0, 1, 2 이순서로 온다.
            ans[i] = lst[i//2]

        elif i % 2 == 0: # 짝수 인덱스에는 list 인덱스의 len(lst)-1, len(lst)-2, len(lst)-3 이순서로 온다.
            ans[i] = lst[len(lst)-(i//2+1)]

    print('#{}'.format(tc), *ans[:10]) # 10개만 출력하라는 문제이므로.
```



### 1979 어디에 단어가 들어갈 수 있을까

```python

```



### 1966 숫자정렬

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    # 선택정렬
    for i in range(len(box)-1):
        min_idx = i
        for j in range(i+1, len(box)):
            if box[min_idx] > box[j]:
                min_idx = j
        tmp = box[i]
        box[i] = box[min_idx]
        box[min_idx] = tmp

    print('#{}'.format(tc), *box)
```

