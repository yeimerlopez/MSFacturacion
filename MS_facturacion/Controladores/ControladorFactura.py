from Repositorios.repositorioFactura import RepositorioFactura
from Modelos.Factura import Factura



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


    def update(self, id , laFactura):
        print(" Actualizando una factura con id", id)
        facturaActual = Factura(self.repositorioFactura.findById(id))
        facturaActual.fecha = laFactura["fecha"]
        facturaActual.direccionEntrega = laFactura["direccionEntrega"]
        facturaActual.metodoPago= laFactura["metodoPago"]
        return self.repositorioFactura.save(facturaActual)



# ventaActual.xxxxx = laventa["xxxxx"]
# ventaActual.xxxxx = laventa["xxxxx"]



    def delete(self, id):
        print("Eliminando la factura con id ", id)
        return self.repositorioFactura.delete(id)