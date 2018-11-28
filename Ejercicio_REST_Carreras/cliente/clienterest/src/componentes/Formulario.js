import React, { Component } from 'react';
import { Button, Card, Form, Input, TextArea } from "semantic-ui-react";


class Formulario extends Component {
  datos = ["", ""]
  
  campoListener = (event, data, numeroDato) => {
    this.datos[numeroDato] = data.value;    
  }

  agregar = (event) => {
    event.preventDefault();
    const carrera = {
      'nombre': this.datos[0],
      'descripcion': this.datos[1]
    }

    this.props.agregarCarrera(carrera);
  }

	render() {
		return (
			<Card color="purple" style={{"padding": "2%"}}>
				<Form onSubmit={this.agregar}>
  				<Form.Field        			
          			control={Input}
          			label='Nombre de Carrera'
          			placeholder='Nombre'
                onChange={(event, data) => this.campoListener(event, data, 0)}
        			/>
          <Form.Field        
            control={TextArea}
            label='Descripción'
            placeholder='Descripción'
            onChange={(event, data) => this.campoListener(event, data, 1)}
          />

          <Button>Agregar</Button>
				</Form>
			</Card>
		);
	}
}

export default Formulario;