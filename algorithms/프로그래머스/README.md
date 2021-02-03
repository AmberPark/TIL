# 코딩테스트

> 개인공부 + 스터디

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



### 4. k번째 수

- 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하기.
- 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
  - array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
  - 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
  - 2에서 나온 배열의 3번째 숫자는 5입니다.

```python
def solution(array, commands):
    answer = []
    for c in commands:
        s_lst = sorted(array[c[0]-1:c[1]])
        answer.append(s_lst[c[2]-1])
        
    return answer
```

> 문제 잘읽자!! 첨에 번째를 요소로 혼자 해석하고 예시 안보고 풀다가  array[c[0]:c[1]+1] 이런 식으로 구해서 계속 에러가 났었다.. 도대체 이유가 뭘까 혼자 몇십분동안 고민하고 ㅋㅋㅋ 뭔가 잘 안나온다 싶으면 문제부터 다시보기!~!



### 5. 가운데 글자 가져오기

- 단어 s의 가운데 글자를 반환하는 함수, solution 만들기. 단어의 길이가 짝수라면 가운데 두글자를 반환.

```python
def solution(s):
    answer = ''
    if len(s)%2:
        answer = s[len(s)//2]
    else:
        answer = s[len(s)//2-1:len(s)//2+1]
    return answer
```



### 6. 모의고사

- 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

  1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
  2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
  3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

  1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

```python
def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for idx, ans in enumerate(answers):
        if ans == person1[idx%5]: # 1번사람은 5개가지고 찍으니까. 만약 6번째면 다시 첫번째 요소로 와야하니까!!
            cnt1 += 1
            
        if ans == person2[idx%8]: # elif는 else if 이므로 if 조건이 아니면 돌아가는 함수이다. 지금은 1,2,3번 사람 다 돌아야 하므로 if를 세번 쓴다
            cnt2 += 1
        if ans == person3[idx%10]:
            cnt3 += 1
            
    count_lst = [cnt1, cnt2, cnt3]
    for c, cnt in enumerate(count_lst):
        if cnt == max(count_lst):
            answer.append(c+1) # 왜 3명다일경우 3명까지 안나오지?
    
    return answer
```



### 7. 완주하지 못한 선수

- 

```python
def solution(participant, completion):
    answer = ''
       
    for person in participant:
        if person not in completion:
            answer = person
        #동명이인이 있으면 
        #동명이인모두가 완주한 경우가 아닐때만 
        if participant.count(person) != completion.count(person):
            answer = person
            
    return answer
```

> 효율성 테스트 실패.. 흠..🤔 어떻게 시간을 줄이지? if 조건문이 너무 길어서 그런가?

```python
def solution(participant, completion):
    answer = ''
       
    for person in participant:
        if participant.count(person) != completion.count(person):
            answer = person
            
    return answer
```

> 생각해보니 카운트 개수가 다를 때만 반환하면 되니까 if 조건문 하나만 있어도 된다. 근데 여전히 효율성 에서 실패다.😂








