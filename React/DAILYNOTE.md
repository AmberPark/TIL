# React:happy:

## 2021.07.12~2021.07.15

### 인프런_노드리액트기초강좌

#### - ERRORS:anger:

- `[HPM] Error occurred while proxying request localhost:3000/api/users/login to http://localhost:5000/ [ECONNREFUSED] (https://nodejs.org/api/errors.html#errors_common_system_errors)` 로그인하는데 자꾸 이에러가 뜬다... 프록시에러같은데 뭘까? setupProxy.js에 target 을 5000으로 해두고
  - 해결! package.json에 	`"backend" : "nodemon server/index.js",` 여기서 `server/`을 안적어서 백엔드쪽에 에러가 나서 그런것이었다. 
- withRouter로 감싸줬는데도 빈화면만 나와서 뭘까 했는데 auth.js에 `SpecificComponent` 앞에 s를 소문자로 해서 에러가 난 것이었다.



## 2021.07.15

### 리액트 공식문서로 자습_틱택토

