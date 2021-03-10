

![image-20210310200248442](model.assets/image-20210310200248442.png)

# CREAT

- creat 하는 세가지 방법. (shell_plus 터미널에서)

![image-20210310155800150](model.assets/image-20210310155800150.png)

# READ

## 1. all()

## 2. get()

- 객체가 없으면 DoesNotExist 에러 발생
- 객체가 여러개면 MultipleObjectsReturned 에러 발생
- 위와 같은 특징을 갖고 있기 때문에 unique 혹은 NOT NULL 특징을 가지고 있는 경우에만 사용 가능( pk)

![image-20210310143951578](model.assets/image-20210310143951578.png)

## 3. filter()

![image-20210310143748496](model.assets/image-20210310143748496.png)





# admin

![image-20210310150719519](model.assets/image-20210310150719519.png)

- admin 에 만든 클래스 넣고(어드민 사이트에 내가만든 클래스 register) superuser하면 어드민 사이트에서 데이터 수정 쉽게 가능.
- ![image-20210310151944298](model.assets/image-20210310151944298.png)



- 어드민 사이트 에서 보일 디스플레이 설정

![image-20210310151915025](model.assets/image-20210310151915025.png)