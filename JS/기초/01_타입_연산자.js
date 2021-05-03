/*
  Primitive Types
  1. Number

  2. String

  3. Empty

  4. Boolean
*/

// number type
console.log(
  1, -1, 3.14, 2.998e3,
  Infinity, 10/0,
  Nan, // 숫자아님
)


// string type
console.log(
  'hello', "world", 'ssafy' + '5th',
  `` // f''와 같은 거
  `1 + 1 = ${1 + 1}` // Template Literal.
)

//empty
console.log(
  undefined, null // undefined, null => 의도의 차이
)


// Boolean
console.log(
  true, false
)


/*
  연산자
  Operands
  1. unary (단항 연산자)
  - (음수/양수), typeof (-, typeof), ++, --, !
  2. binary (이항 연산자)
  +, -, *, /, +=, -= , <, >, <=, >=. *=, /=, &&, ||
  3. ternary (삼항 연산자)
  ? , :


  1. 산술연산자
  2. 수, 비교연산자
  3. (비교)동등연산자
  4. 논리연산자

*/

console.log(
  'Unary Operator',
  -1, typeof 1
)

let i = 1
console.log(i++) // i에 대한 평가가 끝난 후 1을 더한다.
console.log(++i) // i에 대한 평가가 끝나기 전에 1을 더한다

// ! => not 과 같다

// 동등 ==  => 안씀

// 일치 ===  => 이것만 씀


// and => &&, or => ||
console.log(true && true && false)
console.log(false || true || true)

// 가치평가 ? true일 경우 : false 일 경우
console.log(1 > 2 ? '크다' : '작다') // => 작다
