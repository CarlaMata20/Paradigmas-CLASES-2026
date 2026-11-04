-- Plantilla: Polimorfismo paramétrico y ad-hoc (clases de tipo)
-- Enunciados: polimorfismo-parametrico-y-ad-hoc.md
-- Cargar con: ghci Polimorfismo.hs   (y :r para recargar después de editar)
--
-- Algunos bloques están comentados porque dependen de tipos o clases que
-- tenés que definir vos. Descomentalos a medida que avanzás.

-- Ejercicio 1: Funciones paramétricas --------------------------------------

identidad :: a -> a
identidad = undefined

duplicar :: a -> (a, a)
duplicar = undefined

aplicarPar :: (a -> b) -> (a, a) -> (b, b)
aplicarPar = undefined

-- Ejercicio 2: Tipos paramétricos ------------------------------------------

-- data Par a b = ...
-- data Caja a = ...

-- intercambiarPar :: Par a b -> Par b a
-- intercambiarPar = undefined

-- mapCaja :: (a -> b) -> Caja a -> Caja b
-- mapCaja = undefined

-- Ejercicio 3: ¿Qué restricción hace falta? --------------------------------
-- Completá las firmas con la restricción mínima.

-- maximoDe :: ??? => [a] -> a
-- maximoDe = undefined

-- sumarTodos :: ??? => [a] -> a
-- sumarTodos = undefined

-- buscar :: ??? => k -> [(k, v)] -> Maybe v
-- buscar = undefined

-- Ejercicio 4: Instancia de Show a mano ------------------------------------

data Punto = Punto Double Double

instance Show Punto where
  show = undefined

-- Ejercicio 5: Eq y Ord a mano ---------------------------------------------

data Persona = Persona { nombre :: String, edad :: Int }
  deriving (Show)

instance Eq Persona where
  (==) = undefined

instance Ord Persona where
  compare = undefined

-- Ejercicio 6: Tu propia clase ---------------------------------------------

-- class Describible a where
--   ...

-- instance Describible Bool where
--   ...

-- instance Describible Int where
--   ...

-- instance ... => Describible [a] where
--   ...

-- Ejercicio 7: Una clase, varios tipos -------------------------------------

data Circulo = Circulo Double
data Rectangulo = Rectangulo Double Double

-- class Forma a where
--   ...

-- instance Forma Circulo where
--   ...

-- instance Forma Rectangulo where
--   ...

-- Ejercicio 8: Métodos por defecto y newtype -------------------------------

-- class Monoide a where
--   neutro        :: a
--   combinar      :: a -> a -> a
--   combinarTodos :: [a] -> a
--   combinarTodos = ...

-- newtype Suma = Suma Int deriving (Show)
-- newtype Producto = Producto Int deriving (Show)

-- instance Monoide Suma where
--   ...

-- instance Monoide Producto where
--   ...

-- instance Monoide [b] where
--   ...

-- Ejercicio 9: Polimorfismo en el tipo de retorno --------------------------

-- class Default a where
--   def :: a

-- instance Default Int where ...
-- instance Default Bool where ...
-- instance Default [a] where ...

-- Ejercicio 10: Functor ----------------------------------------------------

data Arbol a = Hoja | Nodo (Arbol a) a (Arbol a)
  deriving (Show)

-- instance Functor Caja where
--   fmap = undefined

instance Functor Arbol where
  fmap = undefined
