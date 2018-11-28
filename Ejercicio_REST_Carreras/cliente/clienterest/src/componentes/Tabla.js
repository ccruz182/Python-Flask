import React, { Component } from 'react';
import { Table } from 'semantic-ui-react'

class Tabla extends Component {
	render() {
		const datosCarrera = this.props.datos;
    const filas = []

    datosCarrera.forEach( (element) => {
      filas.push(
      <Table.Row>
        <Table.Cell>
          {element[0]}
        </Table.Cell>
        <Table.Cell>{element[1]}</Table.Cell>
        <Table.Cell textAlign='right'>
          {element[2]}
        </Table.Cell>
      </Table.Row>
      );
    });
		return (
			<Table celled striped>
				<Table.Header>
			      <Table.Row>
			        <Table.HeaderCell colSpan='3'>Carreras</Table.HeaderCell>
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