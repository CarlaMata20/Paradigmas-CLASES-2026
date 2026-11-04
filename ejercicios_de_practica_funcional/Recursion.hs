-- Plantilla: Definición recursiva de funciones usando pattern matching
-- Enunciados: recursion-con-pattern-matching.md
-- Cargar con: ghci Recursion.hs   (y :r para recargar después de editar)

-- Ejercicio 1: Sobre números -----------------------------------------------

factorial :: Integer -> Integer
factorial = undefined

fib :: Int -> Integer
fib = undefined

-- Ejercicio 2: Sobre listas, sin Prelude -----------------------------------

sumaLista :: [Int] -> Int
sumaLista = undefined

longitud :: [a] -> Int
longitud = undefined

maximoLista :: [Int] -> Int
maximoLista = undefined

-- Ejercicio 3: Pertenencia -------------------------------------------------

pertenece :: Eq a => a -> [a] -> Bool
pertenece = undefined

-- Ejercicio 4: Invertir ----------------------------------------------------

invertir :: [a] -> [a]
invertir = undefined

-- Ejercicio 5: take y drop -------------------------------------------------

tomar :: Int -> [a] -> [a]
tomar = undefined

soltar :: Int -> [a] -> [a]
soltar = undefined

-- Ejercicio 6: Intercalar --------------------------------------------------

intercalar :: [a] -> [a] -> [a]
intercalar = undefined

-- Ejercicio 7: Euclides ----------------------------------------------------

mcd :: Int -> Int -> Int
mcd = undefined

-- Ejercicio 8: Patrones de dos elementos -----------------------------------

aplanar :: [[a]] -> [a]
aplanar = undefined

comprimir :: Eq a => [a] -> [a]
comprimir = undefined

-- Ejercicio 9: Dígitos -----------------------------------------------------

digitos :: Int -> [Int]
digitos = undefined

-- Ejercicio 10: Sobre un árbol ---------------------------------------------

data Arbol a = Hoja | Nodo (Arbol a) a (Arbol a)
  deriving (Show)

altura :: Arbol a -> Int
altura = undefined

cantidadNodos :: Arbol a -> Int
cantidadNodos = undefined

-- Ejercicio 11: Recursión mutua --------------------------------------------

esPar :: Int -> Bool
esPar = undefined

esImpar :: Int -> Bool
esImpar = undefined

-- Ejercicio 12: Acumulador -------------------------------------------------

invertirAcc :: [a] -> [a]
invertirAcc = undefined
