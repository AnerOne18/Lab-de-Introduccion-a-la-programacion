# 🔐 Login Streamlit App - Explicación del Código

## 📌 Introducción

Este programa es una aplicación web creada con **Streamlit**, la cual implementa un sistema de inicio de sesión (login) y un menú visual con tarjetas que contienen diferentes opciones.

---

## 📦 Importaciones

```python
import streamlit as st
import base64
```

* `streamlit`: permite crear interfaces web de forma sencilla con Python.
* `base64`: se utiliza para convertir imágenes a texto codificado y poder usarlas dentro del HTML/CSS.

---

## 🧱 Clase principal

```python
class LoginStreamlitApp:
```

Se define una clase que contiene toda la lógica del programa, esto ayuda a mantener el código organizado.

---

## ⚙️ Constructor (`__init__`)

```python
def __init__(self) -> None:
    self.usuario_correcto = "admin"
    self.contrasena_correcta = "Admin2026"
```

Aquí se definen las credenciales correctas para el login.

```python
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
```

* `session_state` guarda información mientras la app está activa.
* Se usa para saber si el usuario ya inició sesión o no.

---

## 🖼️ Función `get_base64`

```python
def get_base64(self, file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
```

Esta función:

1. Abre una imagen en modo binario (`rb`)
2. La convierte a base64
3. La devuelve como texto

👉 Esto permite insertar imágenes directamente en el diseño usando CSS.

---

## 🚀 Función principal `ejecutar`

```python
def ejecutar(self) -> None:
```

Es la función que arranca toda la aplicación.

---

### 🎨 Configuración de la página

```python
st.set_page_config(page_title="Login Streamlit", page_icon="🔐", layout="wide")
```

* Define el título de la pestaña
* Define el icono
* Usa un layout ancho

---

### 🌌 Fondo de pantalla

```python
bg = self.get_base64("fondo.jpg")
```

Se obtiene la imagen del fondo en base64.

```python
background-image: url("data:image/jpg;base64,{bg}");
```

Esto permite poner la imagen como fondo de toda la aplicación.

---

### 🎭 Estilos CSS

Se usa `st.markdown` con HTML para definir estilos personalizados:

* `.card`: diseño de tarjetas
* `.card:hover`: animación al pasar el mouse
* `.card-img`: imagen dentro de la tarjeta
* `.card-body`: contenido
* `.card-title`: título

👉 Esto hace que la app se vea más moderna.

---

## 🔀 Lógica de navegación

```python
if st.session_state.autenticado:
    self.mostrar_menu()
else:
    self.mostrar_login()
```

* Si el usuario ya inició sesión → muestra el menú
* Si no → muestra el login

---

## 🔐 Función `mostrar_login`

```python
st.title("🔐 Login")
```

Muestra el título.

```python
with st.form("form_login"):
```

Crea un formulario.

```python
usuario = st.text_input("Usuario")
contrasena = st.text_input("Contraseña", type="password")
```

* Campo de usuario
* Campo de contraseña (oculta)

```python
if enviar:
```

Cuando se presiona el botón:

* Compara los datos ingresados con los correctos

* Si coinciden:

  ```python
  st.session_state.autenticado = True
  st.rerun()
  ```

  👉 Guarda la sesión y recarga la app

* Si no:

  ```python
  st.error("Credenciales incorrectas")
  ```

---

## 📋 Función `mostrar_menu`

### 🔴 Botón de cerrar sesión

```python
if st.button("❌"):
```

* Cambia el estado a `False`
* Regresa al login

---

### 📌 Título

```python
st.title("🌌 Menú del sistema")
```

---

### 🧩 Columnas

```python
col1, col2, col3 = st.columns(3)
```

Divide la pantalla en 3 secciones.

---

### 🪐 Tarjeta 1: Clasificar número

```python
planeta = self.get_base64("planeta.png")
```

Carga la imagen.

```html
<div class="card">
```

Muestra una tarjeta con:

* Imagen
* Título

---

### 🕳️ Tarjeta 2: Categoría de edad

Funciona igual que la anterior, pero con otra imagen.

---

### ✨ Tarjeta 3: Calcular tarifa

Mismo funcionamiento con diferente contenido.

---

## ▶️ Ejecución del programa

```python
app = LoginStreamlitApp()
app.ejecutar()
```

* Se crea una instancia de la clase
* Se ejecuta la aplicación

---

## ⚠️ Consideraciones importantes

Para que funcione correctamente, deben existir estos archivos:

* `fondo.jpg`
* `planeta.png`
* `agujero.jpg`
* `cuasar.jpg`

---

## 🧠 Conclusión

Este programa:

* Implementa un sistema de login básico
* Usa sesiones para mantener el estado del usuario
* Aplica estilos personalizados con CSS
* Utiliza imágenes en base64 para mejorar la interfaz

---
