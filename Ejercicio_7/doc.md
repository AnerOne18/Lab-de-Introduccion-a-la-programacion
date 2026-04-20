# 🔐 Sistema con Login y Menú en Python - Explicación del Código

## 📌 Introducción

Este programa implementa:

* Un sistema de **login con validación**
* Un menú interactivo
* Tres funcionalidades principales:

  * Clasificar números
  * Determinar categoría de edad
  * Calcular tarifas con descuentos

---

# 🔧 Funciones del sistema

---

## 1️⃣ Función `clasificar_numero()`

```python id="c1a8zx"
def clasificar_numero():
```

### 🔍 ¿Qué hace?

Permite al usuario ingresar un número y determina:

* Si es positivo, negativo o cero
* Si es par o impar
* Permite repetir el proceso

---

### 🔄 Control del ciclo

```python id="k5l0s1"
while clasificar == 0:
```

👉 Mantiene el programa activo hasta que el usuario decida salir

---

### ✅ Validación de número

```python id="s9p2df"
numero.lstrip("-").isdigit()
```

👉 Permite números negativos y asegura que sea entero

---

### 📊 Clasificación

* Positivo / negativo / cero
* Par / impar usando:

```python id="4q7hda"
numero % 2
```

---

### 🔁 Repetición

Pregunta al usuario si desea continuar:

```python id="n3x8pt"
¿Desea clasificar otro numero? (s/n)
```

---

## 2️⃣ Función `categoria_edad()`

```python id="b8k3wv"
def categoria_edad():
```

### 🔍 ¿Qué hace?

Clasifica al usuario según su edad y determina permisos.

---

### 📊 Clasificación por edad

* Niño: 0 - 12
* Adolescente: 13 - 17
* Adulto: 18 - 64
* Adulto mayor: 65+

---

### ⚠️ Detalle importante

```python id="x7m2qp"
elif edad >= 13:
```

👉 Esta condición hace que la siguiente (`elif edad >= 13 and edad < 18`) nunca se ejecute correctamente.

---

### 🚗 Permisos

* Registro
* Compra con tutor
* Conducir
* Servicio VIP

---

## 3️⃣ Función `calcular_tarifa()`

```python id="f3w8qz"
def calcular_tarifa():
```

### 🔍 ¿Qué hace?

Calcula el precio final basado en:

* Edad
* Día de la semana
* Si es estudiante
* Si es miembro
* Método de pago

---

### 💰 Precio base

```python id="u1y9kq"
precio_base = 200
```

---

### 📅 Recargo por fin de semana

```python id="j4r7nx"
if dia == 6 or dia == 7:
```

👉 Aplica un 10% extra

---

### 🎯 Descuentos

#### Por edad:

* Niño → 50%
* Adolescente → 20%
* Adulto mayor → 30%

#### Otros:

* Estudiante → 15%
* Miembro → 10%
* Pago en efectivo → 5%

---

### ⚠️ Límite de descuento

```python id="p6m1sz"
if porcentaje_descuento > 60:
```

👉 Máximo 60% de descuento

---

### 🧾 Resultado final

Muestra:

* Precio base
* Recargo
* Descuento aplicado
* Total final

---

# 🔐 Sistema de Login

---

## 🔁 Intentos

```python id="t8q4ny"
intentos = 0
while intentos < 3:
```

👉 Máximo 3 intentos

---

## 👤 Validación de usuario

* No puede estar vacío
* Debe ser alfanumérico

```python id="r2v6cb"
usuario.isalnum()
```

---

## 🔑 Validación de contraseña

* Mínimo 8 caracteres
* Debe contener:

  * Letras
  * Números

```python id="m5d9az"
elemento.isalpha()
elemento.isdigit()
```

---

## ✅ Acceso correcto

```python id="z1k8qf"
if usuario == "admin" and contraseña == "Admin2026":
```

👉 Permite entrar al sistema

---

# 📋 Menú principal

```python id="g7n2ls"
while acceso == 1:
```

Opciones:

1. Clasificar número
2. Categoría de edad
3. Calcular tarifa
4. Cerrar sesión
5. Salir

---

## 🎯 Selección con `match`

```python id="y3p9jt"
match opcion:
```

👉 Ejecuta la función correspondiente

---

## 🔓 Cerrar sesión

```python id="d4x7kv"
acceso = 0
```

---

## 🚪 Salir del sistema

```python id="w6q2mn"
intentos = 4
```

👉 Rompe el ciclo principal

---

# ⚠️ Errores y detalles importantes

* Algunas condiciones están mal ordenadas (`elif edad >= 13`)
* No valida correctamente ciertos inputs (puede romperse si ingresan texto)
* El sistema es funcional pero mejorable

---

# 🧠 Conclusión

Este programa demuestra:

* Uso de funciones
* Validación de datos
* Estructuras de control (`if`, `while`, `for`)
* Uso de `match-case`
* Implementación de un sistema básico de login

---

