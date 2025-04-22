# 1. Determinar si un número es par o impar
# La lógica aquí es usar el operador módulo (%) para verificar si el resto de la división entre 2 es 0.
numero = 15
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

# 2. Saludar según la hora del día
# Se utilizan condicionales anidados para verificar en qué rango de horas se encuentra la hora actual.
hora = 14
if 6 <= hora < 12:
    print("¡Buenos días!")
elif 12 <= hora < 18:
    print("¡Buenas tardes!")
else:
    print("¡Buenas noches!")

# 3. Calcular la suma de los números en una lista
# Un bucle 'for' itera sobre cada elemento de la lista, acumulando la suma en una variable.
numeros = [1, 2, 3, 4, 5]
suma = 0
for num in numeros:
    suma += num
print(f"La suma de los números en la lista es: {suma}")

# 4. Encontrar el número más grande en una lista
# Se inicializa una variable con el primer elemento y luego se compara con los demás en un bucle 'for'.
numeros = [10, 5, 20, 8, 15]
maximo = numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num
print(f"El número más grande en la lista es: {maximo}")

# 5. Invertir una cadena de texto
# Se utiliza un bucle 'for' para iterar desde el último carácter hasta el primero y construir la cadena invertida.
cadena = "Hola"
invertida = ""
for i in range(len(cadena) - 1, -1, -1):
    invertida += cadena[i]
print(f"La cadena invertida es: {invertida}")

# 6. Contar la frecuencia de cada elemento en una lista
# Se utiliza un diccionario para almacenar la frecuencia de cada elemento mientras se itera sobre la lista.
colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo"]
frecuencia = {}
for color in colores:
    if color in frecuencia:
        frecuencia[color] += 1
    else:
        frecuencia[color] = 1
print(f"Frecuencia de los colores: {frecuencia}")

# 7. Verificar si un elemento existe en una tupla
# Se utiliza el operador 'in' para comprobar de manera concisa la existencia de un elemento.
mi_tupla = (10, 20, 30, 40, 50)
elemento_a_buscar = 35
if elemento_a_buscar in mi_tupla:
    print(f"{elemento_a_buscar} existe en la tupla.")
else:
    print(f"{elemento_a_buscar} no existe en la tupla.")

# 8. Crear una lista de números pares dentro de un rango
# Se utiliza un bucle 'for' y un condicional 'if' para seleccionar solo los números pares dentro del rango.
numeros_pares = []
for i in range(1, 11):
    if i % 2 == 0:
        numeros_pares.append(i)
print(f"Lista de números pares del 1 al 10: {numeros_pares}")

# 9. Simular un contador regresivo
# Un bucle 'while' se ejecuta mientras una condición (contador > 0) sea verdadera, decrementando el contador en cada iteración.
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("¡Despegue!")

# 10. Combinar dos listas y eliminar duplicados
# Se combinan las listas usando el operador '+' y luego se convierte a un conjunto ('set') para eliminar duplicados,
# volviendo a convertirlo a una lista al final.
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 5, 6, 7, 8]
combinada = lista1 + lista2
sin_duplicados = list(set(combinada))
print(f"Lista combinada sin duplicados: {sin_duplicados}")