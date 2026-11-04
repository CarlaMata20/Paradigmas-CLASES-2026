# Evaluación perezosa y listas infinitas

Plantilla para resolver: `Lazy.hs`.

## Repaso rápido

```haskell
[1 ..]               -- infinita
take 3 [1 ..]        -- [1,2,3]
iterate (* 2) 1      -- [1,2,4,8,...]
takeWhile (< 10) xs  -- corta cuando el predicado falla por primera vez
```

Nunca uses `length`, `sum`, `reverse` o `filter` sin un `take` / `takeWhile` sobre una lista infinita: no terminan.

## Ejercicios

### 1. Rangos infinitos

Definí `naturales`, `pares` (con `filter`) y `multiplosDe3`, todas de tipo `[Integer]`.

```haskell
(take 5 naturales, take 5 pares, take 5 multiplosDe3)
-- ([0,1,2,3,4],[0,2,4,6,8],[0,3,6,9,12])
```


Definí `miIterate`, `miRepeat` y `miCycle` con el mismo comportamiento que las del Prelude.

```haskell
take 4 (miIterate (+ 3) 0)  -- [0,3,6,9]
take 3 (miRepeat 'x')       -- "xxx"
take 7 (miCycle [1, 2, 3])  -- [1,2,3,1,2,3,1]
```


### ¿termina? ¿qué devuelve?

Respondé antes de probar. Si una no termina, cortala con `Ctrl+C`.

```haskell
fst (1, undefined)
length [undefined, undefined]
head (map (* 2) [1 ..])
take 3 (filter (> 100) [1 ..])
let x = undefined in 5
takeWhile (< 10) (map (* 2) [1 ..])
filter (< 10) (map (* 2) [1 ..])
take 5 (filter even [1, 3 ..])
length [1 ..]
```
