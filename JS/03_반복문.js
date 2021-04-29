let i = 0
while (i < 10) {
  console.log('hi')
  i++

}

//전통적인 for
for (let i=0; i<5; i++) {
  console.log('hi')
}

const arr = [1,2,3,4,5]
for (let number of arr) {
  console.log(number)
}

const numbers = [1,2,3,4,5]
// array 요소를 꺼내는 for - of
for (const number of numbers) {
  console.log(number)
}

const person = {name: 'new', 'address':'seoul'}
// object => key 를 꺼내는 for - in
for (const key in person) {
  console.log(key) // => 키 값만 뽑혀 나옴
}
// 키에 작은 따옴표 있든 없든 person.name, person.address 벨류값은 잘 나옴.