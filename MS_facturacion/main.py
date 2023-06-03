from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCliente import ControladorCliente


#print("Mobile planet")

app = Flask(__name__)
cors = CORS(app)

# En esta linea estoy instanciando el controlador de cliente
miControladorCliente = ControladorCliente()


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["massage"] = "Server Running ..."
    return jsonify(json)

 ######################################Servicios Clientes####################################################
# 1.listar todas los clientes
@app.route("/clientes",methods=['GET'])
def getClientes():
    json = miControladorCliente.index()
    return jsonify(json)



#listar cliente por id
@app.route("/clientes/<string:id>",methods=['GET'])
def getCliente(id):
    json = miControladorCliente.show(id)
    return jsonify(json)

#Crear
@app.route("/clientes",methods=['POST'])
def createCliente():
    data = request.get_json()
    json = miControladorCliente.create(data)
    return jsonify(json)

#Actualiza



#función para leer el archivo de configuración
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

