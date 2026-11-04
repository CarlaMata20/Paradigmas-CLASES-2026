-- Plantilla: Evaluación perezosa y listas infinitas
-- Enunciados: evaluacion-perezosa-y-listas-infinitas.md
-- Cargar con: ghci Lazy.hs   (y :r para recargar después de editar)
--
-- Ojo: en GHCi, si evaluás una lista infinita sin take, cortá con Ctrl+C.

-- Ejercicio 1: Rangos infinitos --------------------------------------------


head [] = error " lista vacia"
head (x : _ ) = x

naturales :: [Integer]
naturales = [0..]

pares :: [Integer]
pares = filter even naturales 

multiplosDe3 :: [Integer]
multiplosDe3 = filter (\x -> mod x 3 == 0) naturales

multiplosDeN n = filter (\x -> mod x n == 0) naturales

-- Ejercicio 2: iterate -----------------------------------------------------

-- aplicarNVeces 
        -- 0.  1.    2.      3.            4. 
-- x f => [x, f x, f (f x), f (f (f x)), f (f (f (f x))),............]

iterar f valorInicial = valorInicial : iterar f (f valorInicial)

potenciasDe2 :: [Integer]
potenciasDe2 =  iterar (\x -> x * 2 ) 1

potenciasDe3 =  iterar (* 3) 1

potenciasDeN n = iterar (\x -> x * n) 1
primeraPotenciaMayor :: Integer -> Integer
primeraPotenciaMayor = undefined

-- Ejercicio 3: Fibonacci autorreferencial ----------------------------------

fibs :: [Integer]
fibs = undefined

-- Ejercicio 4: Criba de Eratóstenes ----------------------------------------

primos :: [Int]
primos = undefined

-- Ejercicio 5: cycle -------------------------------------------------------

alternar :: Int -> [Bool]
alternar = undefined

-- Ejercicio 6: takeWhile ---------------------------------------------------

sumaCuadradosMenores :: Int -> Int
sumaCuadradosMenores = undefined

-- Ejercicio 7: Las tuyas ---------------------------------------------------

miIterate :: (a -> a) -> a -> [a]
miIterate = undefined

miRepeat :: a -> [a]
miRepeat = undefined

miCycle :: [a] -> [a]
miCycle = undefined

-- Ejercicio 8: Collatz -----------------------------------------------------

collatz :: Int -> [Int]
collatz = undefined

-- Ejercicio 9: Tu propio if ------------------------------------------------

si :: Bool -> a -> a -> a
si = undefined

-- Ejercicio 10: scanl y zip ------------------------------------------------

triangulares :: [Int]
triangulares = undefined

enumerar :: [a] -> [(Int, a)]
enumerar = undefined

-- Ejercicio 11: Quiz -------------------------------------------------------
-- Anotá acá tu respuesta (valor, o "no termina") antes de probar:
--
--   fst (1, undefined)                   ->
--   length [undefined, undefined]        ->
--   head (map (* 2) [1 ..])              ->
--   take 3 (filter (> 100) [1 ..])       ->
--   let x = undefined in 5               ->
--   takeWhile (< 10) (map (* 2) [1 ..])  ->
--   filter (< 10) (map (* 2) [1 ..])     ->
--   take 5 (filter even [1, 3 ..])       ->
--   length [1 ..]                        ->
