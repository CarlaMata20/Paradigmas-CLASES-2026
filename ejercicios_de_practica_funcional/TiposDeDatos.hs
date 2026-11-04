-- Plantilla: Definición de tipos de datos
-- Enunciados: tipos-de-datos.md
-- Cargar con: ghci TiposDeDatos.hs   (y :r para recargar después de editar)
--
-- Los stubs están comentados porque usan tipos que tenés que definir vos.
-- Descomentá cada bloque a medida que avanzás, así el archivo siempre compila.

-- Ejercicio 1: Días de la semana -------------------------------------------
data Palo = Oro | Copa | Espada | Basto 
    deriving Show

data Dia = Lunes | Martes | Miercoles | Jueves | Viernes | Sabado | Domingo
  deriving (Show)

esFinDeSemana :: Dia -> Bool
esFinDeSemana Sabado  = True 
esFinDeSemana Domingo = True 
esFinDeSemana _       = False

-- Ejercicio 2: Día siguiente (cíclico) -------------------------------------

siguienteDia :: Dia -> Dia
siguienteDia Lunes = Martes 
siguienteDia Martes = Miercoles 
siguienteDia Miercoles = Jueves
siguienteDia Jueves = Viernes 
siguienteDia Viernes = Sabado 
siguienteDia Sabado = Domingo 
siguienteDia Domingo = Lunes 


-- f(x,y+1) 
-- f x (y+1)
diaDespuesDeNDias :: Dia -> Int -> Dia
diaDespuesDeNDias diaInicial 0  = diaInicial 
diaDespuesDeNDias diaInicial n = diaDespuesDeNDias (siguienteDia diaInicial) (n-1)
-- ejemplo: diaDespuesDeNDias Lunes 2 => Miercoles 

-- Ejercicio 3: Record Persona ----------------------------------------------

data Persona = Persona { nombre :: String, edad :: Int }
  deriving (Show, Eq)

rocio :: Persona
rocio = Persona { nombre = "Rocio", edad = 23}

zeus = Persona { nombre = "Zeus", edad = 24}
zeus2 = Persona {nombre = "Zeus", edad = 0 }

cumplirAnios :: Persona -> Persona
cumplirAnios (Persona n e) = Persona n (e + 1)

recibirse :: Persona -> Persona 
recibirse (Persona n e) = Persona ("Ing. " ++ n) e

-- cumplirAnios :: Persona -> Persona
-- cumplirAnios = undefined


esMayorDeEdad :: Persona -> Bool
esMayorDeEdad (Persona nombre  edad) = edad >= 18  

mayoresDeEdad :: [Persona] -> [String]
mayoresDeEdad listaDePersonas = map nombre (filter esMayorDeEdad listaDePersonas) 

-- ejemplo: mayoresDeEdad [zeus, zeus2, rocio ] => ["Zeus", "Rocio"]
listaInvitados :: [Persona]
listaInvitados = [zeus, zeus2, rocio ]

-- Ejercicio 4: Figuras -----------------------------------------------------

-- data Figura = ...

-- area :: Figura -> Double
-- area = undefined

-- Ejercicio 5: Tu propia lista ---------------------------------------------

-- data ListaNat = ...

-- longitudLN :: ListaNat -> Int
-- longitudLN = undefined

-- sumaLN :: ListaNat -> Int
-- sumaLN = undefined

-- aLista :: ListaNat -> [Int]
-- aLista = undefined

-- Ejercicio 6: Árbol binario de búsqueda -----------------------------------

-- data Arbol a = ...

-- insertar :: Ord a => a -> Arbol a -> Arbol a
-- insertar = undefined

-- enOrden :: Arbol a -> [a]
-- enOrden = undefined

-- Ejercicio 7: Expresiones aritméticas -------------------------------------

-- data Expr = ...

-- evaluar :: Expr -> Int
-- evaluar = undefined

-- mostrar :: Expr -> String
-- mostrar = undefined

-- Ejercicio 8: Records anidados --------------------------------------------

-- data Cuenta = Cuenta { ... }

-- depositar :: Double -> Cuenta -> Cuenta
-- depositar = undefined

-- extraer :: Double -> Cuenta -> Maybe Cuenta
-- extraer = undefined
