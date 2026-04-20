# 🧠 Programa de Ejercicios en Python - Explicación del Código

## 📌 Introducción

Este programa es un conjunto de **13 ejercicios básicos en Python**, organizados en funciones.
El usuario puede elegir cuál ejecutar mediante un menú interactivo.

---

## 📦 Importaciones

```python
from unittest import case
```

👉 Esta línea realmente **no es necesaria** en el programa.
El `case` que usas después pertenece a `match`, no a `unittest`.

---

## 🧩 Estructura general

El programa está dividido en:

* Funciones → cada una hace un ejercicio
* Un menú (`while True`)
* Un `match-case` → para seleccionar la opción

---

# 🔧 Funciones

## 1️⃣ Función `palabra()`

```python
def palabra():
```

* Pide una palabra
* La imprime **10 veces** usando un `for`

```python
for i in range(0, 10):
```

👉 Repite del 0 al 9 (10 veces)

---

## 2️⃣ Función `edad()`

```python
edad = int(input(...))
```

* Convierte la entrada a entero

```python
for k in range (0, edad + 1):
```

👉 Imprime desde 0 hasta la edad

* Usa `try-except` para evitar errores si no es número

---

## 3️⃣ Función `impares()`

* Pide un número positivo
* Recorre desde 0 hasta ese número
* Usa:

```python
if i % 2 != 0:
```

👉 Detecta números impares

* Guarda el resultado en un string

---

## 4️⃣ Función `cuenta_atras()`

```python
for i in range(numero, -1, -1):
```

👉 Cuenta desde el número hasta 0

* Paso `-1` → va hacia atrás

---

## 5️⃣ Función `capital_obtenido()`

* Calcula interés compuesto

```python
capital += capital * (tasa / 100)
```

👉 Aumenta el capital cada año

* Usa `for` para simular los años

---

## 6️⃣ Función `triangulo_rectangulo()`

```python
print("*" * i)
```

👉 Imprime un triángulo con asteriscos

Ejemplo:

```
*
**
***
```

---

## 7️⃣ Función `tabla_multiplicar()`

* Dos `for` anidados:

```python
for i in range(1,11):
    for j in range(1,11):
```

👉 Genera todas las multiplicaciones del 1 al 10

---

## 8️⃣ Función `piramide_numeros()`

* Crea una pirámide de números

```python
for j in range(2*i - 1, 0, -2):
```

👉 Genera números impares descendentes

---

## 9️⃣ Función `contraseña()`

* Pide una contraseña
* Usa `while` hasta que coincidan

```python
while contraseña != ingresar_contraseña:
```

👉 Se repite hasta que sea correcta

---

## 🔟 Función `numero_primo()`

* Verifica si un número es primo

```python
for i in range(2, int(num**0.5) + 1):
```

👉 Solo revisa hasta la raíz del número (optimización)

---

## 1️⃣1️⃣ Función `palabra_alrevez()`

* Invierte una palabra manualmente

```python
for i in range(len(palabra) -1, -1, -1):
```

👉 Recorre la palabra al revés

---

## 1️⃣2️⃣ Función `frase_letra()`

* Cuenta cuántas veces aparece una letra

```python
if frase[i] == letra:
```

👉 Compara cada carácter

---

## 1️⃣3️⃣ Función `eco()`

* Repite lo que el usuario escribe

```python
while True:
```

👉 Ciclo infinito hasta escribir `"salir"`

---

# 🖥️ Menú principal

```python
while True:
```

👉 Mantiene el programa corriendo siempre

---

## 📋 Opciones

Se muestran todos los ejercicios:

```python
print("Ejercicio 1: ...")
```

---

## 🎯 Selección con `match-case`

```python
match opcion:
```

👉 Funciona como un `switch`

Ejemplo:

```python
case "1":
    palabra()
```

* Ejecuta la función correspondiente

---

## 🚪 Salida del programa

```python
case "14":
    break
```

👉 Termina el ciclo y el programa

---

## ❌ Opción inválida

```python
case _:
```

👉 Captura cualquier opción incorrecta

---

# 🧠 Conclusión

Este programa:

* Practica estructuras básicas de Python:

  * `for`
  * `while`
  * `if`
  * `match-case`
* Usa funciones para organizar el código
* Permite interacción con el usuario

---

# ⚠️ Detalles importantes

* `from unittest import case` no es necesario
* Se recomienda validar mejor entradas en algunos ejercicios
* Algunas funciones podrían optimizarse

---

