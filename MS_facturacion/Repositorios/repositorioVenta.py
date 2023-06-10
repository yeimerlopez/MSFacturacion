from Repositorios.interfaceRepositorio import InterfaceRepositorio
from Modelos.Venta import Venta
from bson import ObjectId


class RepositorioVenta(InterfaceRepositorio[Venta]):
    #def getListadoVentasEnProducto(self, id_producto):
    def getListadoIncritosEnMateria(self, id_producto):
        theQuery = {"producto.$id": ObjectId(id_producto)}
        return self.query(theQuery)


