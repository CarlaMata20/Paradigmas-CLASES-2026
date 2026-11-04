-- Plantilla: Funciones de orden superior y expresiones lambda
-- Enunciados: orden-superior-y-lambdas.md
-- Cargar con: ghci OrdenSuperior.hs   (y :r para recargar después de editar)

-- Ejercicio 1: Aplicar dos veces -------------------------------------------

-- aplicarDosVeces siguienteDia Lunes ==> Miercoles
data Dia = Lunes | Martes | Miercoles | Jueves | Viernes | Sabado | Domingo
  deriving (Show)

siguienteDia :: Dia -> Dia
siguienteDia Lunes = Martes 
siguienteDia Martes = Miercoles 
siguienteDia Miercoles = Jueves
siguienteDia Jueves = Viernes 
siguienteDia Viernes = Sabado 
siguienteDia Sabado = Domingo 
siguienteDia Domingo = Lunes 

aplicarFuncion :: (a -> b) -> a -> b 
aplicarFuncion funcion variable = funcion variable  

aplicarDosVeces :: (a -> a) -> a -> a
aplicarDosVeces funcion variable = funcion (funcion variable)

aplicarNVeces :: (a -> a) -> a -> Int -> a
aplicarNVeces funcion variable 0 = variable
aplicarNVeces funcion variable n = aplicarNVeces funcion (funcion variable) (n-1)

-- Ejercicio 2: Reimplementar map y filter ----------------------------------

miMap :: (a -> b) -> [a] -> [b]
miMap  f []   = []
miMap  f (elem : restoDeLaLista) = (f elem) : (miMap f restoDeLaLista)

miFilter :: (a -> Bool) -> [a] -> [a]
miFilter condicion [] = []
miFilter condicion (elem : restoDeLaLista)
    | condicion elem  =  elem : (miFilter condicion restoDeLaLista)  -- se cumple la condicion
    | otherwise = miFilter condicion restoDeLaLista

esPar x = mod x 2 == 0 

-- Ejercicio 3: Composición -------------------------------------------------

sumaCuadradosPares :: [Int] -> Int
sumaCuadradosPares = undefined

-- Ejercicio 4: Todo con foldr ----------------------------------------------

longitud' :: [a] -> Int
longitud' = undefined

concatenar' :: [[a]] -> [a]
concatenar' = undefined

maximo' :: [Int] -> Int
maximo' = undefined

-- Ejercicio 5: Componer una lista de funciones -----------------------------

componer :: [a -> a] -> (a -> a)
componer = undefined

-- Ejercicio 6: Contar los que cumplen --------------------------------------

contarSi :: (a -> Bool) -> [a] -> Int
contarSi = undefined

-- Ejercicio 7: Lista de funciones, un argumento ----------------------------

aplicarATodos :: [a -> b] -> a -> [b]
aplicarATodos = undefined

aplicarATodos' :: [a -> b] -> a -> [b]
aplicarATodos' = undefined

-- Ejercicio 8: Producto escalar --------------------------------------------

productoEscalar :: [Double] -> [Double] -> Double
productoEscalar = undefined

-- Ejercicio 9: until -------------------------------------------------------

primeraPotenciaDe2Mayor :: Int -> Int
primeraPotenciaDe2Mayor = undefined

-- Ejercicio 10: Mini quiz --------------------------------------------------
-- Anotá acá tu respuesta antes de probar en GHCi.
--
--   map (subtract 1) [1, 2, 3]  ->
--   map (`div` 2) [10, 11]      ->
--   map (2 `div`) [1, 2]        ->
--   flip (-) 1 10               ->
