# ============================================================
#  TEMA 2: MANEJO DE STRINGS (CADENAS DE TEXTO)
#  Desarrollado por: Alberto Velasco
# ============================================================
# Un string es una secuencia de caracteres entre comillas.
# Python ofrece muchas herramientas para trabajar con texto.

# ------------------------------------------------------------
# 1. CREAR STRINGS
# ------------------------------------------------------------
simple = 'Hola'
doble = "Mundo"
multilinea = """Este texto
ocupa varias
líneas"""

print(simple)
print(doble)
print(multilinea)

# ------------------------------------------------------------
# 2. CONCATENAR (unir) STRINGS
# ------------------------------------------------------------
nombre = "Ana"
apellido = "García"

completo = nombre + " " + apellido
print("\n--- Concatenación ---")
print(completo)  # Ana García

# ------------------------------------------------------------
# 3. F-STRINGS (la forma más moderna y cómoda)
# ------------------------------------------------------------
edad = 25
mensaje = f"Me llamo {nombre} y tengo {edad} años."
print("\n--- F-strings ---")
print(mensaje)

# También puedes hacer operaciones dentro:
print(f"El doble de mi edad es {edad * 2}")

# ------------------------------------------------------------
# 4. MÉTODOS ÚTILES DE STRINGS
# ------------------------------------------------------------
texto = "  Hola, Python!  "

print("\n--- Métodos ---")
print(texto.upper())       # TODO EN MAYÚSCULAS
print(texto.lower())       # todo en minúsculas
print(texto.strip())       # elimina espacios al inicio y al final
print(texto.replace("Python", "Mundo"))  # reemplaza texto
print(texto.strip().startswith("Hola"))  # ¿empieza por "Hola"? -> True
print(len(texto))          # longitud del string (número de caracteres)

# ------------------------------------------------------------
# 5. ACCEDER A CARACTERES (indexación)
# ------------------------------------------------------------
# Los índices empiezan en 0
palabra = "Python"

print("\n--- Indexación ---")
print(palabra[0])   # P  (primer carácter)
print(palabra[1])   # y
print(palabra[-1])  # n  (último carácter)

# ------------------------------------------------------------
# 6. SLICING (obtener partes del string)
# ------------------------------------------------------------
# formato: texto[inicio:fin]  (fin no incluido)
frase = "Hola Mundo"

print("\n--- Slicing ---")
print(frase[0:4])   # Hola
print(frase[5:])    # Mundo  (desde el índice 5 hasta el final)
print(frase[:4])    # Hola   (desde el principio hasta el índice 4)

# ------------------------------------------------------------
# 7. DIVIDIR UN STRING
# ------------------------------------------------------------
csv = "manzana,pera,naranja"
frutas = csv.split(",")  # divide por la coma
print("\n--- Split ---")
print(frutas)  # ['manzana', 'pera', 'naranja']

# ============================================================
#  EJERCICIOS
# ============================================================

# EJERCICIO 1
# Crea dos variables: 'ciudad' y 'pais' con los valores que quieras.
# Usa un f-string para imprimir: "Vivo en [ciudad], [pais]."

# Escribe tu solución aquí:


# EJERCICIO 2
# Dada la variable: frase = "  El cielo es azul  "
# - Elimina los espacios del principio y el final
# - Convierte todo a mayúsculas
# - Imprime el resultado

# Escribe tu solución aquí:


# EJERCICIO 3
# Dada la variable: texto = "Python es genial"
# - Imprime solo la palabra "Python" usando slicing
# - Imprime el último carácter usando índice negativo
# - Imprime cuántos caracteres tiene en total

# Escribe tu solución aquí:


# EJERCICIO 4
# Dada la variable: nombres = "Ana,Luis,María,Carlos"
# Divídela por la coma e imprime cada nombre en una línea separada.
# Pista: usa split() y un print por cada elemento.

# Escribe tu solución aquí:
