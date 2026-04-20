# 🔐 Sistema de Login con Menú (Versión Simplificada)

## 📌 Introducción

Este programa implementa:

* Un sistema de **inicio de sesión con validación**
* Un límite de **3 intentos**
* Un menú interactivo con opciones básicas

---

# 🔑 Sistema de Login

## 🔁 Control de intentos

```python
intentos = 0

while intentos < 3:
```

* Se inicia el contador en 0
* El usuario tiene máximo **3 intentos**

---

## 👤 Entrada de datos

```python
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
```

Se solicitan las credenciales.

---

## ⚠️ Validaciones del usuario

### ❌ Usuario vacío

```python
if usuario == "":
```

👉 Evita que el usuario deje el campo vacío

---

### 🔤 Usuario válido

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

### 🔎 Verificación de contenido

```python
tiene_letra = False
tiene_numero = False

for elemento in contraseña:
```

👉 Recorre cada carácter de la contraseña

---

```python
if elemento.isalpha():
    tiene_letra = True
```

👉 Detecta letras

---

```python
if elemento.isdigit():
    tiene_numero = True
```

👉 Detecta números

---

### ❌ Validación final

```python
if not tiene_letra or not tiene_numero:
```

👉 La contraseña debe tener **al menos una letra y un número**

---

## ✅ Acceso correcto

```python
if usuario == "admin" and contraseña == "Admin2026":
```

👉 Permite el acceso al sistema

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

  * Si es positivo, negativo o cero
  * Si es par o impar

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

👉 Determina el signo

---

```python
if numero % 2 == 0:
```

👉 Determina si es par

---

### 🔁 Repetición

Permite repetir el proceso hasta que el usuario lo decida.

---

## 2️⃣ Categoría de edad

### 🔍 ¿Qué hace?

Clasifica al usuario según su edad y muestra permisos.

---

### 📊 Clasificación

* Niño → 0 a 12
* Adolescente → 13 a 17
* Adulto → 18 a 64
* Adulto mayor → 65+

---

### ⚠️ Error lógico importante

```python
if edad >= 13:
```

👉 Esta condición hace que la siguiente nunca se cumpla correctamente:

```python
elif edad >= 13 and edad < 18:
```

---

### 🚗 Permisos

* Registro
* Compra con tutor
* Conducir
* Servicio VIP

---

## 3️⃣ Calcular tarifa

```python
elif opcion == "3":
    print("Calcular tarifa.")
```

👉 En esta versión solo muestra el texto (no tiene lógica implementada)

---

# 🔓 Opciones del menú

## 🔴 Cerrar sesión

```python
acceso = 0
```

👉 Regresa al login

---

## 🚪 Salir del sistema

```python
intentos = 4
```

👉 Fuerza la salida del programa

---

## ❌ Opción inválida

```python
else:
    print("Opción no válida.")
```

👉 Maneja errores del usuario

---

# 🚫 Acceso incorrecto

```python
else:
    print("Credenciales incorrectas.")
    intentos += 1
```

👉 Aumenta el contador de intentos

---

# 🧾 Mensajes finales

```python
if intentos == 3:
```

👉 Bloquea el sistema

```python
elif intentos == 4:
```

👉 Indica salida del sistema

---

# 🧠 Conclusión

Este programa demuestra:

* Validación de usuario y contraseña
* Uso de ciclos (`while`)
* Uso de condiciones (`if`)
* Creación de menús interactivos

---

# ⚠️ Observaciones

* El módulo de tarifa no está implementado
* Hay un pequeño error lógico en la validación de edad
* El código puede organizarse mejor usando funciones

---
