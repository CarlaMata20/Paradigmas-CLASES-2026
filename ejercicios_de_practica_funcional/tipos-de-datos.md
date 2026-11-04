# Definición de tipos de datos

Temas: tipos enumerados, records, tipos suma con varios constructores, tipos recursivos (listas y árboles propios).

Plantilla para resolver: `TiposDeDatos.hs`. Cargala con `ghci TiposDeDatos.hs` y andá descomentando los stubs a medida que definís los tipos.

## Repaso rápido



```haskell
data Color = Rojo | Verde | Azul                -- enumerado
data Punto = Punto { x :: Double, y :: Double } -- record
data Lista = Fin | Nodo Int Lista               -- recursivo
```

- `deriving (Show, Eq, Ord, Enum, Bounded)` le pide al compilador instancias automáticas.
- Actualización de records: `p { x = 0 }` devuelve una copia de `p` con `x` cambiado.

## Ejercicios

### 1. Días de la semana

Definí el tipo enumerado `Dia` con los siete días (de `Lunes` a `Domingo`), derivando `Show`, `Eq`, `Enum` y `Bounded`.
Escribí `esFinDeSemana :: Dia -> Bool`.

```haskell
map esFinDeSemana [minBound .. maxBound]
-- [False,False,False,False,False,True,True]
```

### 2. Día siguiente (cíclico)

Escribí `siguienteDia :: Dia -> Dia`. Después del `Domingo` viene el `Lunes`.

```haskell
siguienteDia Domingo  -- Lunes
siguienteDia Jueves   -- Viernes
```

### 3. Record Persona

Definí el record `Persona` con los campos `nombre :: String` y `edad :: Int`, derivando `Show` y `Eq`.
Escribí:

- `cumplirAnios :: Persona -> Persona`, usando la sintaxis de actualización de records.
- `mayoresDeEdad :: [Persona] -> [String]`, que devuelve los nombres de quienes tienen 18 o más.

```haskell
cumplirAnios (Persona "Ana" 17)
-- Persona {nombre = "Ana", edad = 18}

mayoresDeEdad [Persona "Ana" 17, Persona "Beto" 30, Persona "Caro" 18]
-- ["Beto","Caro"]
```

### 4. Figuras

Definí `Figura` con tres constructores: `Circulo` (radio), `Rectangulo` (base y altura) y `Triangulo` (tres lados), todos con `Double`.
Escribí `area :: Figura -> Double`. Para el triángulo usá la fórmula de Herón: con `s = (a + b + c) / 2`, el área es `sqrt (s * (s - a) * (s - b) * (s - c))`.

```haskell
area (Rectangulo 3 4)   -- 12.0
area (Triangulo 3 4 5)  -- 6.0
```

### 5. Tu propia lista

Definí el tipo recursivo `ListaNat` con constructores `Vacia` y `Cons Int ListaNat`.
Escribí `longitudLN :: ListaNat -> Int`, `sumaLN :: ListaNat -> Int` y `aLista :: ListaNat -> [Int]`.

```haskell
let l = Cons 1 (Cons 2 (Cons 3 Vacia))
(longitudLN l, sumaLN l, aLista l)  -- (3,6,[1,2,3])
```

### 6. Árbol binario de búsqueda

Definí `Arbol a` con constructores `Hoja` y `Nodo (Arbol a) a (Arbol a)`.
Escribí:

- `insertar :: Ord a => a -> Arbol a -> Arbol a`, que inserta manteniendo el orden (menores a la izquierda, mayores a la derecha, repetidos se ignoran).
- `enOrden :: Arbol a -> [a]`, el recorrido en orden.

```haskell
enOrden (foldr insertar Hoja [5, 3, 8, 1, 4])  -- [1,3,4,5,8]
```

### 7. Expresiones aritméticas

Definí `Expr` con constructores `Num Int`, `Suma Expr Expr`, `Mult Expr Expr` y `Neg Expr`.
Escribí `evaluar :: Expr -> Int` y `mostrar :: Expr -> String` (con paréntesis alrededor de cada suma y producto).

```haskell
let e = Suma (Num 2) (Mult (Num 3) (Neg (Num 4)))
mostrar e  -- "(2 + (3 * -4))"
evaluar e  -- -10
```

### 8. Records anidados

Definí el record `Cuenta` con campos `titular :: Persona` y `saldo :: Double`.
Escribí:

- `depositar :: Double -> Cuenta -> Cuenta`
- `extraer :: Double -> Cuenta -> Maybe Cuenta`, que devuelve `Nothing` si el saldo no alcanza.

```haskell
let c = Cuenta (Persona "Ana" 17) 100
saldo (depositar 50 c)                                   -- 150.0
(fmap saldo (extraer 30 c), fmap saldo (extraer 500 c))  -- (Just 70.0,Nothing)
```
