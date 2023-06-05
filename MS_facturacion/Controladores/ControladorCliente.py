
from Modelos.Cliente import Cliente
from Repositorios.repositorioCliente import RepositorioCliente

class ControladorCliente():
    def __init__(self):
        print("creando controlador Cliente")
        self.repositorioCliente = RepositorioCliente()


    def index(self):
        print("listar todos los Clientes esto sale solo en la consola")
        # codigo para simular lo que a futuro se mostrara Datos quemados
        unCliente = {
            "id": "1234",
            "nombre": "Juan",
            "apellido": "Perez",
            "telefono": "123456789",
            "email": "plsgq@example.com",
            "direccion": "Calle 123",
        }
        return [unCliente]


    def create(self, elCliente):
        print("creando un cliente ;-)")
        nuevoCliente = Cliente(elCliente)
        return self.repositorioCliente.save(nuevoCliente)


    def show(self, id):
        print("Mostrando un Cliente con id", id)
        elCliente = {
            "id": "1234",
            "nombre": "Juan",
            "apellido": "Perez",
            "telefono": "123456789",
            "email": "plsgq@example.com",
            "direccion": "Calle 123",
        }
        return elCliente

    def update(self, id, elCliente):
        print(" Actualizando una cliente con id", id)
        elCliente =Cliente(elCliente)
        return elCliente.__dict__

    def delete(self, id):
        print("Eliminando cliente con id ", id)
        return {"deleted_count": 1 }


