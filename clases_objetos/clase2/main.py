
# Paso 1: peso facturable
def peso_volumetrico(largo, ancho, alto):
    return (largo * ancho * alto) / 5000


def peso_facturable(peso_real, largo, ancho, alto):
    volumetrico = peso_volumetrico(largo, ancho, alto)
    if peso_real > volumetrico:
        return peso_real
    if volumetrico >= peso_real:
        return volumetrico


# Paso 2: costo base segun servicio
def costo_base(servicio):
    if servicio == "estandar":
        return 500
    if servicio == "express":
        return 1200
    if servicio == "mismo_dia":
        return 2500
    if servicio == "retiro_en_sucursal":
        return 350


# Paso 3: recargo por peso
def recargo_por_peso(peso):
    if peso <= 1:
        return 0
    if peso > 1 and peso <= 5:
        return (peso - 1) * 200
    if peso > 5:
        return 800 + (peso - 5) * 350


# Paso 4: multiplicador por destino
def multiplicador_destino(destino):
    if destino == "caba":
        return 1.0
    if destino == "gba":
        return 1.3
    if destino == "interior":
        return 1.8
    if destino == "patagonia":
        return 2.2


# Funcion principal: junta los cuatro pasos
def costo_envio(servicio, destino, peso_real, largo, ancho, alto):
    peso = peso_facturable(peso_real, largo, ancho, alto)
    base = costo_base(servicio)
    recargo = recargo_por_peso(peso)
    subtotal = base + recargo
    factor = multiplicador_destino(destino)
    return subtotal * factor


def main():
    # Caso 1: libro liviano, estandar, a CABA -> $500
    caso1 = costo_envio("estandar", "caba", 0.5, 20, 15, 5)
    print("Caso 1 (esperado $500):", caso1)

    # Caso 2: caja voluminosa, express, al interior -> $16.200
    caso2 = costo_envio("express", "interior", 3, 50, 50, 50)
    print("Caso 2 (esperado $16.200):", caso2)


if __name__ == "__main__":
    main()
