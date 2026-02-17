## Explicación del código

La primera línea del programa define una función llamada `convertir_base`, la cual recibe dos argumentos: `numero`, que representa el valor que se desea transformar, y `base`, que indica el sistema de numeración al que se quiere convertir. En este caso, se trabajan las bases 2, 8 y 16, que corresponden a los sistemas binario, octal y hexadecimal.

Dentro de la función, se utiliza una estructura condicional `if` para comprobar si el valor de `numero` es igual a cero. Si se cumple esta condición, la función retorna directamente el valor "0", lo que permite evitar problemas en el proceso de conversión.

Posteriormente, se define una cadena llamada `digitos`, la cual contiene los caracteres que se usarán para representar los valores resultantes. Esta cadena es especialmente importante para el sistema hexadecimal, ya que incluye las letras de la A a la F para representar los números del 10 al 15.

Después se inicializa la variable `resultado`, que servirá para ir almacenando el número convertido conforme avanza el proceso.

El ciclo `while` se encarga de repetir las operaciones mientras el valor de `numero` sea mayor que cero. Dentro de este ciclo se calcula la variable `residuo`, que obtiene el resto de dividir el número entre la base. Dicho residuo se utiliza como índice para seleccionar el carácter correspondiente dentro de la cadena `digitos`, el cual se agrega al inicio de la variable `resultado`.

A continuación, el valor de `numero` se actualiza mediante una división entera entre la base, permitiendo continuar con las siguientes iteraciones hasta que el número sea igual a cero y el ciclo finalice.

Más adelante, el programa solicita un valor al usuario utilizando la función `input`, el cual se recibe inicialmente como una cadena de texto. Este valor puede representar un número entero, un número decimal o incluso un valor lógico.

Mediante una estructura condicional, si el usuario ingresa "true", se asigna el valor entero 1 a la variable `numero`. De manera similar, si se ingresa "false", se asigna el valor 0.

En caso contrario, se utiliza una estructura `else` junto con un bloque `try-except`. Dentro del bloque `try`, se verifica si el valor contiene un punto decimal; si es así, se convierte primero a tipo `float` y luego a entero usando `int(float(valor))`, eliminando la parte decimal. Si no contiene punto, se convierte directamente a entero con `int(valor)`.

Si ocurre algún error durante estas conversiones, como cuando se ingresa un texto que no es numérico, se ejecuta el bloque `except`, mostrando un mensaje de error y terminando la ejecución del programa.

Finalmente, se muestran los resultados en pantalla utilizando la función `print`, donde se llama a la función `convertir_base` con el número ingresado y las bases 2, 8 y 16, obteniendo así su representación en binario, octal y hexadecimal, además de mostrar su valor en el sistema decimal.
