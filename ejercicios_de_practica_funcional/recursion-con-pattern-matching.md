# Definición recursiva de funciones usando pattern matching

Temas: caso base + caso recursivo, recursión sobre números y listas, recursión sobre tipos propios, recursión mutua, acumuladores.

Plantilla para resolver: `Recursion.hs`.

## Repaso rápido

Toda definición recursiva sobre listas tiene la misma forma:

```haskell
f []     = <caso base>
f (x:xs) = <combinar x con> f xs
```

Preguntate siempre: ¿cuál es el caso más chico? ¿Cómo achico el problema en cada llamada?

## Ejercicios

### 1. Sobre números

- `factorial :: Integer -> Integer`
- `fib :: Int -> Integer` (`fib 0 = 0`, `fib 1 = 1`)

```haskell
factorial 5        -- 120
map fib [0 .. 10]  -- [0,1,1,2,3,5,8,13,21,34,55]
```

### 2. Sobre listas, sin Prelude

- `sumaLista :: [Int] -> Int`
- `longitud :: [a] -> Int`
- `maximoLista :: [Int] -> Int` (lista no vacía: el caso base es `[x]`)

```haskell
(sumaLista [1, 2, 3], longitud "hola", maximoLista [3, 9, 2])  -- (6,4,9)
```

### 3. Pertenencia

`pertenece :: Eq a => a -> [a] -> Bool`

```haskell
pertenece 3 [1, 2, 3]  -- True
pertenece 'z' "abc"    -- False
```

### 4. Invertir

`invertir :: [a] -> [a]`, usando `++`.

```haskell
invertir "hola"  -- "aloh"
```

### 5. take y drop

- `tomar :: Int -> [a] -> [a]`
- `soltar :: Int -> [a] -> [a]`

Tienen que funcionar aunque `n` sea más grande que la lista.

```haskell
(tomar 2 [1, 2, 3, 4], tomar 10 [1, 2])    -- ([1,2],[1,2])
(soltar 2 [1, 2, 3, 4], soltar 10 [1, 2])  -- ([3,4],[])
```

### 6. Intercalar

`intercalar :: [a] -> [a] -> [a]`: alterna elementos de las dos listas; cuando una se acaba, sigue con la otra. Pista: en la llamada recursiva, intercambiá las listas.

```haskell
intercalar [1, 3, 5] [2, 4, 6, 8, 10]  -- [1,2,3,4,5,6,8,10]
```

### 7. Euclides

`mcd :: Int -> Int -> Int`, máximo común divisor con `mod`.

```haskell
mcd 48 18  -- 6
mcd 7 5    -- 1
```

### 8. Patrones de dos elementos

- `aplanar :: [[a]] -> [a]`
- `comprimir :: Eq a => [a] -> [a]`: elimina repetidos consecutivos. Pista: matcheá `(x:y:ys)`.

```haskell
aplanar [[1, 2], [], [3]]  -- [1,2,3]
comprimir "aaabccdd"       -- "abcd"
```

### 9. Dígitos

`digitos :: Int -> [Int]`, con `div` y `mod`.

```haskell
digitos 1234  -- [1,2,3,4]
digitos 7     -- [7]
```

### 10. Sobre un árbol

Dado `data Arbol a = Hoja | Nodo (Arbol a) a (Arbol a)` (ya está en la plantilla):

- `altura :: Arbol a -> Int` (una `Hoja` tiene altura 0)
- `cantidadNodos :: Arbol a -> Int`

```haskell
let a = Nodo (Nodo Hoja 1 Hoja) 2 (Nodo (Nodo Hoja 3 Hoja) 4 Hoja)
(altura a, cantidadNodos a)  -- (3,4)
```

### 11. Recursión mutua

`esPar` y `esImpar :: Int -> Bool`, definidas una en términos de la otra, sin usar `mod` ni `even`.

```haskell
(esPar 10, esImpar 7, esPar 7)  -- (True,True,False)
```

### 12. Acumulador

`invertirAcc :: [a] -> [a]`: otra versión de `invertir` con una función auxiliar en el `where` que lleve un acumulador. No tiene que usar `++`.

```haskell
invertirAcc [1, 2, 3]  -- [3,2,1]
```
