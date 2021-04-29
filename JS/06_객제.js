/*
  python dict와 다른점
  1. key 문자열의 따옴표 삭제 가능(띄어쓰기 없을 때)
  2. 접근할 때, ['key']와 .key 모두 가능
  3. 함수 정의 시작
*/

const me = {
  name: '홍길동',
  //'phone number': '0123456786' // => 가능하지만 key도 변수명처럼 지을 것
  phoneNumber: '0123456789',
  friends: [
    '도우너','akdlzhf', '또치'

  ],
  home: {
    address: '서울',
    owner: '고길동',
  }

}



// ES6+ 
// new
const dooly = {
  name: 'dooly',
  // Arrow
  greeting1: () => console.log('도우너'),
  // Function 키워드 대체용
  greeting2 () {
    console.log('어서오고')
  }

}

// 3. (minor) computed property name


// 4. Object Destructuring (비구조화)
const userInfo = {
  name: '김싸피',
  eamil: 'kim@ssafy.com',
  phone: '0123456789',

}

// const { name } = userInfo
// const { eamil } = userInfo
// const { phone } = userInfo

const { name, email, phone } = userInfo
