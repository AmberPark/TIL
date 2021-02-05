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

  

  