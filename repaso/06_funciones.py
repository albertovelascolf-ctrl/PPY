# ============================================================
#  FUNCIONES
#  Desarrollado por: Alberto Velasco
# ============================================================
# Una función es un bloque de código reutilizable que realiza
# una tarea concreta. Evita repetir código y lo organiza mejor.

# ------------------------------------------------------------
# 1. DEFINIR Y LLAMAR UNA FUNCIÓN
# ------------------------------------------------------------
# Se define con 'def', seguido del nombre y paréntesis.

def saludar():
    print("¡Hola! Bienvenido a Python.")

# Para ejecutarla, la llamamos por su nombre:
saludar()
saludar()  # podemos llamarla todas las veces que queramos

# ------------------------------------------------------------
# 2. FUNCIONES CON PARÁMETROS
# ------------------------------------------------------------
# Los parámetros son valores que le pasamos a la función.

def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Luis")

# Con varios parámetros:
def presentar(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

presentar("Carlos", 30, "Madrid")

# ------------------------------------------------------------
# 3. PARÁMETROS CON VALOR POR DEFECTO
# ------------------------------------------------------------
# Si no se pasa ese argumento, usa el valor por defecto.

def saludar_idioma(nombre, idioma="español"):
    if idioma == "español":
        print(f"Hola, {nombre}")
    elif idioma == "inglés":
        print(f"Hello, {nombre}")

saludar_idioma("Ana")             # usa "español" por defecto
saludar_idioma("John", "inglés")  # usa "inglés"

# ------------------------------------------------------------
# 4. FUNCIONES QUE DEVUELVEN VALORES (return)
# ------------------------------------------------------------
# 'return' devuelve un resultado que podemos guardar o usar.

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(f"\nSuma: {resultado}")      # 8
print(f"Suma: {sumar(10, 20)}")    # 30

# Puede devolver varios valores a la vez:
def minimo_maximo(lista):
    return min(lista), max(lista)

minimo, maximo = minimo_maximo([4, 2, 8, 1, 9])
print(f"Mínimo: {minimo}, Máximo: {maximo}")

# ------------------------------------------------------------
# 5. VARIABLES LOCALES Y GLOBALES
# ------------------------------------------------------------
# Las variables dentro de una función son locales (solo existen ahí).
# Las variables fuera son globales.

nombre_global = "Python"

def mostrar_scope():
    nombre_local = "función"
    print(f"Dentro: {nombre_local}")
    print(f"Global accesible: {nombre_global}")

mostrar_scope()
print(f"Fuera: {nombre_global}")
# print(nombre_local)  # esto daría error: no existe fuera de la función

# ------------------------------------------------------------
# 6. FUNCIONES LAMBDA (funciones anónimas de una línea)
# ------------------------------------------------------------
# Útiles para operaciones simples y rápidas.

cuadrado = lambda x: x ** 2
sumar_lambda = lambda a, b: a + b

print(f"\nCuadrado de 5: {cuadrado(5)}")
print(f"Suma lambda: {sumar_lambda(3, 4)}")

# Muy útiles con sorted(), filter(), map():
numeros = [5, 2, 8, 1, 9, 3]
ordenados = sorted(numeros, key=lambda x: x)
print(f"Ordenados: {ordenados}")

# ------------------------------------------------------------
# 7. DOCSTRINGS (documentar funciones)
# ------------------------------------------------------------
# Buena práctica: explicar qué hace la función.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Parámetros:
        base (float): la base del rectángulo
        altura (float): la altura del rectángulo
    
    Retorna:
        float: el área del rectángulo
    """
    return base * altura

print(f"\nÁrea: {calcular_area_rectangulo(5, 3)}")
help(calcular_area_rectangulo)  # muestra el docstring

# ============================================================
#  EJERCICIOS
# ============================================================

# EJERCICIO 1
# Crea una función llamada 'es_par' que reciba un número
# y devuelva True si es par o False si es impar.
# Pruébala con varios números.

# Escribe tu solución aquí:


# EJERCICIO 2
# Crea una función llamada 'calcular_nota' que reciba una nota numérica
# y devuelva el texto correspondiente:
# >= 9 -> "Sobresaliente", >= 7 -> "Notable",
# >= 5 -> "Aprobado", < 5 -> "Suspenso"

# Escribe tu solución aquí:


# EJERCICIO 3
# Crea una función llamada 'contar_vocales' que reciba un texto
# y devuelva el número de vocales que contiene.
# Pruébala con una frase.

# Escribe tu solución aquí:


# EJERCICIO 4
# Crea una función llamada 'calcular_estadisticas' que reciba una lista
# de números y devuelva (como tupla): media, mínimo y máximo.
# Pruébala con la lista [5, 3, 8, 1, 9, 2, 7].

# Escribe tu solución aquí:


# EJERCICIO 5
# Crea una función con un parámetro por defecto:
# 'crear_usuario(nombre, rol="alumno")' que imprima
# "Usuario [nombre] creado con rol [rol]".
# Pruébala con y sin el parámetro rol.

# Escribe tu solución aquí:
