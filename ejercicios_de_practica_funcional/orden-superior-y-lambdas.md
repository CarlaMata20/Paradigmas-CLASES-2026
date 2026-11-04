# Funciones de orden superior y expresiones lambda

Plantilla para resolver: `OrdenSuperior.hs`.

## Repaso rápido

```haskell
\x -> x * 2              -- lambda
(+ 1), (2 *), (`div` 2)  -- secciones: funciones de un argumento
f . g                    -- composición: (f . g) x = f (g x)
foldr (+) 0 [1, 2, 3]    -- 1 + (2 + (3 + 0))
```

## Ejercicios

### 1. Aplicar dos veces

`aplicarDosVeces :: (a -> a) -> a -> a`

```haskell
aplicarDosVeces (\x -> x * 3) 2  -- 18
aplicarDosVeces (++ "!") "hola"  -- "hola!!"
```

### 2. Reimplementar map y filter

Escribí `miMap :: (a -> b) -> [a] -> [b]` y `miFilter :: (a -> Bool) -> [a] -> [a]` con recursión, sin usar las del Prelude.

```haskell
miMap (+ 1) [1, 2, 3]   -- [2,3,4]
miFilter odd [1 .. 10]  -- [1,3,5,7,9]
```

### 3. Composición

`sumaCuadradosPares :: [Int] -> Int`: suma de los cuadrados de los números pares.

```haskell
sumaCuadradosPares [1 .. 6]  -- 56   (4 + 16 + 36)
```


### 4. Componer una lista de funciones

`componer :: [a -> a] -> (a -> a)`. La lista `[f, g, h]` tiene que comportarse como `f . g . h`. Pista: `foldr` e `id`.

```haskell
componer [(+ 1), (* 2)] 5  -- 11
componer [(* 2), (+ 1)] 5  -- 12
```

### 6. Contar los que cumplen

`contarSi :: (a -> Bool) -> [a] -> Int`

```haskell
contarSi even [1 .. 10]     -- 5
contarSi (> 'm') "haskell"  -- 1
```

### 7. Lista de funciones, un argumento

`aplicarATodos :: [a -> b] -> a -> [b]`. Escribila dos veces: `aplicarATodos` con una lambda y `aplicarATodos'` usando la aplicacion parcial de "$"  `($ x)`.

```haskell
aplicarATodos [(+ 1), (* 2), (^ 2)] 5  -- [6,10,25]
```

### 8. Producto escalar

`productoEscalar :: [Double] -> [Double] -> Double`, usando `zipWith`.

```haskell
productoEscalar [1, 2, 3] [4, 5, 6]  -- 32.0
```
