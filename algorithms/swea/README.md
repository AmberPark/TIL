# 알고리즘

코딩 체력 키우기!!



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



