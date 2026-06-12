# ============================================================
#  TEMA 4: BUCLES
#  Desarrollado por: Alberto Velasco
# ============================================================
# Los bucles permiten repetir un bloque de código
# varias veces sin tener que escribirlo cada vez.

# ------------------------------------------------------------
# 1. BUCLE FOR
# ------------------------------------------------------------
# Recorre una secuencia (lista, string, rango...) elemento a elemento.

print("--- For básico ---")
frutas = ["manzana", "pera", "naranja"]

for fruta in frutas:
    print(fruta)

# Recorrer un string:
print("\n--- For en string ---")
for letra in "Python":
    print(letra)

# ------------------------------------------------------------
# 2. RANGE()
# ------------------------------------------------------------
# range(fin)           -> del 0 al fin-1
# range(inicio, fin)   -> del inicio al fin-1
# range(inicio, fin, paso) -> saltando de 'paso' en 'paso'

print("\n--- Range ---")
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

print()
for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

print()
for i in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10
    print(i)

# ------------------------------------------------------------
# 3. ENUMERATE() — índice + valor a la vez
# ------------------------------------------------------------
print("\n--- Enumerate ---")
colores = ["rojo", "verde", "azul"]

for indice, color in enumerate(colores):
    print(f"{indice}: {color}")

# ------------------------------------------------------------
# 4. BUCLE WHILE
# ------------------------------------------------------------
# Se repite MIENTRAS la condición sea True.
# Úsalo cuando no sabes cuántas veces vas a iterar.

print("\n--- While ---")
contador = 0

while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # importante: actualizar para no crear bucle infinito

# ------------------------------------------------------------
# 5. BREAK Y CONTINUE
# ------------------------------------------------------------
# break    -> sale del bucle inmediatamente
# continue -> salta a la siguiente iteración

print("\n--- Break ---")
for i in range(10):
    if i == 5:
        break       # para cuando i llega a 5
    print(i)

print("\n--- Continue ---")
for i in range(10):
    if i % 2 == 0:
        continue    # salta los números pares
    print(i)        # solo imprime los impares

# ------------------------------------------------------------
# 6. FOR / ELSE y WHILE / ELSE
# ------------------------------------------------------------
# El bloque else se ejecuta si el bucle termina SIN un break.

print("\n--- For / Else ---")
for i in range(5):
    print(i)
else:
    print("Bucle completado sin interrupciones")

# ============================================================
#  EJERCICIOS
# ============================================================

# EJERCICIO 1
# Imprime la tabla de multiplicar del 7 (del 7x1 al 7x10)
# usando un bucle for y range().

# Escribe tu solución aquí:


# EJERCICIO 2
# Dada la lista: numeros = [4, 7, 2, 9, 1, 5, 8, 3, 6]
# Recórrela con un for e imprime solo los números mayores que 5.

# Escribe tu solución aquí:


# EJERCICIO 3
# Usa un bucle while para simular una cuenta atrás desde 10 hasta 0.
# Cuando llegues a 0, imprime "¡Despegue!".

# Escribe tu solución aquí:


# EJERCICIO 4
# Recorre la lista: palabras = ["gato", "perro", "pájaro", "pez", "caballo"]
# Imprime cada palabra en mayúsculas junto a su índice.
# Ejemplo: "0: GATO"
# Pista: usa enumerate().

# Escribe tu solución aquí:


# EJERCICIO 5
# Usa un bucle for con range() para calcular la suma de todos
# los números del 1 al 100. Imprime el resultado.

# Escribe tu solución aquí:
