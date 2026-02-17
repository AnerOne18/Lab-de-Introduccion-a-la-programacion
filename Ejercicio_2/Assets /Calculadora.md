## Explicación del código

La primera línea del programa define una función llamada `convertir_base`, la cual recibe dos argumentos: `numero`, que representa el valor que se desea transformar, y `base`, que indica el sistema de numeración al que se quiere convertir. En este caso, se trabajan las bases 2, 8 y 16, que corresponden a los sistemas binario, octal y hexadecimal.

Dentro de la función, se utiliza una estructura condicional `if` para comprobar si el valor de `numero` es igual a cero. Si se cumple esta condición, la función retorna directamente el valor "0", lo que permite evitar problemas en el proceso de conversión.

Posteriormente, se define una cadena llamada `digitos`, la cual contiene los caracteres que se usarán para representar los valores resultantes. Esta cadena es especialmente importante para el sistema hexadecimal, ya que incluye las letras de la A a la F para representar los números del 10 al 15.

Después se inicializa la variable `resultado`, que servirá para ir almacenando el número convertido conforme avanza el proceso.

El ciclo `while` se encarga de

