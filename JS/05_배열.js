/*
  JS의 배열 (Array)
  1. 리스트로 구현되어 있음(크기제한 없음)
  2. 음수 인덱싱, 슬라이싱 불가능
*/

const numbers = [1, 2, 3, 4]
numbers[0] // 가능
numbers[-1] // 불가능
// number[:] // 슬라이싱 불가능

numbers.length // 길이


// .reverse() => 원본 파괴
numbers.reverse() // 

numbers = [1, 2, 3, 4]

// .push()
numbers.push('a')   // 5 : numbers.length 를 return
numbers             // [1, 2, 3, 4, 'a']

// .pop()
numbers.pop()   // 'a' : pop 한 결과
numbers         // [1, 2, 3, 4]

// .unshift()
numbers.unshift('a')   // 5 : numbers.length 를 return
numbers                // ['a', 1, 2, 3, 4]

// .shift()
numbers.shift()   // 'a'  : shift(dequeue)한 결과
numbers           // [1, 2, 3, 4]

// .includes()
numbers.includes(4)  // true
numbers              // 변화 없음

// .indexOf()
numbers.indexOf(2)     // 1 : 찾은 요소의 첫번째 idx 반환
numbers.indexOf(1234)  // -1 : 없는 경우 -1 반환
numbers                // 변화 없음

// .join()
numbers.join('-')     // '1-2-3-4'
numbers               // 변화 없음
