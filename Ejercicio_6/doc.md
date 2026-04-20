# 💰 Cálculo de Tarifa con Descuentos - Explicación del Código

## 📌 Introducción

Este fragmento de código calcula el precio final de una tarifa considerando:

* Edad del usuario
* Día de la semana
* Si es estudiante
* Si es miembro
* Método de pago

Además, aplica descuentos acumulativos con un límite máximo.

---

# 💵 Precio base

```python
tarifa_base = 200
```

👉 Se define el costo inicial del servicio.

---

# 📥 Entrada de datos

```python
edad = int(input("Ingresa tu edad (0 a 120): "))
dia = int(input("Día de la semana (1=lunes ...7=domingo): "))
estudiante = input("¿Eres estudiante? (s/n): ").lower()
miembro = input("¿Eres miembro? (s/n): ").lower()
metodo = input("Método de pago E(efectivo) T(tarjeta): ").lower()
```

Se solicitan datos al usuario:

* Edad → número entero
* Día → número del 1 al 7
* Estudiante → "s" o "n"
* Miembro → "s" o "n"
* Método → "e" o "t"

👉 `.lower()` asegura que no importe si el usuario usa mayúsculas o minúsculas.

---

# 🧮 Variables de control

```python
descuento = 0
recargo = 0
```

* `descuento` → porcentaje acumulado
* `recargo` → porcentaje extra

---

# 📅 Recargo por fin de semana

```python
if dia == 6 or dia == 7:
    recargo = 0.10
```

👉 Si es sábado o domingo, se agrega un **10% extra**

---

# 🎯 Descuento por edad

```python
if edad <= 12:
    descuento += 0.50
elif edad <= 17:
    descuento += 0.20
elif edad >= 65:
    descuento += 0.30
```

* Niños → 50%
* Adolescentes → 20%
* Adultos mayores → 30%

---

# 🎓 Descuento por estudiante

```python
if estudiante == "s" and edad >= 13:
    descuento += 0.15
```

👉 Aplica solo si:

* Es estudiante
* Tiene 13 años o más

---

# 🧾 Descuento por miembro

```python
if miembro == "s":
    descuento += 0.10
```

👉 Aplica un 10% adicional

---

# 💳 Descuento por método de pago

```python
if metodo == "e":
    descuento += 0.05
```

👉 Si paga en efectivo → 5% de descuento

---

# ⚠️ Límite de descuento

```python
if descuento > 0.60:
    descuento = 0.60
```

👉 El descuento máximo permitido es **60%**

---

# 🧮 Cálculo final

```python
tarifa_final = tarifa_base * (1 - descuento) * (1 + recargo)
```

👉 Fórmula:

* Primero se aplica el descuento
* Luego se suma el recargo

---

# 🖨️ Resultado

```python
print(f"La tarifa final es: {tarifa_final:.2f}")
```

👉 Muestra el resultado con **2 decimales**

---

# 🧠 Conclusión

Este código demuestra:

* Uso de condiciones (`if`, `elif`)
* Manejo de porcentajes
* Validación básica de entradas
* Aplicación de múltiples descuentos acumulativos

---

# ⚠️ Observaciones

* No valida si los datos ingresados son incorrectos (puede fallar con texto)
* El cálculo está bien optimizado y más limpio que versiones anteriores
* Usa una fórmula más elegante para calcular el total

---


while intentos < 3:
```

* Permite máximo **3 intentos**
* Si se excede, el sistema se bloquea

---

## 👤 Entrada de datos

```python
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
```

Se solicitan credenciales al usuario.

---

## ⚠️ Validaciones del usuario

### ❌ Usuario vacío

```python
if usuario == "":
```

👉 Evita que el usuario esté en blanco

---

### 🔤 Usuario alfanumérico

```python
if not usuario.isalnum():
```

👉 Solo permite letras y números (sin espacios)

---

## 🔒 Validaciones de contraseña

### 📏 Longitud mínima

```python
if len(contraseña) < 8:
```

👉 Debe tener al menos 8 caracteres

---

### 🔎 Contenido (letras y números)

```python
for elemento in contraseña:
    if elemento.isalpha():
    if elemento.isdigit():
```

👉 Verifica que tenga:

* Al menos una letra
* Al menos un número

---

### ❌ Validación final

```python
if not tiene_letra or not tiene_numero:
```

👉 Si no cumple, se rechaza

---

## ✅ Acceso correcto

```python
if usuario == "admin" and contraseña == "Admin2026":
```

👉 Permite entrar al sistema

---

# 📋 Menú principal

```python
while acceso == 1:
```

Se muestra un menú con opciones:

1. Clasificar número
2. Categoría de edad
3. Calcular tarifa
4. Cerrar sesión
5. Salir

---

# 🔧 Funcionalidades

---

## 1️⃣ Clasificar número

### 🔍 ¿Qué hace?

* Pide un número
* Determina:

  * Positivo / negativo / cero
  * Par / impar

---

### 🔎 Validación

```python
numero.lstrip("-").isdigit()
```

👉 Permite números negativos correctamente

---

### 📊 Clasificación

```python
if numero > 0:
elif numero < 0:
```

```python
if numero % 2 == 0:
```

👉 Usa módulo para detectar pares/impares

---

### 🔁 Repetición

Permite repetir el proceso hasta que el usuario diga que no

---

## 2️⃣ Categoría de edad

### 🔍 ¿Qué hace?

Clasifica a la persona según edad y permisos.

---

### 📊 Clasificación

* Niño → 0 a 12
* Adolescente → 13 a 17
* Adulto → 18 a 64
* Adulto mayor → 65+

---

### ⚠️ Detalle importante

```python
if edad >= 13:
```

👉 Hace que la condición siguiente nunca se cumpla correctamente (error lógico)

---

### 🚗 Permisos

* Registro
* Compra con tutor
* Conducir
* Acceso VIP

---

## 3️⃣ Calcular tarifa

### 🔍 ¿Qué hace?

Calcula el costo final considerando:

* Edad
* Día
* Estudiante
* Miembro
* Método de pago

---

### 💰 Precio base

```python
precio_base = 200
```

---

### 📅 Recargo

```python
if dia == 6 or dia == 7:
```

👉 10% extra en fin de semana

---

### 🎯 Descuentos

* Edad:

  * Niño → 50%
  * Adolescente → 20%
  * Adulto mayor → 30%

* Otros:

  * Estudiante → 15%
  * Miembro → 10%
  * Efectivo → 5%

---

### ⚠️ Límite

```python
if porcentaje_descuento > 60:
```

👉 Máximo 60% de descuento

---

### 🧾 Resultado

Se muestran:

* Precio base
* Recargo
* Descuento
* Total final

---

# 🔓 Opciones del menú

## 🔴 Cerrar sesión

```python
acceso = 0
```

👉 Regresa al login

---

## 🚪 Salir

```python
intentos = 4
```

👉 Termina todo el sistema

---

## ❌ Opción inválida

```python
else:
    print("Opción no válida")
```

---

# 🧠 Conclusión

Este programa demuestra:

* Validación de datos de entrada
* Uso de ciclos (`while`)
* Uso de condiciones (`if`)
* Manejo de menús interactivos
* Lógica estructurada en un solo flujo

---

# ⚠️ Observaciones

* Algunas condiciones pueden mejorarse
* Falta validación en entradas numéricas (`int(input())`)
* El código podría separarse en funciones para mayor orden

---

