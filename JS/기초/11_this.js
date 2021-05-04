/*
  this 는 아래의 경우를 제외하고 모두 최상위 객체(window)를 가르킴.
  1. constructor 함수 내부에서 => 생성될 객체를 가르킨다.
  2. class 정의 내부의 메서드 정의
*/

const neo = {
  name: '유태영',
  greeting: function () {
    return `hello ${this.name}입니다.`

  }
}

const neo = {
  lastName: '유',
  firstName: '태영',
  greeting: function () {
    return `hello ${this.lastName + this.firstName}입니다.`

  }
}