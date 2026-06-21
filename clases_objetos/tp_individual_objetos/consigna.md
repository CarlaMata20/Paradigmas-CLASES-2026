Una empresa de logística, PDPEnvios, necesita calcular cuánto cobrar por enviar un paquete. El precio final depende de cuatro cosas: el tipo de servicio elegido por el cliente, el destino del envío, el peso del paquete y su volumen. La función principal del proyecto recibe estos datos de entrada y devuelve el costo total en pesos argentinos.
 
## Reglas de negocio
 
El cálculo del costo sigue cuatro pasos aplicados en orden: primero se determina el peso facturable, luego el costo base según el servicio, después se suma el recargo por peso, y finalmente se multiplica por el factor del destino.
 
### Paso 1: Peso facturable
 
El peso facturable es el valor (en kilogramos) que se usa para calcular el recargo. **No siempre coincide con el peso real del paquete**, porque un paquete muy voluminoso pero liviano ocupa lugar en el camión igual que uno pesado, y eso también cuesta.
 
Se calcula como el mayor entre el peso real y el peso volumétrico, donde el peso volumétrico se obtiene dividiendo el volumen del paquete por un factor estándar de la industria:
 
```
peso_volumétrico = (largo × ancho × alto) / 5000
peso_facturable  = max(peso_real, peso_volumétrico)
```
 
Las dimensiones se expresan en centímetros. Por ejemplo, una caja de 50×50×50 cm pesando 1 kg tiene un peso volumétrico de 25 kg, y se factura como si pesara 25 kg.
 
### Paso 2: Costo base según servicio
 
| Servicio              | Costo base | Observaciones                                |
|-----------------------|-----------:|----------------------------------------------|
| Estándar              |   $500     | Entrega en 3 a 5 días hábiles                |
| Express               |  $1.200    | Entrega en 24 a 48 horas                     |
| Mismo día             |  $2.500    | Solo disponible en CABA y GBA                |
| Retiro en sucursal    |   $350     | 30% de descuento sobre el estándar           |
 
### Paso 3: Recargo por peso
 
Al costo base se le suma un recargo que depende del peso facturable. El esquema es escalonado: los primeros kilos son gratis, los siguientes cuestan un precio, y los que superan cierto umbral cuestan más.
 
| Rango de peso facturable   | Recargo                                       |
|----------------------------|-----------------------------------------------|
| Hasta 1 kg                 | Sin recargo                                   |
| De 1 kg a 5 kg             | $200 por cada kg adicional (por encima de 1)  |
| Más de 5 kg                | $800 fijos + $350 por cada kg por encima de 5 |
 
Los $800 fijos del tercer tramo corresponden al recargo acumulado por los 4 kg del tramo anterior (4 × $200).
 
### Paso 4: Multiplicador por destino
 
El costo acumulado se multiplica por un factor que depende del destino geográfico. Cuanto más lejos o más difícil es llegar, mayor es el factor.
 
| Destino                       | Factor multiplicador |
|-------------------------------|---------------------:|
| CABA                          | 1.0                  |
| GBA                           | 1.3                  |
| Interior (resto del país)     | 1.8                  |
| Patagonia                     | 2.2                  |
 
## Ejemplos de cálculo
 
Para ver cómo se combinan los pasos, conviene seguir dos casos completos.
 
**Caso 1: paquete liviano, servicio estándar, a CABA.** Un libro de 0,5 kg en una caja de 20×15×5 cm, enviado en modalidad estándar a CABA. El peso volumétrico es (20×15×5)/5000 = 0,3 kg, menor que el peso real, así que el peso facturable es 0,5 kg. El costo base es $500 (estándar). No hay recargo por peso (está por debajo de 1 kg). El multiplicador de CABA es 1,0. **Costo final: $500.**
 
**Caso 2: paquete voluminoso pero liviano, servicio express, al interior.** Una caja de 50×50×50 cm con 3 kg de ropa adentro, enviada en express al interior del país. Acá el peso volumétrico manda: (50×50×50)/5000 = 25 kg, mucho mayor que los 3 kg reales, así que el peso facturable es 25 kg. El costo base es $1.200 (express). El recargo por peso, como está por encima de 5 kg, es $800 + (25 − 5) × $350 = $7.800, así que el subtotal queda en $9.000. Finalmente, el multiplicador de interior es 1,8: $9.000 × 1,8 = **$16.200.**
