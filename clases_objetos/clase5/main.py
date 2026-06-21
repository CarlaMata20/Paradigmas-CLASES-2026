

class Personaje:
    def __init__(self, vida, inventario, mana):
        self.vida = vida
        self.inventario = inventario
        self.mana = mana

    def agarrar_objeto(self, objeto):
        self.inventario.append(objeto)

    def atacar(self, otro):
        # el daño realizado es la mitad del mana
        danio = self.mana * 0.5
        # realizo el daño al enemigo
        otro.vida = otro.vida - danio
        self.mana = self.mana - danio

    def pelear(self, enemigo):
        # primero ataca self
        self.atacar(enemigo)
        # despues ataca el enemigo
        enemigo.atacar(self)

class Mago:
    pass

class Arma:
    def __init__(self, desgaste):
        self.desgaste = desgaste

class Silla(Arma):
    def danio(self):
        # no afecta el desgaste
        return 3

class Espada(Arma):
    def danio(self):
        return 20 - (self.desgaste + 2)

class Arco(Arma):
    def danio(self):
        return 15 - self.desgaste



# quiero que sea como un personaje pero ataca el doble que un personaje comun
class Guerrero(Personaje):
    def __init__(self, vida, inventario, mana, stamina, arma):
        # self.vida = vida
        # self.inventario = inventario
        # self.mana = mana
        super().__init__(vida, inventario, mana)
        self.stamina = stamina
        self.arma = arma

    # el guerrero hace el doble de daño que el personaje comun
    def atacar(self, otro):
        # el daño realizado es el del arma que porta el guerrero
        danio = self.arma.danio()
        # realizo el daño al enemigo
        otro.vida = otro.vida - danio

class GuerreroConEspada(Guerrero):
    def atacar(self, otro):
        # el daño realizado por la espada (20)
        danio = 20
        # realizo el daño al enemigo
        otro.vida = otro.vida - danio

class GuerreroConArco(Guerrero):
    def atacar(self, otro):
        # el daño realizado por el arco (15)
        danio = 15
        # realizo el daño al enemigo
        otro.vida = otro.vida - danio

class GuerreroConJavalina(Guerrero):
    pass

class Mounstruo:
    def __init__(self, vida, objetos_iniciales, defensa, ataque):
        self.vida = vida
        self.defensa = defensa
        self.inventario = objetos_iniciales
        self.ataque = ataque
    
    def agarrar_objeto(self, objeto):
        self.inventario.append(objeto)

    def atacar(self, enemigo):
        # el daño del mounstruo es el 10% de su ataque
        enemigo.vida = enemigo.vida - self.ataque * 0.1
        # se cansa al atacar, baja su vida en 1 cada vez que ataca
        self.vida = self.vida - 1