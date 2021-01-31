# Intro

### 기초

- 파이썬은 한줄에 한문장이 원칙.

```python
print('hello')print('world')
print('hello
world') # 이대로 쓸려면 hello 바로 뒤에 \ 을 사용 해야함
```

> 위의 예시들은 다 에러 나는 것. 



### 변수

- 다른값 동시에 할당 가능

```python
x, y = 1, 10
print(x, y) # => 1 10
```

- 변수 x, y값 바꾸기

```python
# 임시 변수 활용
temp = x
x = y 
y = temp
print(x, y) 
```

```python
# x, y = 1, 10
x = 10
y = 100
x, y = y, x
print(x, y)
```



- 식별자  : 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어. 주로 변수 또는 함수 이름 등으로 사용.
  - 키워드 사용할 수 없음. `import keyword` 하고  `print(keyword.kwlist)` 로 출력하면 파이썬의 키워드 나옴
  - 특수문자는 언더바(_)만 허용
  - 숫자로 시작하면 안됨
  - 공백 포함 x
  - 내장함수(Built-in function)나 모듈 등의 이름으로도 만들면 안됨. ex)  print
  
  
  
- 실수 연산

```python
3.5 - 3.12 => 0.3799999999999999
3.5 - 3.12 == 0.38 # => False  띠요옹

# 따라서 처리방법
# 1.
a = 3.5 - 3.12
b = 0.38
abs(a - b) <= 1e-10
# 2.sys 모듈을 통해 처리. `epsilon` 은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환
import sys
abs(a - b) <= sys.float_info.epsilon
# 3.
import math
math.isclose(a, b)
# 세개 다 True
```



- `0` `0.0` `()` `[]` `{}` `''` `None` 은 False로 변환.
- 논리연산자

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

```
True
False
False
False
```

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

```
True
True
True
False
```

```python
# and : 둘다 True여야 True.
# 첫번째 True, 두번째것도 확인해야함.
# 5
print(3 and 5)
print(3 and 0)
# 첫번째 : 0 => False, 빼박... False!!!
# 0 
print(0 and 3)
print(0 and 0)
```

```
5
0
0
0
```

```python
# or : 둘 중 하나만 True면 True
# 첫번째 3 True이니까 무조건 True!
# 3
print(3 or 5)
print(3 or 0)
# 첫번째 False, 하나만 True여도 True니까 다음 것도 봐야함.
# 3
print(0 or 3)
print(0 or 0)
```

```
3
3
3
0
```



- 산술연산자

  - ```python
    quotient, remainder = divmod(5, 2)
    print(f'몫은 {quotient}, 나머지는 {remainder}') # => 몫은 2, 나머지는 1
    ```

- id ( 파이썬에서 -5부터 256까지의 id는 동일)

  - ```python
    a = []
    b = []
    # 값을 비교하면, 빈 리스트라서 같은데
    # is를 통해서 object, 다름
    print(a == b, a is b) # => True False
    print(id(a), id(b)) # => 2151734416448 2151733434688
    ```

  - ```python
    # 공백없는 알파벳 문자열도 같게끔 해놨다.
    a = 'hi'
    b = 'hi'
    print(a is b) # => True # => 2151694017328 2151694017328
    print(id(a), id(b))
    
    # 느낌표때문에 다름
    a = 'hi!'
    b = 'hi!'
    a is b # => False
    ```

  - 

- 

  

