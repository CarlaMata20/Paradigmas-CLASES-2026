# Café Delta — solución de los puntos 1 a 5


# Excepciones propias (Punto 5)
class PedidoVacioError(Exception):
    pass


class SinStockError(Exception):
    pass


# Punto 1: clase base
class Producto:
    def __init__(self, nombre, precio_base, apto_vegano, stock):
        self.nombre = nombre
        self.precio_base = precio_base
        self.apto_vegano = apto_vegano
        self.stock = stock

    def precio(self):
        return self.precio_base


# Punto 2: subclases con herencia y polimorfismo
class Bebida(Producto):
    def __init__(self, nombre, precio_base, apto_vegano, stock, ml):
        super().__init__(nombre, precio_base, apto_vegano, stock)
        self.ml = ml

    def precio(self):
        if self.ml >= 500:
            return self.precio_base * 1.4
        return self.precio_base


class Postre(Producto):
    def __init__(self, nombre, precio_base, apto_vegano, stock, toppings=None):
        super().__init__(nombre, precio_base, apto_vegano, stock)
        self.toppings = toppings if toppings is not None else []

    def precio(self):
        return self.precio_base + len(self.toppings) * 300


# Punto 3 y 5: el pedido
class Pedido:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if producto.stock <= 0:
            raise SinStockError(f"{producto.nombre} no tiene stock disponible")
        self.productos.append(producto)
        producto.stock -= 1

    def total(self):
        return sum(p.precio() for p in self.productos)

    def cobrar(self):
        if not self.productos:
            raise PedidoVacioError("El pedido está vacío")
        return self.total()


# Punto 4: promociones y consultas
def menu_apto_vegano(productos):
    return [p for p in productos if p.apto_vegano]


def crear_descuento(porcentaje):
    def aplicar(producto):
        return producto.precio() * (1 - porcentaje / 100)
    return aplicar


def hay_stock_de_todo(productos):
    return all(p.stock > 0 for p in productos)


def hay_opcion_barata(productos, tope):
    return any(p.precio() < tope for p in productos)


def main():
    cafe     = Bebida("Café americano",     2000, True,  10, ml=250)
    latte    = Bebida("Latte",              2800, False,  3, ml=500)
    brownie  = Postre("Brownie",            3500, False,  0, toppings=["dulce de leche", "nueces"])
    ensalada = Postre("Ensalada de frutas", 3000, True,   5)
    menu = [cafe, latte, brownie, ensalada]

    print("Precio del latte:", latte.precio())       # 3920.0
    print("Precio del brownie:", brownie.precio())   # 4100

    pedido = Pedido()
    pedido.agregar(latte)
    pedido.agregar(ensalada)
    print("Total del pedido:", pedido.cobrar())      # 6920.0

    print("Aptos veganos:", [p.nombre for p in menu_apto_vegano(menu)])

    con_promo = crear_descuento(10)
    print("Precios con 10% off:", list(map(con_promo, menu)))

    print("¿Hay stock de todo?", hay_stock_de_todo(menu))
    print("¿Hay opción barata (< 2500)?", hay_opcion_barata(menu, 2500))

    # Punto 5: pedido vacío
    try:
        Pedido().cobrar()
    except PedidoVacioError as e:
        print("Error al cobrar:", e)

    # Punto 5: producto sin stock
    try:
        pedido.agregar(brownie)
    except SinStockError as e:
        print("Error al agregar:", e)


if __name__ == "__main__":
    main()
