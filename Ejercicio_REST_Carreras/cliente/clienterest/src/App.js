import React, { Component } from 'react';
import axios from "axios";

import Formulario from "./componentes/Formulario";
import Tabla from "./componentes/Tabla";

class App extends Component {
  state = {
    carreras: []
  }

  componentDidMount() {
  	const url = "http://192.168.0.12:5000/carreras/"
  	axios.get(url).then(response => {
    		this.setState({carreras: response.data.carreras});
 	  }).catch(function (error) {
    	console.log(error);
  	});
  }

  agregarCarrera = carrera => {
    const url = "http://192.168.0.12:5000/carrera/1"

    axios.post(url, {
      nombre: carrera.nombre, descripcion: carrera.descripcion
    }).then(response => {
        console.log(response);
    }).catch(function (error) {
      console.log(error);
    });
    
  }

  render() {
    return (
      <div className="App">
        <center>
          <Formulario agregarCarrera={this.agregarCarrera}/>
          <Tabla datos={this.state.carreras}/>
        </center>
      </div>
    );
  }
}

export default App;
