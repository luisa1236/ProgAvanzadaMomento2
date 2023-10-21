class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None
        # None: denota falta de valor

    def calcular_precio_de_venta(self, margen_de_venta):
        if margen_de_venta <= 0:
            raise ValueError("El margen de utilidad debe estar por encima de cero.")
        return self.costo / (1 - margen_de_venta)

    def registrar_producto(self, callback):
        margen_de_venta = float(input("Cual es el margen de venta del producto: "))
        self.precio_de_venta = self.calcular_precio_de_venta(margen_de_venta)
        callback(self)
        print(f"¡{self.nombre} ha sido registrado con éxito!")

def imprimir_listado(productos):
    for id, producto in productos.items():
        print(f"ID: {id}, Nombre: {producto.nombre}, Descripción: {producto.descripcion}, Costo: {producto.costo}, Cantidad: {producto.cantidad}, Precio de Venta: {producto.precio_de_venta}")


productos = {}

def agregar_producto(producto):
    productos[producto.id] = producto

while True:
    print("________________________________")
    print("A. Registrar Producto")
    print("B. Imprimir Listado de Productos")
    print("C. Salir")
    print("________________________________")
    opcion = input("ELIJA UNA OPCIÓN: ")
    print("________________________________")

    if opcion == "A":
        id = int(input("ID del producto: "))
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        costo = float(input("Costo del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        producto = Producto(id, nombre, descripcion, costo, cantidad, 0)
        producto.registrar_producto(agregar_producto)
    elif opcion == "B":
        imprimir_listado(productos)
    elif opcion == "C":
        break
    else:
        print("NO TENGO ESA OPCIÓN")
