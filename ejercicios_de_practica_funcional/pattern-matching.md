# Pattern matching

Temas: patrones sobre literales, tuplas, listas, `Maybe` y records; comodín `_`; as-patterns `xs@(x:_)`; guardas; `case`; patrones en `where` / `let`.

Plantilla para resolver: `PatternMatching.hs`.

## Repaso rápido

```haskell
f 0 = ...                             -- literal
f (x, y) = ...                        -- tupla
f [] = ...  ;  f (x:xs) = ...         -- lista
f Nothing = ...  ;  f (Just x) = ...  -- Maybe
f todo@(x:_) = ...                    -- as-pattern: `todo` es la lista completa
f n | n > 0 = ... | otherwise = ...   -- guardas
```

Las ecuaciones se prueban **de arriba hacia abajo**: gana la primera que matchea.

## Ejercicios

### 1. Literales

`describirNumero :: Int -> String`: `"cero"` para 0, `"uno"` para 1, `"muchos"` para el resto.

```haskell
map describirNumero [0, 1, 7]  -- ["cero","uno","muchos"]
```

### 2. Tuplas

- `primero :: (a, b, c) -> a`
- `intercambiar :: (a, b) -> (b, a)`

```haskell
primero (1, "a", True)  -- 1
intercambiar (1, "a")   -- ("a",1)
```

### 3. Listas

- `cabeza :: [a] -> Maybe a`
- `segundo :: [a] -> Maybe a` (el segundo elemento, si existe)
- `tieneExactamenteDos :: [a] -> Bool`, sin usar `length`

```haskell
(cabeza "", cabeza "abc")         -- (Nothing,Just 'a')
(segundo [1], segundo [1, 2, 3])  -- (Nothing,Just 2)
tieneExactamenteDos [1, 2]        -- True
```

### 4. Maybe

- `desdeMaybe :: a -> Maybe a -> a`: devuelve el valor, o el default si es `Nothing`.
- `sumarMaybes :: Maybe Int -> Maybe Int -> Maybe Int`: `Just` de la suma si ambos son `Just`, si no `Nothing`.

```haskell
desdeMaybe 0 (Just 5)          -- 5
sumarMaybes (Just 1) (Just 2)  -- Just 3
sumarMaybes (Just 1) Nothing   -- Nothing
```

### 5. Guardas

`clasificarNota :: Int -> String`: `"invalida"` fuera de 0..10, `"desaprobado"` si es menor a 4, `"aprobado"` si es menor a 7, `"promocionado"` en otro caso.

```haskell
map clasificarNota [2, 5, 9, 11]
-- ["desaprobado","aprobado","promocionado","invalida"]
```


### 6. Records

Dado `data Punto = Punto { px :: Double, py :: Double }`:

- `esOrigen :: Punto -> Bool`, matcheando por posición: `(Punto 0 0)`.
- `estaEnEjeY :: Punto -> Bool`, matcheando por nombre de campo: `(Punto { px = 0 })`.
- `cuadrante :: Punto -> Int`: 1 a 4, o 0 si está sobre algún eje.

```haskell
map cuadrante [Punto 1 1, Punto (-1) 1, Punto (-1) (-1), Punto 1 (-1), Punto 0 3]
-- [1,2,3,4,0]
```
