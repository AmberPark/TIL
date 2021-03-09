# 가상환경 파이썬 만들기

- 먼저 파일 만들고 거기서 
- `python -m venv venv`
- `ls`로 확인하고 `which python`으로 다시 확인
- `source venv/Scripts/activate` 로 활성화 (or VS code 로 열기)
- 이제 (venv)라고 뜸
- deactivate 하면 venv 없어짐
- 설치할 것들에 내용 자동으로 설치하는 것은 `pip install -r requirements.txt`



# django 프로젝트 만드는 순서

1. 빈폴더(프로젝트 루트)를 만든다
   1. `.gitignore` 생성
   2. `$ git init` 으로 리포 초기화
   3. `README.md` 생성
   4. 원격 저장소 생성 후 연결
   5. add => commit => push
2. 해당폴더로 이동해서 `$ python -m venv venv` 명령어를 통해 가상독립환경 폴더를 만든다.
3. 가상 동립환경을 활성화`$ source venv/Scripts/activate`한다.
4. `$ pip install django` 를 통해 필요한 패키지들을 설치한다
5. `$ django-admin startproject (프로젝트이름)` 명령어를 통해 프로젝트 초기화
6. 프로젝트 진행



## 프로젝트 열기

반드시 프로젝트 루트 폴더는 대문자로!



## 프로젝트 독립환경 설저

1. `ctrl` + `shift` + `p`

2. python: select interpreter 치고 
3. venv/ 안의 파이썬 선택. 못잡으면
4. enter interpreter path => find => venv/scripts/python 선택
5. 완료 이후 왼쪽 하단에 python venv 확인
6. 터미널창 켜면 (venv) 자동으로 잡아주는거 확인 후 진행



> 장고는 html을 찾을때 templates 안에서 찾음.



### Django project 마스터 파일 생성

- `django-admin startproject firstpjt(파일명)`

### app들 생성

- `python manage.py startapp articles(파일명)`

### 서버 켜기

- `python manage.py runserver`

