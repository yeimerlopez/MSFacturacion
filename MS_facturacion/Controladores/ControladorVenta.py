from Repositorios.repositorioVenta import RepositorioVenta
from Modelos.Venta import Venta
from Repositorios.repositorioFactura import RepositorioFactura
from Modelos.Factura import Factura
from Repositorios.repositorioProducto import RepositorioProducto
from Modelos.Producto import Producto




class ControladorVenta():
    def __init__(self):
        print("creando controlador venta")
        self.repositorioVenta = RepositorioVenta()
        self.repositorioFactura = RepositorioFactura()
        self.repositorioProducto = RepositorioProducto()

    def index(self):
        print("listar todos las ventas")
        return self.repositorioVenta.findAll()

    """
    Asignacion factura y producto a venta  V
    
    """
    def create(self, infoVenta, id_factura, id_producto):
        nuevoVenta = Venta(infoVenta)
        lafactura = Factura(self.repositorioFactura.findById(id_factura))
        elproducto = Producto(self.repositorioProducto.findById(id_producto))  # repositorio materias estaba en plural
        nuevoVenta.factura = lafactura
        nuevoVenta.producto = elproducto
        return self.repositorioVenta.save(nuevoVenta)

    def show(self, id):
        laVenta = Venta(self.repositorioVenta.findById(id))
        return laVenta.__dict__

    """
        Modificación de inscripción (estudiante y materia)              


    """

    def update(self, id, infoVenta, id_factura, id_producto):
        laVenta = Venta(self.repositorioVenta.findById(id))
        laVenta.fecha = infoVenta["fecha"]
        laVenta.precio = infoVenta["precio"]
        laFactura = Factura(self.repositorioFactura.findById(id_factura))
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        laVenta.factura = laVenta
        laVenta.producto = laVenta
        return self.repositorioVenta.save(laVenta)

    def delete(self, id):
        return self.repositorioVenta.delete(id)

    """
    Obtener todos LOS PRODUCTOS EN LAS VENTAS
    """

    #def listarVentasxproducto(self, id_producto):
    def ListarInscritosEnMateria(self, id_producto):
        return self.repositorioVenta.getListadoIncritosEnMateria(id_producto)


