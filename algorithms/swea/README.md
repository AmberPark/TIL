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


    print('#{}'.format(k), *box) # 검색해보고 알았다!! 리스트 그냥 1 2 2 2 0 이런식으로 나타내는 방법 *list ! 
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
    for k in range(len(cnt_lst)-1, -1, -1):
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



### 4831 전기버스

```python

```

