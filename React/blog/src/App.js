/*eslint-disable*/
import React, { useState } from 'react'
import './App.css';

function App() {
  const [title, change] = useState(['여자가방추천', '여자 백팩 추천', '남자 향수 추천'])
  const [like, likechange] = useState(0)
  //useState('여자가방추천') // 얘는 실행하고 나면 array가 나옴
  function changeTitle(){
    const newArray = [...title]
    newArray[0] = '남자가방추천'
    change( newArray )
  }
  return (
    <div className="App">
      <div className="black-nav">
        <div>개발 Blog</div>
      </div>
      <button onClick={changeTitle}>button</button>
      <div className="list">
        <h4>{ title[0] } <span onClick={() => {likechange(like+1)}}>❤</span>{like}</h4>
        <p>7월 22일 발행</p>
        <hr/><h4>{ title[1] }</h4>
        <p>7월 22일 발행</p>
        <hr/><h4>{ title[2] }</h4>
        <p>7월 22일 발행</p>
        <hr/>
      </div>  

      <div>
        <h2>제목</h2>
        <p></p>
      </div>
    </div>
  );
}

export default App;
