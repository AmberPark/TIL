# HTML(HyperText Markup Language)

### 1. 개요

- HTML은 웹 페이지를 기술하기 위한 마크업 언어. 웹페이지의 내용과 구조를 담당하는 언어로 HTML tag를 통해 정보를 구조화 한다. 

- 반드시 `<!DOCTYPE html>`로 시작.

- 웹브라우저에 출력되는 모든 요소는 `<body>`와 `</body>` 사이에 위치

- ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <h1>This is Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>
  
    <p>본문</p>
    <ol>
      <li>Ordered List</li>
      <li>순서가 있는 list</li>
    </ol>
      
    <ul>
      <li>Unordered List</li>
      <li>순서가 없는 list</li>
      <li>md: - </li>
    </ul>
    <br> <!--한줄띄우기-->
    <form action="">
      <div>
        <input type="text">
      </div>
      <div>
        <input type="submit">
      </div>
    </form>
  
    <div></div><!--의미없이 구분하는 거-->
    <section></section>
    <header></header>
    <article></article>
    <aside></aside>
    <footer></footer>
    <nav></nav>
    <h2>여기까지는 Block 요소들</h2>
    <hr>
    <h2>아래부터는 inline 요소들</h2>
    <a href="https://google.com">Google</a>구글은 검색엔진
    <br>
    시험 성적 확인은 <a href="https://edu.ssafy.com" target="_blank">이곳</a>에서
    <!--target="_blank"을 하면 새탭에서 열림-->
    <span></span>
  
    <b></b><!--그냥 굵게 보여주는거-->
    <strong>중요</strong> <!--중요한 내용을 강조-->
  
  </body>
  </html>
  ```



### 2. 기본문법

#### Element(요소)

- 요소는 시작태그, 태그사이 위치한 content, 종료태그로 구성된다. 딱히 대소문자 구분은 없지만 소문자 사용이 일반적.

#### Empty Element(빈요소)

- content가 필요 없다. Attribute만 가질 수 있다.
- 대표적으로 br, hr, imag, imput, link, meta 가 있다.

#### Attribute

- 요소의 성질을 정의하는 것이다. 요소에 추가적 정보를 제공한다. 
- 시작 태그에 위치해야 하며 이름과 값의 쌍을 이룬다. ex) `<img src="html.png"></img>` 에서 src는 attribute 이름, ""안의 것은 attribute 값.

#### Global Attribute

- 모든 HTML요소가 공통으로 사용할 수 있는 어트리뷰트. 
  - id : 유일한 식별자(id)를 요소에 지정. *중복 지정이 불가*
  - class : 스타일 시트에 정의된 class를 요소에 지정. *중복지정 가능*
  - hidden : css의 hidden과는 다르게 의미상으로도 브라우저에 노출되지 않도록 함
  - lang : 언어 지정. 
  - style : 요소에 Inline style을 지정.
  - tabindex : 사용자가 키보드로 페이지를 네비게이션 시 이동 순서를 지정.
  - title : 제목 지정

#### 주석

- 주석은 `<!--이것은 주석입니다-->` 이렇게 작성



### 3. 시맨틱 웹(Semantic Web)

#### 시맨틱 태그

- 검색 엔진에 보다 의미론적으로 문서 정보를 전달할 수 있고 검색 엔진 또한 시맨틱 요소를 이용해 보다 효과적인 크롤링과 인덱싱을 함. 즉 시맨틱 태그란 브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확하게 설명하는 역할을 함.
- HTML요소는 non-semantic 과 semantic요소로 구분할 수 있다. 
  - non-semantic element : div, span 등. content에 대해 어떤 설명도 하지 않음.
  - semantic element : form, table, img 등. content의 의미를 명확히 설명함. 
- HTML5에 새롭게 추가된 시맨틱 태그 : header, nav, aside, section, article, footer.



### 4. 태그

#### 기본 태그

- html : html 태그는 모든 HTML요소의 부모요소. 웹페이지에 단 하나만 존재.  
- head : 메타데이터를 포함하기 위한 요소. 웹페이지에 단 하나만 존재. 메타데이터 이외의 호면에 표시되는 일체의 요소를 포함시킬 수 없다. 
- title : 문서의 제목 정의. 브라우저 탭에 표시된다.
- style  : HTML 문서를 위gks style 정보를 정의.
- link : 외부 리소스와의 연계정보 정의. 
- script : client-side JavaScript 정의.
- meta : 브라우저, 검색엔진 등에 의해 사용. charset 어트리뷰트는 브라우저가 사용할 문자셋 정의.
- body : HTML문서의 내용 나타냄. 웹페이지에 단 하나만 존재함! 

#### 텍스트 관련 태그

- 제목 태그
    - heading : 주로 제목 나타낼 때 사용. h1에서 h6가지 있다. 시멘틱 웹의 의미를 살려 제목 이외에는 사용하지 않는 것이 좋음.
- 글자 형태 태그      
  
  
  - b : bold체를 지정. 의미론적(semantic) 중요성의 의미는 없음.
  - strong : bold 체 지정. 하지만 의미론적 중요성의 의미를 갖는다. 
    - i : Italic체 지정. 의미론적 중요성의 의미는 없다. 
    - em : Italic체로 표현. emphasized(강조, 중요한) text 지정.  의미론적 중요성의 의미 가짐.
    - mark : highlighted text 지정.
- 본문 태그
    - p : 단락 지정
    - br : 강제 개행 지정. 종료태그 없다.
    - pre : 형식화된 text 지정. pre태그 내의 content는 작성한 그대로 브라우저에 표시.
    - hr : 수평줄 삽입. 종료태그 없다.
    - q : 짧은 인용문 지정. 
    - blockquote : 긴 인용문 블록을 지정. 브라우저는 blockquote요소를 들여쓰기함.



### 5. Hyper link

- target attribute 
  - "_blank" : 새탭에서 열기

