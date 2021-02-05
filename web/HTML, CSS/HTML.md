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

#### - Element(요소)

- 요소는 시작태그, 태그사이 위치한 content, 종료태그로 구성된다. 딱히 대소문자 구분은 없지만 소문자 사용이 일반적.

#### - Empty Element(빈요소)

- content가 필요 없다. Attribute만 가질 수 있다.
- 대표적으로 br, hr, imag, imput, link, meta 가 있다.

#### - Attribute

- 요소의 성질을 정의하는 것이다. 요소에 추가적 정보를 제공한다. 
- 시작 태그에 위치해야 하며 이름과 값의 쌍을 이룬다. ex) `<img src="html.png"></img>` 에서 src는 attribute 이름, ""안의 것은 attribute 값.

#### - Global Attribute

- 모든 HTML요소가 공통으로 사용할 수 있는 어트리뷰트. 
  - id : 유일한 식별자(id)를 요소에 지정. *중복 지정이 불가*
  - class : 스타일 시트에 정의된 class를 요소에 지정. *중복지정 가능*
  - hidden : css의 hidden과는 다르게 의미상으로도 브라우저에 노출되지 않도록 함
  - lang : 언어 지정. 
  - style : 요소에 Inline style을 지정.
  - tabindex : 사용자가 키보드로 페이지를 네비게이션 시 이동 순서를 지정.
  - title : 제목 지정

#### - 주석

- 주석은 `<!--이것은 주석입니다-->` 이렇게 작성



### 3. 시맨틱 웹(Semantic Web)



