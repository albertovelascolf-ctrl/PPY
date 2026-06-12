# ============================================================
#  TEMA 5: LISTAS Y DICCIONARIOS
#  Desarrollado por: Alberto Velasco
# ============================================================

# ============================================================
#  PARTE A: LISTAS
# ============================================================
# Una lista es una colección ordenada de elementos.
# Puede contener cualquier tipo de dato y se pueden repetir.

# ------------------------------------------------------------
# 1. CREAR UNA LISTA
# ------------------------------------------------------------
frutas = ["manzana", "pera", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = [42, "hola", True, 3.14]  # puede mezclar tipos
vacia = []

print("--- Listas ---")
print(frutas)
print(type(frutas))

# ------------------------------------------------------------
# 2. ACCEDER A ELEMENTOS
# ------------------------------------------------------------
print("\n--- Acceso ---")
print(frutas[0])   # manzana (primer elemento)
print(frutas[-1])  # naranja (último elemento)
print(frutas[1:3]) # ['pera', 'naranja'] (slicing)

# ------------------------------------------------------------
# 3. MODIFICAR LISTAS
# ------------------------------------------------------------
print("\n--- Modificar ---")
frutas.append("uva")        # añade al final
frutas.insert(1, "kiwi")    # inserta en posición 1
frutas.remove("pera")       # elimina por valor
eliminado = frutas.pop()    # elimina y devuelve el último
frutas[0] = "melón"         # modifica por índice

print(frutas)
print(f"Elemento eliminado con pop: {eliminado}")

# ------------------------------------------------------------
# 4. MÉTODOS ÚTILES
# ------------------------------------------------------------
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

print("\n--- Métodos ---")
print(len(numeros))          # longitud: 8
print(sum(numeros))          # suma: 31
print(min(numeros))          # mínimo: 1
print(max(numeros))          # máximo: 9
print(numeros.count(1))      # cuántas veces aparece el 1: 2

numeros.sort()               # ordena la lista (modifica la original)
print(numeros)

numeros_ordenados = sorted([3, 1, 4, 1, 5])  # devuelve nueva lista ordenada
print(numeros_ordenados)

# ------------------------------------------------------------
# 5. LISTAS DE LISTAS (matrices)
# ------------------------------------------------------------
print("\n--- Lista de listas ---")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[0])      # [1, 2, 3]
print(matriz[1][2])   # 6 (fila 1, columna 2)

# ============================================================
#  PARTE B: DICCIONARIOS
# ============================================================
# Un diccionario guarda pares clave-valor.
# Las claves son únicas y se usan para acceder a los valores.

# ------------------------------------------------------------
# 6. CREAR UN DICCIONARIO
# ------------------------------------------------------------
print("\n--- Diccionarios ---")
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
print(persona)
print(type(persona))

# ------------------------------------------------------------
# 7. ACCEDER A VALORES
# ------------------------------------------------------------
print("\n--- Acceso ---")
print(persona["nombre"])           # Ana
print(persona.get("edad"))         # 25
print(persona.get("email", "N/A")) # N/A (valor por defecto si no existe)

# ------------------------------------------------------------
# 8. MODIFICAR DICCIONARIOS
# ------------------------------------------------------------
print("\n--- Modificar ---")
persona["edad"] = 26               # modifica valor existente
persona["email"] = "ana@mail.com"  # añade nueva clave
del persona["ciudad"]              # elimina una clave

print(persona)

# ------------------------------------------------------------
# 9. RECORRER UN DICCIONARIO
# ------------------------------------------------------------
print("\n--- Recorrer ---")
alumno = {"nombre": "Luis", "nota": 8.5, "aprobado": True}

for clave in alumno:
    print(clave)                           # solo claves

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")             # clave y valor

print(list(alumno.keys()))                 # lista de claves
print(list(alumno.values()))               # lista de valores

# ------------------------------------------------------------
# 10. DICCIONARIO DE DICCIONARIOS
# ------------------------------------------------------------
print("\n--- Diccionario de diccionarios ---")
alumnos = {
    "A001": {"nombre": "Ana", "nota": 9.0},
    "A002": {"nombre": "Luis", "nota": 6.5},
}
print(alumnos["A001"]["nombre"])  # Ana

# ============================================================
#  EJERCICIOS
# ============================================================

# EJERCICIO 1
# Crea una lista con 5 de tus películas favoritas.
# - Añade una más al final con append()
# - Elimina la segunda película con remove() o pop()
# - Imprime la lista ordenada alfabéticamente

# Escribe tu solución aquí:


# EJERCICIO 2
# Crea un diccionario llamado 'coche' con las claves:
# 'marca', 'modelo', 'año' y 'color'.
# - Imprime solo el valor de 'marca'
# - Cambia el color
# - Añade una clave 'kilometros' con el valor que quieras
# - Recorre el diccionario imprimiendo "clave -> valor"

# Escribe tu solución aquí:


# EJERCICIO 3
# Dada la lista: notas = [8, 5, 9, 3, 7, 6, 4, 10, 2, 8]
# - Calcula e imprime la media
# - Imprime cuántas notas hay por encima de 5
# - Imprime la nota más alta y la más baja

# Escribe tu solución aquí:


# EJERCICIO 4
# Crea un diccionario de contactos con al menos 3 personas.
# Cada persona tiene: nombre, teléfono y email.
# Recorre el diccionario e imprime los datos de cada contacto
# de forma legible.

# Escribe tu solución aquí:
