// import logo from './logo.svg';
import React, {Component} from 'react';
import './App.css';

class Subject extends Component {
  render() {
    return (
      <header>
      <h1>Web</h1>
      World Wide web!
    </header>
    )
 
  }
}

class App extends Component {
  render() {
    return (
      
      <div className="App">
        <Subject></Subject>
        Hello, React!!
      </div>
    )
  }
}



export default App;
