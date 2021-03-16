- POST method 를 쓰면 views 에서 `if request.method == 'POST':` 쓰고 GET을 다 POST로 바꿔주기 

- ![image-20210311132536554](model.assets/image-20210311132536554.png)

  ![image-20210311132605107](model.assets/image-20210311132605107.png)





- html에서 form 안에 `method='POST'` 하고 밑에 `{% csrf_token %}` 꼭 적기! 안그러면 forbidden 페이지 뜸. 

- ![image-20210311132631895](model.assets/image-20210311132631895.png)

  ![image-20210311132844899](model.assets/image-20210311132844899.png)

  ![image-20210311132902189](model.assets/image-20210311132902189.png)

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





# DELETE

shell_plus 에서 .delete() 하고 s = 0

![image-20210311094944691](model.assets/image-20210311094944691.png)



- 브라우저에서 delete 누르고 확인 창 뜨게하는거 : onclick="return confirm('message')"



# admin

![image-20210310150719519](model.assets/image-20210310150719519.png)

- admin 에 만든 클래스 넣고(어드민 사이트에 내가만든 클래스 register) superuser하면 어드민 사이트에서 데이터 수정 쉽게 가능.
- ![image-20210310151944298](model.assets/image-20210310151944298.png)



- 어드민 사이트 에서 보일 디스플레이 설정

![image-20210310151915025](model.assets/image-20210310151915025.png)





# 데이터 다 날리고 처음부터 하고싶을 때

- db 날리고, migrations 안에 생긴 initial.py들도 지워주기.
- ![image-20210316095712826](model.assets/image-20210316095712826.png)

- 다시 처음부터 makemigrations, migrate 하기