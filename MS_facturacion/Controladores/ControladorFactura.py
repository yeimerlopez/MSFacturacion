from Repositorios.repositorioFactura import RepositorioFactura
#from Repositorios.repositorioCliente import RepositorioCliente
from Modelos.Factura import Factura
#from Modelos.Cliente import Cliente


class ControladorFactura():
    def __init__(self):
        print("creando controlador factura")
        self.repositorioFactura = RepositorioFactura()
        #self.repositorioFactura = RepositorioFactura()

    def index(self):
        print("listar todas las facturas")
        return self.repositorioFactura.findAll()

    def create(self, laFactura):
        print("Crear una Factura")
        nuevoFactura = Factura(laFactura)
        return self.repositorioFactura.save(nuevoFactura)

    def show(self, id):
        print("Mostrando una factura con id", id)
        laFactura = Factura(self.repositorioFactura.findById(id))
        return laFactura.__dict__


    def update(self, id , lafactura):
        print(" Actualizando una factura con id", id)
        facturaActual = Factura(self.repositorioFactura.findById(id))
        facturaActual.fecha = lafactura["fecha"]
        #ventaActual.xxxxx = laventa["xxxxx"]
        #ventaActual.xxxxx = laventa["xxxxx"]
        return self.repositoriofactura.save(facturaActual)


    def delete(self, id):
        print("Eliminando la factura con id ", id)
        return self.repositorioFactura.delete(id)