# Algorithm

내장함수 쓰지 않아보기

## 문자열을 정수로 바꾸는 함수(int()구현)

```python
def atoi(num_str):
    value = 0

    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')
    return value

num_str = '1234'
num_int = atoi(num_str)
print(num_int, type(num_int))
```



## 정수를 문자열로 바꾸는 함수(str()구현)

```python
def itoa(num_int):
    strings = ''
    while num_int > 0:
        string = chr(num_int % 10 + 48) 
        strings += string # 나머지를 하나씩 빈 문자열에 넣기 (즉, 일의자리 숫자, 십의자리 숫자,, 순서로 넣게됨) 
        num_int //= 10 # 이제 몫으로 다음 숫자 하나씩 떼어오게 되니까. 
    return strings


a = itoa(123456)
b = itoa(6410)
print(a, type(a))
print(b, type(b))
```

