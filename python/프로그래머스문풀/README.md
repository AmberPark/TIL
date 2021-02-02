# 코딩테스트

## 연습문제

### 1. 나누어 떨어지는 숫자 배열

- array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성. divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환.

```python
def solution(arr, divisor):
    answer = []
    final = []
    for i in arr:
        if i % divisor ==0: 
            answer.append(i)
            final = sorted(answer)
        if len(final) ==0: # 나누어 떨어지는 요소가 없으면 final 개수가 0이 되므로
            final.append(-1)
     
    return final
```

> 시간이 좀 오래 걸리더라..? ㅎㅎ 다른 사람 풀이를 봤는데 진짜 깔끔한 한줄로 출력했더라.

```python
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
```



### 2. 체육복

- 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성.  바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다.

```python
def solution(n, lost, reserve):
    answer = 0
    #잃어버렸고 여분도 있는 사람 빼기
    # 중복 피하기 위해 set 사용
    real_reserve = set(reserve) - set(lost)
    # 진짜 잃어버린 사람
    real_lost = set(lost) - set(reserve)
    answer = n - len(real_lost)
    
    for loser in real_lost:
        if loser-1 in real_reserve: 
            answer += 1
            real_reserve -= {loser-1} # 있으면 real_reserve 에서 빼기
        elif loser+1 in real_reserve:
            answer += 1
            real_reserve -= {loser+1}
            
        else: continue
    return answer
    
```

> 첨에 혼자 고민하고있었는데 이건 아니다 싶어서 반 학우분의 코드를 봤다. ㅠ접근방식부터 달랐어.. 정말.. 열심히해야겠구나 를 또 느꼈다 ㅎ

```python
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
```

> 다른사람 풀이..진짜.. 너무깔끔해..



### 3. 소수찾기

```python
def solution(n):
    if n == 2:
        return 1
    
    answer = 1 
    for i in range(2, n+1):
        for j in range(2, int(i**(1/2))+2):
            if i % j == 0:
                break
        else:
            answer +=1
    
    return answer
```

> 일단.. 반 학우분이.. 써주신거.. 난 문제도 못봤다 두번째꺼 푸느라 . 내일 다시 봐야지












