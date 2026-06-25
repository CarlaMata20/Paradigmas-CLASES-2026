import pytest
from main import Bebida, Postre, Pedido, PedidoVacioError, SinStockError


# Punto 2
def test_bebida_sin_recargo():
    assert Bebida("Café", 2000, True, 5, ml=250).precio() == 2000

def test_bebida_con_recargo():
    assert Bebida("Latte", 2800, False, 3, ml=500).precio() == 2800 * 1.4

def test_postre_sin_toppings():
    assert Postre("Tarta", 3000, True, 5).precio() == 3000

def test_postre_con_toppings():
    assert Postre("Brownie", 3500, False, 2, toppings=["a", "b"]).precio() == 4100


# Punto 3
def test_total_pedido():
    latte   = Bebida("Latte",    2800, False, 3, ml=500)
    ensalada = Postre("Ensalada", 3000, True,  5)
    pedido = Pedido()
    pedido.agregar(latte)
    pedido.agregar(ensalada)
    assert pedido.total() == 6920.0


# Punto 5
def test_cobrar_pedido_vacio():
    with pytest.raises(PedidoVacioError):
        Pedido().cobrar()

def test_agregar_sin_stock():
    brownie = Postre("Brownie", 3500, False, 0)
    with pytest.raises(SinStockError):
        Pedido().agregar(brownie)

def test_agregar_descuenta_stock():
    cafe = Bebida("Café", 2000, True, 2, ml=250)
    pedido = Pedido()
    pedido.agregar(cafe)
    assert cafe.stock == 1
