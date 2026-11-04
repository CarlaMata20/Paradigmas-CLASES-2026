# Polimorfismo paramétrico y ad-hoc (clases de tipo)

Temas: funciones y tipos con variables de tipo (`a`, `b`); restricciones de clase (`Ord a =>`); instancias de clases existentes (`Show`, `Eq`, `Ord`, `Functor`); definición de clases propias con métodos por defecto.

Plantilla para resolver: `Polimorfismo.hs`.

## Repaso rápido

- **Paramétrico**: una sola definición sirve para todos los tipos, sin saber nada de ellos. `length :: [a] -> Int`.
- **Ad-hoc**: la misma función se comporta distinto según el tipo; cada tipo aporta su implementación en una `instance`. `show :: Show a => a -> String`.

```haskell
class Describible a where
  describir :: a -> String

instance Describible Bool where
  describir True  = "si"
  describir False = "no"
```

## Ejercicios

### 1. Funciones paramétricas

- `identidad :: a -> a`
- `duplicar :: a -> (a, a)`
- `aplicarPar :: (a -> b) -> (a, a) -> (b, b)`

```haskell
(identidad 'a', duplicar True, aplicarPar (+ 1) (1, 2))  -- ('a',(True,True),(2,3))
```

Para pensar: ¿cuántas funciones distintas (que terminen) pueden tener el tipo `a -> a`? ¿Y el tipo `a -> b`?

### 2. Tipos paramétricos

Definí `data Par a b = Par a b` y `data Caja a = Caja a` (derivando `Show`) y escribí:

- `intercambiarPar :: Par a b -> Par b a`
- `mapCaja :: (a -> b) -> Caja a -> Caja b`

```haskell
intercambiarPar (Par 1 "a")   -- Par "a" 1
mapCaja length (Caja "hola")  -- Caja 4
```

### 3. ¿Qué restricción hace falta?

Escribí las funciones y poné en la firma la restricción de clase **mínima** que necesita cada una:

- `maximoDe :: ??? => [a] -> a`
- `sumarTodos :: ??? => [a] -> a`
- `buscar :: ??? => k -> [(k, v)] -> Maybe v`

```haskell
maximoDe "haskell"               -- 's'
sumarTodos [1.5, 2.5]            -- 4.0
buscar "b" [("a", 1), ("b", 2)]  -- Just 2
```

### 4. Instancia de Show a mano

Dado `data Punto = Punto Double Double` (sin `deriving`), escribí `instance Show Punto` para que se muestre como `(1.0, 2.5)`.

deriving (Eq, Ord, Show)
### 5. Eq y Ord a mano

Dado el record `Persona { nombre :: String, edad :: Int }`:

- `instance Eq Persona`: dos personas son iguales si tienen el mismo nombre.
- `instance Ord Persona`: se ordenan por edad. Alcanza con definir `compare`.

```haskell
Persona "Ana" 30 == Persona "Ana" 99           -- True
maximum [Persona "Ana" 30, Persona "Beto" 25]  -- Persona {nombre = "Ana", edad = 30}
```

### 6. Tu propia clase

Definí `class Describible a` con `describir :: a -> String` e instancias para `Bool`, `Int` y `[a]` (esta última requiere que `a` también sea `Describible`).

```haskell
describir True           -- "verdadero"
describir (3 :: Int)     -- "el entero 3"
describir [True, False]  -- "lista de 2: verdadero falso"
```

Para pensar: ¿qué pasa con `describir "hola"`? ¿Y con `describir 3` sin la anotación de tipo?

### 7. Una clase, varios tipos

Definí `class Forma a` con `area` y `perimetro` (ambas devuelven `Double`), e instancias para `data Circulo = Circulo Double` y `data Rectangulo = Rectangulo Double Double`.

```haskell
(area (Circulo 1), perimetro (Rectangulo 2 3))  -- (3.141592653589793,10.0)
```

Para pensar: compará esto con el `data Figura` de `tipos-de-datos.md`. ¿Qué es más fácil con cada enfoque: agregar una figura nueva, o agregar una operación nueva?

### 8. Métodos por defecto y newtype

Definí:

```haskell
class Monoide a where
  neutro        :: a
  combinar      :: a -> a -> a
  combinarTodos :: [a] -> a   -- con implementación por defecto usando foldr
```

e instancias para `newtype Suma = Suma Int` (suma), `newtype Producto = Producto Int` (producto) y `[b]` (concatenación). Las instancias no deben redefinir `combinarTodos`.

```haskell
combinarTodos [Suma 1, Suma 2, Suma 3]  -- Suma 6
combinarTodos [Producto 2, Producto 5]  -- Producto 10
combinarTodos ["ab", "cd", "e"]         -- "abcde"
```
