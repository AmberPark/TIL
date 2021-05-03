const arr = [1, 2, 3]

/* 
  array helper methods 의 생김새
  .forEach, .map, .filter

  arr.helperMethod(callbackFunction)
  arr.helperMethod(function () {})

*/
// .forEach() => return 되는 값 없음 === 콜백 함수에 return 필요 없음
// for - of 의 대체제 느낌
arr.forEach(function (num) {
  console.log(num)
})

// .map() => 콜백함수의 리턴값으로 만든 배열을 리턴
// arr.map(function (num) {
//   return num * 2
// })
arr.map(num => num * 2)
const contents = ['hello', 'world']
const tags = contents.map(function (content) {
  return `<h2>${content}</h2>`
})
tags.forEach(tag => document.write(tag))
contents.map(content => `<h2>${content}</h2>`).forEach(tag => document.write(tag))

// .find() =>콜백 함수의 리턴값이 true(혹은 true로 평가되는)
// 첫번째 요소만 리턴
arr.find(function (num) {
  return num === 2
})

arr.find(num => num === 2)

const articles = [
  {pk: 1, title: 'hi'},
  {pk: 2, title: 'hello'},
  {pk: 3, title: 'great'},
]

articles.find(article => article.pk === 3)




// .filter() => 콜백 함수의 리턴값이 true(혹은 true 로 평가되는)
// 요소만 모아서 배열로 리턴
arr.filter(num => num % 2)

// 사용 예시
const movies = [
  {title: 'matrix', isAdult: false},
  {title: 'kingsman', isAdult: true},
]

const adultMovies = movies.filter(function (movie) {
  return movie.isAdult
})

const adultMovies = movies.filter(movie => movie.isAdult)
// .reduce()