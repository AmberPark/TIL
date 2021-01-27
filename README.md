# Today I Learned

## git 사용하기

*2021.01.26*

1. 일단 가장 기본적으로 git에 push 할 때 , push 할 폴더에서 git bash 열어서

```
$ git add .
$ git commit -m '쓰고싶은말'
$ git push origin master
```

2. 조금 더 깊이 들어가서

```
$ git branch branch-name => 새로운 branch 생성
$ git switch(or checkout) branch-name => 전환
$ git switch -c branch-name => 새로운 branch 생성과 함께 전환
$ git branch -d branch-name => branch delete
$ git branch -D branch-name => 강제로 delete
$ git merge branch-name => branch 병합. ex)master과 home-page를 같은것으로 만들겠다.
```



## OOP

*2021.01.27*

- Object(객체) : 파이썬에서 모든 것은 객체. 모든 객체는 type, attribute, method를 가짐.

  - instance : type 의 instance(예시)

  - ```python
    a = 10
    type(a) # => int. a 는 int 타입의 인스턴스.
    ```

  - Attribute(속성) ( `객체.속성` )

  - ```python
    complex_number = 3+4j
    complex_number.real # => .real => 실수부를 구하는 속성
    complex_number.imag # => .imag => 허수부를 구하는 속성
    ```

  - Method(메서드)( `객체.조작법()` )

  - ```python
    a = [3, 2, 1]
    a.sort()
    
    # list타입의 객체들이 할 수 있는 모든 속성과 메서드를 보는 방법
    print(dir(a))
    # complex타입 객체들이 할 수 있는 모든것 보는 방법 
    print(dir(3+4j)) # 예시
    ```






- 객체 지향 프로그래밍(Object Oriented Programming)
  - Class 생성
  - instance 생성
  - method 정의

  

  

## python

##### 1. Intro

- 식별자  : 프로그래밍 언어에서 이름을 붙일 때 사용하는 단어. 주로 변수 또는 함수 이름 등으로 사용.
  - 키워드 사용 x. `print(keyword.kwlist)` 로 출력하면 파이썬의 키워드 나옴
  - 특수문자는 언더바(_)만 허용
  - 숫자로 시작하면 안됨
  - 공백 포함 x
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
# and : 둘다 True여야 True..
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
# 첫번째 3 True, 빼박... True!
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



- id ( 파이썬에서 -5부터 256까지의 id는 동일)

  - ```python
    # 느낌표때문에 같지 않다..
    a = 'hi!'
    b = 'hi!'
    a is b # => False
    ```

  - ```python
    # object interning..
    # 의도적으로.. 공백없는 알파벳 문자열도 같게끔 해놨다.
    a = 'hi'
    b = 'hi'
    print(a is b) # => True
    print(id(a), id(b)) # => same
    ```





#####  2. Container

- Sequence형(ordered data)

  - list
  - tuple
  - range
  - string

  





- Non-sequence형(unordered data)