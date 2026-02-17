# Creación y uso de un entorno virtual en Python con Visual Studio Code

Un entorno virtual en Python permite aislar las librerías de cada proyecto, evitando conflictos entre versiones y manteniendo un entorno de trabajo limpio y organizado.

A continuación, se presenta la secuencia completa de pasos (1 al 9) para crear, activar y utilizar un entorno virtual (env) en Visual Studio Code.

---

## 1. Abrir el proyecto en Visual Studio Code

1. Abrir Visual Studio Code.  
2. Ir a File → Open Folder.  
3. Seleccionar la carpeta del proyecto.

Es importante que el entorno virtual se cree dentro de la carpeta del proyecto para que Visual Studio Code lo detecte correctamente.

---

## 2. Abrir la terminal integrada de Visual Studio Code

1. Presionar Ctrl + `  
2. O ir a Terminal → New Terminal

La terminal integrada se abrirá directamente en la carpeta del proyecto.

---

## 3. Crear el entorno virtual

El entorno virtual se crea utilizando el módulo venv, que viene incluido con Python.

python -m venv env

Este comando creará una carpeta llamada env que contendrá todos los archivos del entorno virtual.

---

## 4. Activar el entorno virtual

Para activar el entorno virtual en la terminal de Visual Studio Code, usar el siguiente comando:

env\Scripts\activate

En caso de error por permisos:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Cuando el entorno se activa correctamente, la terminal mostrará algo como:

(env)

---

## 5. Seleccionar el intérprete de Python en Visual Studio Code

Para asegurarse de que VS Code utilice el Python del entorno virtual:

1. Presionar Ctrl + Shift + P  
2. Escribir: Python: Select Interpreter  
3. Seleccionar el intérprete que incluya (env)

Esto garantiza que el editor ejecute el código usando el entorno virtual.

---

## 6. Instalar una librería dentro del entorno virtual

Con el entorno virtual activo, se pueden instalar librerías usando pip.

Ejemplo: instalación de la librería NumPy:

pip install numpy

La librería se instalará únicamente dentro del entorno virtual.

---

## 7. Importar la librería en un archivo Python

Después de instalar la librería, se puede utilizar dentro de un archivo .py:

import numpy

---
env/

