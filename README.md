# git 사용하기

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

3. 

```
$ git remote add github https://github.com/AmberPark/learn_git.git => github으로 푸쉬할때
$ git push github master
```



## git 리포 만들때

1.  `$ touch .gitignore`만들기
2.  `$ git init`
3.  `$ touch .gitignore READ.md`
4.  `$ git add .` -> `$ git commit` 그 다음에
5.  `$ git remote add origin 주소`
6.  ` $ git push origin master` 

## 받아올때

두번째 페어는 

![image-20210312131419232](README.assets/image-20210312131419232.png)











1. `$ touch .gitignore`만들기 , vs code 들어가기

2. `$ git init`

3. python -m venv venv

4. source venv/Scripts/activete

5. pip install django django_extensions

6. pip freeze > requirements.txt (페어는 pip install -r requirements.txt 로 받아옴)

7. (`$ touch .gitignore READ.md` => 얘 1번에서 같이하기)

   

8. `$ git remote add origin 주소`(클론 눌러서 주소 복사한거)

9. git remote -v

10. `$ git add .` -> `$ git commit -m message` 

11. ` $ git push origin master` 