import React, { Component } from 'react';
import { Button, Table } from 'semantic-ui-react'

class Tabla extends Component {
	render() {
		const datosCarrera = this.props.datos;
    const filas = []

    datosCarrera.forEach( (element) => {
      filas.push(
      <Table.Row key={element[0]}>
        <Table.Cell>{element[0]}</Table.Cell>

        <Table.Cell>{element[1]}</Table.Cell>
        
        <Table.Cell textAlign='right'>{element[2]}</Table.Cell>
        <Table.Cell collapsing textAlign='center'>
          <Button basic color="red" onClick={() => this.props.actionEliminar(element[0])}>Eliminar</Button>
        </Table.Cell>
      </Table.Row>
      );
    });

		return (
			<Table celled striped color="red">
				<Table.Header>
			      <Table.Row>
			        <Table.HeaderCell colSpan='4'>Carreras</Table.HeaderCell>
			      </Table.Row>
			    </Table.Header>

			    <Table.Body>
          {filas}
			    </Table.Body>
			</Table>
		);
	}
}

export default Tabla;