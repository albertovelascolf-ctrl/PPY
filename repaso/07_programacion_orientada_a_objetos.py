# ============================================================
#  PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
#  Desarrollado por: Alberto Velasco
# ============================================================
# La POO organiza el código en "objetos" que combinan
# datos (atributos) y comportamiento (métodos).
#
# Analogía: una CLASE es como un molde/plano,
# y un OBJETO es algo creado a partir de ese molde.
# Ej: "Perro" es la clase, y "Rex" es un objeto (instancia).

# ------------------------------------------------------------
# 1. DEFINIR UNA CLASE
# ------------------------------------------------------------

class Perro:
    # __init__ es el constructor: se llama al crear el objeto
    # 'self' representa al propio objeto
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre  # atributo
        self.raza = raza      # atributo
        self.edad = edad      # atributo

    # Método: una función que pertenece a la clase
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def presentarse(self):
        print(f"Soy {self.nombre}, un {self.raza} de {self.edad} años.")


# ------------------------------------------------------------
# 2. CREAR OBJETOS (instanciar la clase)
# ------------------------------------------------------------
print("--- Crear objetos ---")
rex = Perro("Rex", "Pastor Alemán", 3)
luna = Perro("Luna", "Labrador", 5)

rex.presentarse()
luna.presentarse()
rex.ladrar()

# Acceder a atributos directamente:
print(rex.nombre)
print(luna.edad)

# ------------------------------------------------------------
# 3. MODIFICAR ATRIBUTOS
# ------------------------------------------------------------
print("\n--- Modificar atributos ---")
rex.edad = 4  # cumpleaños de Rex
print(f"Nueva edad de Rex: {rex.edad}")

# ------------------------------------------------------------
# 4. MÉTODO __str__ (representación en texto del objeto)
# ------------------------------------------------------------

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        # Esto se llama cuando hacemos print(objeto)
        return f"'{self.titulo}' de {self.autor} ({self.paginas} páginas)"

    def es_largo(self):
        return self.paginas > 300


print("\n--- Método __str__ ---")
libro1 = Libro("El Quijote", "Cervantes", 863)
libro2 = Libro("El Principito", "Saint-Exupéry", 96)

print(libro1)  # usa __str__
print(libro2)
print(f"¿El Quijote es largo? {libro1.es_largo()}")

# ------------------------------------------------------------
# 5. HERENCIA
# ------------------------------------------------------------
# Una clase puede heredar atributos y métodos de otra.
# La clase hija extiende o modifica a la clase padre.

class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hablar(self):
        print(f"{self.nombre} hace: {self.sonido}")

    def __str__(self):
        return f"Animal: {self.nombre}"


class Gato(Animal):  # Gato hereda de Animal
    def __init__(self, nombre):
        super().__init__(nombre, "Miau")  # llama al __init__ del padre
        self.vidas = 7

    def ronronear(self):  # método propio de Gato
        print(f"{self.nombre} ronronea... Purrrr")


class Pato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "Cuac")

    def nadar(self):
        print(f"{self.nombre} está nadando")


print("\n--- Herencia ---")
gato = Gato("Whiskers")
pato = Pato("Donald")

gato.hablar()       # heredado de Animal
gato.ronronear()    # propio de Gato
print(f"Vidas: {gato.vidas}")

pato.hablar()       # heredado de Animal
pato.nadar()        # propio de Pato

# ------------------------------------------------------------
# 6. ATRIBUTOS DE CLASE (compartidos por todos los objetos)
# ------------------------------------------------------------

class Contador:
    total = 0  # atributo de clase (compartido)

    def __init__(self, nombre):
        self.nombre = nombre
        Contador.total += 1  # se incrementa cada vez que se crea uno

    @classmethod
    def cuantos_hay(cls):
        print(f"Se han creado {cls.total} contadores")


print("\n--- Atributos de clase ---")
c1 = Contador("primero")
c2 = Contador("segundo")
c3 = Contador("tercero")
Contador.cuantos_hay()  # 3

# ============================================================
#  EJERCICIOS
# ============================================================

# EJERCICIO 1
# Crea una clase 'Rectangulo' con atributos 'base' y 'altura'.
# Añade métodos para calcular el área (base * altura)
# y el perímetro (2 * (base + altura)).
# Crea dos rectángulos distintos e imprime sus medidas.

# Escribe tu solución aquí:


# EJERCICIO 2
# Crea una clase 'CuentaBancaria' con:
# - Atributos: titular (nombre) y saldo (empieza en 0)
# - Método 'ingresar(cantidad)': suma al saldo
# - Método 'retirar(cantidad)': resta del saldo, pero si no hay
#   suficiente saldo imprime "Saldo insuficiente"
# - Método '__str__': muestra titular y saldo actual
# Pruébala haciendo varios ingresos y retiradas.

# Escribe tu solución aquí:


# EJERCICIO 3
# Crea una clase 'Vehiculo' con atributos: marca, modelo y velocidad_max.
# Luego crea dos clases que hereden de ella: 'Coche' y 'Moto'.
# - Coche tiene un atributo extra: num_puertas
# - Moto tiene un atributo extra: tipo (ej: "deportiva", "scooter")
# Ambas clases deben tener un método 'describir()' que imprima
# todos sus datos.

# Escribe tu solución aquí:


# EJERCICIO 4
# Crea una clase 'Estudiante' con nombre y una lista de notas vacía.
# Añade métodos para:
# - agregar_nota(nota): añade una nota a la lista
# - calcular_media(): devuelve la media de las notas
# - esta_aprobado(): devuelve True si la media es >= 5
# Crea un estudiante, añádele 5 notas y muestra si está aprobado.

# Escribe tu solución aquí:
