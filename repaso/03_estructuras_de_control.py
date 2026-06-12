# ============================================================
#  ESTRUCTURAS DE CONTROL
#  Desarrollado por: Alberto Velasco
# ============================================================
# Las estructuras de control permiten tomar decisiones
# en el programa según condiciones.

# ------------------------------------------------------------
# 1. IF / ELIF / ELSE
# ------------------------------------------------------------
# if   -> si se cumple la condición
# elif -> si no se cumplió la anterior y se cumple esta
# else -> si no se cumplió ninguna condición anterior

edad = 20

print("--- If / Elif / Else ---")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Con varias condiciones:
nota = 6.5

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

# ------------------------------------------------------------
# 2. OPERADORES DE COMPARACIÓN
# ------------------------------------------------------------
# ==   igual a
# !=   distinto de
# >    mayor que
# <    menor que
# >=   mayor o igual que
# <=   menor o igual que

print("\n--- Comparaciones ---")
print(5 == 5)   # True
print(5 != 3)   # True
print(10 > 3)   # True
print(2 >= 2)   # True

# ------------------------------------------------------------
# 3. OPERADORES LÓGICOS
# ------------------------------------------------------------
# and  -> se cumplen AMBAS condiciones
# or   -> se cumple AL MENOS UNA condición
# not  -> niega la condición

print("\n--- Operadores lógicos ---")

tiene_dni = True
es_mayor = True

if tiene_dni and es_mayor:
    print("Puede votar")

temperatura = 35

if temperatura > 30 or temperatura < 0:
    print("Temperatura extrema")

llueve = False
if not llueve:
    print("No llueve, puedes salir")

# ------------------------------------------------------------
# 4. OPERADOR TERNARIO (if en una línea)
# ------------------------------------------------------------
# valor_si_true if condicion else valor_si_false

edad = 20
estado = "mayor" if edad >= 18 else "menor"
print(f"\nEres {estado} de edad")

# ------------------------------------------------------------
# 5. MATCH / CASE (Python 3.10+, similar al switch)
# ------------------------------------------------------------
dia = "lunes"

print("\n--- Match / Case ---")
match dia:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print("Día laborable")
    case "sábado" | "domingo":
        print("Fin de semana")
    case _:
        print("Día no reconocido")

# ============================================================
#  EJERCICIOS
# ============================================================

# EJERCICIO 1
# Pide al usuario su edad con input() y conviértela a entero.
# Imprime si puede conducir (>=18), si le falta poco (entre 16 y 17)
# o si todavía es muy joven (menos de 16).

# Escribe tu solución aquí:


# EJERCICIO 2
# Crea una variable 'numero' con cualquier valor entero.
# Imprime si el número es positivo, negativo o cero.

# Escribe tu solución aquí:


# EJERCICIO 3
# Crea dos variables: 'usuario' y 'contraseña' con valores de tu elección.
# Simula un login: si ambas coinciden con los valores guardados, imprime
# "Acceso concedido", en caso contrario "Acceso denegado".

# Escribe tu solución aquí:


# EJERCICIO 4
# Dado un precio, aplica descuento usando estas reglas:
# - Si el precio es mayor de 100€ -> 20% de descuento
# - Si el precio está entre 50€ y 100€ -> 10% de descuento
# - Si es menor de 50€ -> sin descuento
# Imprime el precio final.

# Escribe tu solución aquí:
