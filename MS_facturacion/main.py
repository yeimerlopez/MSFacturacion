from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCliente import ControladorCliente
from Controladores.ControladorFactura import ControladorFactura
from Controladores.ControladorProducto import ControladorProducto
from Controladores.ControladorVenta import ControladorVenta


#print("Mobile planet")

app = Flask(__name__)
cors = CORS(app)

# En esta linea estoy instanciando el controlador de cliente
miControladorCliente = ControladorCliente()
miControladorFactura = ControladorFactura()
miControladorProducto = ControladorProducto()
miControladorVenta = ControladorVenta()


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["massage"] = "Server Running ..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data



 ######################################Servicios Facturas############################################
#listar todos las factura
@app.route("/facturas",methods=['GET'])
def getFacturas():
    json = miControladorFactura.index()
    return jsonify(json)

#listar factura por id
@app.route("/facturas/<string:id>",methods=['GET'])
def getFactura(id):
    json = miControladorFactura.show(id)
    return jsonify(json)

#Crear factura
@app.route("/facturas",methods=['POST'])
def createFactura():
    data = request.get_json()
    json = miControladorFactura.create(data)
    return jsonify(json)

#Actualiza una factura
@app.route("/facturas/<string:id>",methods=['PUT'])
def modificarFactura(id):
    data = request.get_json()
    json = miControladorFactura.update(id,data)
    return jsonify(json)

#Elimina una factura
@app.route("/facturas/<string:id>",methods=['DELETE'])
def eliminarFactura(id):
    json = miControladorFactura.delete(id)
    return jsonify(json)
 #####################################################################################################


 ######################################Servicios Clientes############################################
#listar todos los clientes
@app.route("/clientes",methods=['GET'])
def getClientes():
    json = miControladorCliente.index()
    return jsonify(json)

#listar cliente por id
@app.route("/clientes/<string:id>",methods=['GET'])
def getCliente(id):
    json = miControladorCliente.show(id)
    return jsonify(json)

#Crear cliente
@app.route("/clientes",methods=['POST'])
def createCliente():
    data = request.get_json()
    json = miControladorCliente.create(data)
    return jsonify(json)

#Actualiza un cliente
@app.route("/clientes/<string:id>",methods=['PUT'])
def modificarCliente(id):
    data = request.get_json()
    json = miControladorCliente.update(id,data)
    return jsonify(json)

#Elimina un estudiante
@app.route("/clientes/<string:id>",methods=['DELETE'])
def eliminarCliente(id):
    json = miControladorCliente.delete(id)
    return jsonify(json)
###################################################################################################



 ######################################Servicios Productos#########################################
#listar todos los productos
@app.route("/productos",methods=['GET'])
def getProductos():
    json = miControladorProducto.index()
    return jsonify(json)

#listar producto por id
@app.route("/productos/<string:id>",methods=['GET'])
def getProducto(id):
    json = miControladorProducto.show(id)
    return jsonify(json)

#Crear producto
@app.route("/productos",methods=['POST'])
def createProducto():
    data = request.get_json()
    json = miControladorProducto.create(data)
    return jsonify(json)

#Actualizar un producto
@app.route("/productos/<string:id>",methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json = miControladorProducto.update(id,data)
    return jsonify(json)

#Elimina un producto
@app.route("/productos/<string:id>",methods=['DELETE'])
def eliminarProducto(id):
    json = miControladorProducto.delete(id)
    return jsonify(json)

"""
# A. asignar un cliente a producto  (departamento a materia )(partido a candidato)
@app.route("/candidatos/<string:id>/partidos/<string:id_partido>",methods=['PUT'])
def asignarClienteAProducto(id,id_cliente):
    json = miControladorProducto.asignarCliente(id,id_cliente)
    return jsonify(json)
"""







 ##################################################################################################
 ######################################Servicios Ventas ###########################################
#listar todos las ventas
@app.route("/ventas",methods=['GET'])
def getVentas():
    json = miControladorVenta.index()
    return jsonify(json)

#listar venta por id
@app.route("/ventas/<string:id>",methods=['GET'])
def getVenta(id):
    json = miControladorVenta.show(id)
    return jsonify(json)


@app.route("/ventas/factura/<string:id_factura>/producto/<string:id_producto>",methods=['POST'])
def crearVentas(id_factura,id_producto):
    data = request.get_json()
    json = miControladorVenta.create(data,id_factura,id_producto)
    return jsonify(json)

#Actualiza una venta
@app.route("/ventas/<string:id_venta>/factura/<string:id_factura>/producto/<string:id_producto>",methods=['PUT'])
def modificarVenta(id_venta, id_factura, id_producto):
    data = request.get_json()
    json = miControladorVenta.update(id_venta, data, id_factura, id_producto)
    return jsonify(json)

#Elimina una Venta
@app.route("/ventas/<string:id>",methods=['DELETE'])
def eliminarVenta(id):
    json = miControladorVenta.delete(id)
    return jsonify(json)

@app.route("/ventas/producto/<string:id_producto>",methods=['GET'])
def inscritosEnMateria(id_producto):
    json = miControladorVenta.ListarInscritosEnMateria(id_producto)
    return jsonify(json)



###################################################################################################










#función para leer el archivo de configuración

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

