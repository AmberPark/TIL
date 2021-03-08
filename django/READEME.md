# 가상환경 파이썬 만들기

- 먼저 파일 만들고 거기서 
- `python -m venv venv`
- `ls`로 확인하고 `which python`으로 다시 확인
- `source venv/Scripts/activate` 로 활성화
- 이제 (venv)라고 뜸
- deactivate 하면 venv 없어짐
- 설치할 것들에 내용 자동으로 설치하는 것은 `pip install -r requirements.txt`



# Django project 마스터 파일 생성

- `django-admin startproject firstpjt(파일명)`

# app들 생성

- `python manage.py startapp articles(파일명)`

# 서버 켜기

- `python manage.py runserver`

