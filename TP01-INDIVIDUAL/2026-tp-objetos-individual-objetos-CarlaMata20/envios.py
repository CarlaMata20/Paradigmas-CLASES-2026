#Paquete
#Servicio
#ServicioEstandar
#ServicioExpress
#ServicioMismoDia
#ServicioRetiroSucursal
#Destino
#ResultadoEnvio
#CalculadoraEnvio
#AplicacionPDPEnvios


class Paquete:
    def __init__(self, peso, largo, ancho, alto):
        self.peso = peso
        self.largo = largo
        self.ancho = ancho
        self.alto = alto

    def peso_volumetrico(self):
        return (self.largo * self.ancho * self.alto) / 5000

    def peso_facturable(self):
        return max(self.peso, self.peso_volumetrico())

    def es_valido(self):
        return self.peso > 0 and self.largo > 0 and self.ancho > 0 and self.alto > 0


class Servicio:
    def __init__(self, nombre, costo_base):#_init_ es el constructor de la clase
        self.nombre = nombre
        self.costo_base = costo_base
    def esta_disponible(self, destino):
        return True



class ServicioEstandar(Servicio):
    def __init__(self):
        super().__init__("Estándar", 500)#super() para llamar al constructor de la clase padre


class ServicioExpress(Servicio):
    def __init__(self):
        super().__init__("Express", 1200)


class ServicioMismoDia(Servicio):
    def __init__(self):
        super().__init__("Mismo día", 2500)

    def esta_disponible(self, destino):
        return destino.nombre in ["CABA", "GBA"]

class ServicioRetiroSucursal(Servicio):
    def __init__(self):
        super().__init__("Retiro en sucursal", 350)


class Destino:
    def __init__(self, nombre, factor):
        self.nombre = nombre
        self.factor = factor


class ResultadoEnvio:
    def __init__(self, paquete, servicio, destino, recargo, subtotal, total):
        self.paquete = paquete
        self.servicio = servicio
        self.destino = destino
        self.recargo = recargo
        self.subtotal = subtotal
        self.total = total

    def mostrar(self):
        print("---- RESULTADO DEL ENVÍO -----")
        print(f"Servicio: {self.servicio.nombre}")# F para interpolar variables dentro de una cadena. 
        #Permite incluir expresiones dentro de llaves {} que se evaluarán en tiempo de ejecución y se 
        # insertarán en la cadena resultante.
        print(f"Destino: {self.destino.nombre}")
        print(f"Peso real: {self.paquete.peso:.2f} kg")#.2f para mostrar solo 2 decimales
        print(f"Peso volumétrico: {self.paquete.peso_volumetrico():.2f} kg")
        print(f"Peso facturable: {self.paquete.peso_facturable():.2f} kg")
        print(f"Costo base: ${self.servicio.costo_base:.2f}")
        print(f"Recargo por peso: ${self.recargo:.2f}")
        print(f"Subtotal: ${self.subtotal:.2f}")
        print(f"Factor destino: {self.destino.factor}")
        print(f"Costo total: ${self.total:.2f}")


class CalculadoraEnvio:
    def calcular_recargo(self, peso_facturable):
        if peso_facturable <= 1:
            return 0
        elif peso_facturable <= 5:
            return (peso_facturable - 1) * 200
        else:
            return 800 + (peso_facturable - 5) * 350

    def calcular_total(self, paquete, servicio, destino):
        if not paquete.es_valido():
            raise ValueError("Error: los datos del paquete no son válidos.")

        if not servicio.esta_disponible(destino): #Raise para lanzar una excepción si el servicio no está disponible para el destino, en Javascript se usaría throw new Error() para lanzar una excepción.
            raise ValueError("Error: el servicio mismo día solo está disponible para CABA y GBA.")

        peso_facturable = paquete.peso_facturable()
        recargo = self.calcular_recargo(peso_facturable)

        subtotal = servicio.costo_base + recargo
        total = subtotal * destino.factor

        return ResultadoEnvio(paquete, servicio, destino, recargo, subtotal, total)




def main():#Me ahorro los inputs, cargar los datos en consola y creo los objetos directamente para mostrar el funcionamiento de la calculadora.
    calculadora = CalculadoraEnvio()

    # CASO 1
    envio1 = calculadora.calcular_total(
        Paquete(0.5, 20, 15, 5),
        ServicioEstandar(),
        Destino("CABA", 1.0)
    )
    envio1.mostrar()

    # CASO 2
    envio2 = calculadora.calcular_total(
        Paquete(3, 50, 50, 50),
        ServicioExpress(),
        Destino("Interior", 1.8)
    )
    envio2.mostrar()
    # CASO 3
    envio3 = calculadora.calcular_total(
        Paquete(0.8, 10, 10, 10),
        ServicioMismoDia(),
        Destino("CABA", 1.0)
    )
    envio3.mostrar()
        # CASO 4
    envio4 = calculadora.calcular_total(
        Paquete(1, 10, 10, 10),
        ServicioRetiroSucursal(),
        Destino("CABA", 1.0)
    )
    envio4.mostrar()
    # CASO 5
    envio5 = calculadora.calcular_total(
        Paquete(3, 10, 10, 10),
        ServicioEstandar(),
        Destino("GBA", 1.3)
    )
    envio5.mostrar()
    # CASO 6
    envio6 = calculadora.calcular_total(
        Paquete(10, 10, 10, 10),
        ServicioExpress(),
        Destino("Patagonia", 2.2)
    )
    envio6.mostrar()
    # CASO 7
    envio7 = calculadora.calcular_total(
        Paquete(5, 10, 10, 10),
        ServicioEstandar(),
        Destino("Interior", 1.8)
    )
    envio7.mostrar()
    # CASO 8
    envio8 = calculadora.calcular_total(
        Paquete(1, 100, 50, 40),
        ServicioEstandar(),
        Destino("CABA", 1.0)
    )
    envio8.mostrar()
    # CASO 9
    envio9 = calculadora.calcular_total(
        Paquete(2, 20, 20, 20),
        ServicioMismoDia(),
        Destino("GBA", 1.3)
    )
    envio9.mostrar()
    # CASO 10
    envio10 = calculadora.calcular_total(
        Paquete(7, 15, 15, 15),
        ServicioRetiroSucursal(),
        Destino("Patagonia", 2.2)
    )
    envio10.mostrar()

if __name__ == "__main__":#el __name__ es una variable especial que se asigna al nombre del módulo. #
    # Si el módulo se ejecuta directamente, __name__ será "__main__". Si el módulo se importa, __name__ será el nombre del módulo.
    main()

#servicio,destino,peso_real,largo,ancho,alto,costo_esperado
#1estandar,caba,0.5,20,15,5,500
#2express,interior,3,50,50,50,16200
#3mismo_dia,caba,0.8,10,10,10,2500
#4retiro_en_sucursal,caba,1,10,10,10,350
#5estandar,gba,3,10,10,10,1170
#6express,patagonia,10,10,10,10,8250
#7estandar,interior,5,10,10,10,2340
#8estandar,caba,1,100,50,40,13550
#9mismo_dia,gba,2,20,20,20,3510
#10retiro_en_sucursal,patagonia,7,15,15,15,4070
