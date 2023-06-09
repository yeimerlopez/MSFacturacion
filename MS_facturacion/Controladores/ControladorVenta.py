from Repositorios.repositorioVenta import RepositorioVenta
#from Repositorios.repositorioCliente import RepositorioCliente
from Modelos.Venta import Venta
#from Modelos.Cliente import Cliente


class ControladorVenta():
    def __init__(self):
        print("creando controlador venta")
        self.repositorioVenta = RepositorioVenta()
        #self.repositorioCliente = RepositorioCliente()

    def index(self):
        print("listar todos las ventas")
        return self.repositorioVenta.findAll()

    def create(self, laVenta):
        print("Crear una Venta")
        nuevoVenta = Venta(laVenta)
        return self.repositorioVenta.save(nuevoVenta)

    def show(self, id):
        print("Mostrando una venta con id", id)
        laVenta = Venta(self.repositorioVenta.findById(id))
        return laVenta.__dict__


    def update(self, id , laventa):
        print(" Actualizando un producto con id", id)

        ventaActual = Venta(self.repositorioVenta.findById(id))
        ventaActual.cantidad = laventa["cantidad"]
        #ventaActual.xxxxx = laventa["xxxxx"]
        #ventaActual.xxxxx = laventa["xxxxx"]
        return self.repositorioVenta.save(ventaActual)


    def delete(self, id):
        print("Eliminando la venta con id ", id)
        return self.repositorioVenta.delete(id)