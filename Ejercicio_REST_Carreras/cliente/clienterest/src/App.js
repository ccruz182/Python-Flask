import React, { Component } from 'react';
import axios from "axios";

class App extends Component {
  componentDidMount() {
  	const url = "http://192.168.0.12:5000/carreras/"
  	axios.get(url)
  		.then(function (response) {
    		console.log(response);
 	}).catch(function (error) {
    	console.log(error);
  	});
  }

  render() {
    return (
      <div className="App">
        ok
      </div>
    );
  }
}

export default App;
