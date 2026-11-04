-- Plantilla: Pattern matching
-- Enunciados: pattern-matching.md
-- Cargar con: ghci PatternMatching.hs   (y :r para recargar después de editar)

-- Ejercicio 1: Literales ---------------------------------------------------

describirNumero :: Int -> String
describirNumero = undefined

-- Ejercicio 2: Tuplas ------------------------------------------------------

primero :: (a, b, c) -> a
primero = undefined

intercambiar :: (a, b) -> (b, a)
intercambiar = undefined

-- Ejercicio 3: Listas ------------------------------------------------------

cabeza :: [a] -> Maybe a
cabeza = undefined

segundo :: [a] -> Maybe a
segundo = undefined

tieneExactamenteDos :: [a] -> Bool
tieneExactamenteDos = undefined

-- Ejercicio 4: Maybe -------------------------------------------------------

desdeMaybe :: a -> Maybe a -> a
desdeMaybe = undefined

sumarMaybes :: Maybe Int -> Maybe Int -> Maybe Int
sumarMaybes = undefined

-- Ejercicio 5: Guardas -----------------------------------------------------

clasificarNota :: Int -> String
clasificarNota = undefined

-- Ejercicio 6: As-patterns -------------------------------------------------

duplicarPrimero :: [a] -> [a]
duplicarPrimero = undefined

-- Ejercicio 7: Records -----------------------------------------------------

data Punto = Punto { px :: Double, py :: Double }
  deriving (Show)

esOrigen :: Punto -> Bool
esOrigen = undefined

estaEnEjeY :: Punto -> Bool
estaEnEjeY = undefined

cuadrante :: Punto -> Int
cuadrante = undefined

-- Ejercicio 8: case y patrones en where ------------------------------------

describirLista :: [a] -> String
describirLista = undefined

horasYMinutos :: Int -> String
horasYMinutos = undefined

-- Ejercicio 9: Patrones anidados -------------------------------------------

sumarPrimerosDos :: [(Int, Int)] -> Int
sumarPrimerosDos = undefined

-- Ejercicio 10: Para pensar ------------------------------------------------
-- Anotá acá tu respuesta antes de probarlo:
--
