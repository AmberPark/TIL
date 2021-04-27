# Django 끝자락

## REST API

- 모든 URL 은 URI 이다 -> true

- 모든 URI는 URL이다 -> False

- URI 설계시 주의사항
  - _ 아닌 -(하이폰) 사용 -> 가독성
  - 소문자 사용 -> 대소문자에 따라 다른 자원으로 인식하게 됨
  - 파일 확장자는 포함 x
  
- HTTP Method 종류
  - GET - 특정 자원의 표시 요청, 오직 데이터를 받기만 함
  - POST - 서버로 데이터를 전송, 서버에 변경사항을 만듦
  - PUT - 요청한 주소의 자원을 수정
  - DELETE - 지정한 자원을 삭제

- `GET/articles/1/read/` (x), URI에 불필요한 정보(행위표현)가 포함 -> `GET/articles/1/` (o) 

- `GET/articles/1/delete/` (x),  URI는 자원에 대한 행위는 HTTP method로 표현 -> `DELETE/articles/1/` (o)

  

### 실습

- django-seed 로 더미데이터 만들기
  - pip install django-seed 하고 , settings에 installed app 에 추가하고 , 20 개 넣겠다 -> 아래처럼.
  - ![image-20210426101558519](TIL.assets/image-20210426101558519.png)

- rest_framwork 하면
- ![image-20210426105718768](TIL.assets/image-20210426105718768.png)

![image-20210426105735081](TIL.assets/image-20210426105735081.png)

- 아래처럼 json이 템플릿 형태로 나옴
- ![image-20210426105813087](TIL.assets/image-20210426105813087.png)





- create
  - 위에 `from rest_framework import status`하고 
  
  - ![image-20210427105244017](TIL.assets/image-20210427105244017.png)
  
  - 하면
  
  - ![image-20210427105339426](TIL.assets/image-20210427105339426.png)
  
    이런식으로 나옴