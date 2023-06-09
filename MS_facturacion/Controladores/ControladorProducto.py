from Repositorios.repositorioProducto import RepositorioProducto
from Repositorios.repositorioCliente import RepositorioCliente
from Modelos.Producto import Producto
from Modelos.Cliente import Cliente


class ControladorProducto():
    def __init__(self):
        print("creando controlador producto")
        self.repositorioProducto = RepositorioProducto()
        self.repositorioCliente = RepositorioCliente()

    def index(self):
        print("listar todos los productos")
        return self.repositorioProducto.findAll()

    def create(self, elProducto):
        print("Crear un producto")
        nuevoProducto = Producto(elProducto)
        return self.repositorioProducto.save(nuevoProducto)

    def show(self, id):
        print("Mostrando un Producto con id", id)
        elProducto = Producto(self.repositorioProducto.findById(id))
        return elProducto.__dict__


    def update(self, id , elproducto):
        print(" Actualizando un producto con id", id)

        productoActual = Producto(self.repositorioProducto.findById(id))
        #productoActual.nombre = elproducto["nombre"]
        productoActual.descripcion = elproducto["descripcion"]
        productoActual.precio = elproducto["precio"]
        return self.repositorioProducto.save(productoActual)


    def delete(self, id):
        print("Eliminando el producto con id ", id)
        return self.repositorioProducto.delete(id)



    # relacion  clientes y producto

    def asignarCliente(self, id, id_cliente):
        productoActual = Producto(self.repositorioProducto.findById(id))
        clienteActual = Cliente(self.repositorioCliente.findById(id_cliente))
        productoActual.cliente = clienteActual
        return self.repositorioProducto.save(productoActual)












