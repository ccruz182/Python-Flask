from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import mysql.connector

INSERT_SQL = "INSERT INTO Carrera(nombreCarrera, descripcionCarrera) VALUES (%s, %s)"
SELECT_ALL_SQL = "SELECT * FROM Carrera"
SELECT_ONE_SQL = "SELECT * FROM Carrera WHERE idCarrera = "
DELETE_SQL = "DELETE FROM Carrera WHERE idCarrera = "

app = Flask(__name__)
api = Api(app) # Allows to add Resources
bd = mysql.connector.connect(host='localhost', user='root', passwd='root', database='CarreraPy')
bd_cursor = bd.cursor()


class Carrera(Resource):
	def get(self, ide):		
		bd_cursor.execute(SELECT_ONE_SQL + str(ide))
		elemento = bd_cursor.fetchone()
		if elemento:
			return {"carrera": elemento}, 200
		else:
			return {"error": "No hay registro"}, 400

	def post(self, ide):
		datos = request.get_json()
		nueva_carrera = (datos['nombre'], datos['descripcion'])
		bd_cursor.execute(INSERT_SQL, nueva_carrera)
		bd.commit()
		return {"mensaje": "Todo bien"}, 200

	def delete(self, ide):
		bd_cursor.execute(DELETE_SQL + str(ide))
		bd.commit()
		return {"mensaje": "Todo bien"}, 200

class Carreras(Resource):
	def get(self):
		bd_cursor.execute(SELECT_ALL_SQL)
		elementos = bd_cursor.fetchall()
		if elementos:
			return {"carreras": elementos}, 200
		else:
			return {"error": "No hay registros"}, 400

api.add_resource(Carrera, '/carrera/<string:ide>')
api.add_resource(Carreras, '/carreras/')
app.run(host="0.0.0.0", port=5000, debug=True)