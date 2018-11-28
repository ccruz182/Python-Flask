import React, { Component } from 'react';
import axios from "axios";
import { Message } from "semantic-ui-react";

import Formulario from "./componentes/Formulario";
import Tabla from "./componentes/Tabla";

class App extends Component {
  state = {
    carreras: [],
    exitoso: false    
  }

  mensaje = ""

  componentDidMount() {
  	this.obtenerCarreras();
  }

  agregarCarrera = carrera => {
    const url = "http://localhost:5000/carrera/1"

    axios.post(url, {
      nombre: carrera.nombre, descripcion: carrera.descripcion
    }).then(response => {
        console.log(response);
        this.obtenerCarreras();
        this.mostrarMensajeExitoso("Se añadió correctamente la carrera");        
    }).catch(function (error) {
      console.log(error);
    });    
  }

  eliminarCarrera = idCarrera => {
    const url = "http://localhost:5000/carrera/" + idCarrera;
    axios.delete(url).then(response => {
        console.log(response);
        this.obtenerCarreras();
        this.mostrarMensajeExitoso("Se eliminó correctamente la carrera");
    }).catch(function (error) {
      console.log(error);
    });    
  }

  obtenerCarreras = () => {
    const url = "http://localhost:5000/carreras/"
    axios.get(url).then(response => {
        this.setState({carreras: response.data.carreras});
    }).catch(function (error) {
      console.log(error);
    });
  }

  mostrarMensajeExitoso = mensaje => {
    this.setState({exitoso: true});
    this.mensaje = mensaje;

    setTimeout(() => {
      this.setState({exitoso: false});
    }, 2000);
  }

  render() {
    let mensaje = null;
    if (this.state.exitoso) {
      mensaje = <Message positive><b>{this.mensaje}</b></Message>
    } else {
      mensaje = null;
    }

    return (
      <div className="App">
        <center>
          <Formulario agregarCarrera={this.agregarCarrera}/>
          {mensaje}
          <Tabla datos={this.state.carreras} actionEliminar={this.eliminarCarrera}/>
        </center>
      </div>
    );
  }
}

export default App;
