
from Modelos.Cliente import Cliente
from Repositorios.repositorioCliente import RepositorioCliente

class ControladorCliente():
    def __init__(self):
        print("creando controlador Cliente")
        self.repositorioCliente = RepositorioCliente()


    def index(self):
        print("listar todos los Clientes esto sale solo en la consola")
        return self.repositorioCliente.findAll()


    def create(self, elCliente):
        print("creando un cliente ;-)")
        nuevoCliente = Cliente(elCliente)
        return self.repositorioCliente.save(nuevoCliente)


    def show(self, id):
        print("Mostrando un Cliente con id", id)
        elCliente = Cliente(self.repositorioCliente.findById(id))
        return elCliente.__dict__


    def update(self, id, elCliente):
        print(" Actualizando una cliente con id", id)

        clienteActual = Cliente(self.repositorioCliente.findById(id))
        clienteActual.nombre = elCliente["nombre"]
        clienteActual.direccion = elCliente["direccion"]
        clienteActual.telefono = elCliente["telefono"]
        return self.repositorioCliente.save(clienteActual)





        elCliente = Cliente(elCliente)
        return elCliente.__dict__

    def delete(self, id):
        print("Eliminando cliente con id ", id)
        return self.repositorioCliente.delete(id)





