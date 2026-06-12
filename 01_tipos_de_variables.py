# ============================================================
#  TEMA 1: TIPOS DE VARIABLES
#  Desarrollado por: Alberto Velasco
# ============================================================
# Una variable es un espacio en memoria donde guardamos datos.
# En Python no hace falta declarar el tipo, se asigna solo.

# ------------------------------------------------------------
# 1. NÚMEROS ENTEROS (int)
# ------------------------------------------------------------
edad = 25
año = 2024
temperatura_negativa = -10

print("--- Enteros ---")
print(edad)
print(type(edad))  # <class 'int'>

# ------------------------------------------------------------
# 2. NÚMEROS DECIMALES (float)
# ------------------------------------------------------------
precio = 9.99
pi = 3.14159
nota = 7.5

print("\n--- Decimales ---")
print(precio)
print(type(precio))  # <class 'float'>

# ------------------------------------------------------------
# 3. CADENAS DE TEXTO (str)
# ------------------------------------------------------------
nombre = "Ana"
apellido = 'García'
mensaje = "Hola, bienvenido a Python"

print("\n--- Texto ---")
print(nombre)
print(type(nombre))  # <class 'str'>

# ------------------------------------------------------------
# 4. BOOLEANOS (bool)
# ------------------------------------------------------------
# Solo pueden ser True (verdadero) o False (falso)
es_mayor_de_edad = True
tiene_descuento = False

print("\n--- Booleanos ---")
print(es_mayor_de_edad)
print(type(es_mayor_de_edad))  # <class 'bool'>

# ------------------------------------------------------------
# 5. NONE (valor nulo)
# ------------------------------------------------------------
# Representa la ausencia de valor
resultado = None

print("\n--- None ---")
print(resultado)
print(type(resultado))  # <class 'NoneType'>

# ------------------------------------------------------------
# 6. CONVERSIÓN ENTRE TIPOS
# ------------------------------------------------------------
numero_texto = "42"
numero_entero = int(numero_texto)    # str -> int
numero_decimal = float(numero_texto) # str -> float
de_vuelta_texto = str(numero_entero) # int -> str

print("\n--- Conversión ---")
print(numero_entero + 8)   # 50
print(numero_decimal + 0.5) # 42.5

# ============================================================
#  EJERCICIOS
# ============================================================

# EJERCICIO 1
# Crea una variable llamada 'mi_nombre' con tu nombre,
# otra llamada 'mi_edad' con tu edad,
# y otra llamada 'mi_altura' con tu altura en metros (decimal).
# Luego imprime cada variable y su tipo con type().

# Escribe tu solución aquí:


# EJERCICIO 2
# Crea una variable llamada 'numero_texto' que contenga el string "100".
# Conviértela a entero y súmale 50. Imprime el resultado.

# Escribe tu solución aquí:


# EJERCICIO 3
# ¿Cuál es el tipo de dato de cada uno de estos valores?
# Compruébalo con type() imprimiendo el resultado.
#   a) 3.0
#   b) "3"
#   c) 3
#   d) True
#   e) None

# Escribe tu solución aquí:
