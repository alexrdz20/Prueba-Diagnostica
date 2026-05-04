# Guía de Estudio: Problemas de Lenguajes y Compiladores

Esta guía está diseñada para explicar paso a paso la lógica detrás de los tres problemas desarrollados para la asignatura. Aquí encontrarás el razonamiento matemático, las estructuras de datos y el flujo de los algoritmos de forma clara y didáctica.

---

## 📘 Problema 1: Polinomio $(x+1)^n$ usando Triángulo de Pascal
**Lenguajes implementados:** Java y Python

### 🎯 Objetivo
Calcular y evaluar un binomio elevado a una potencia $n$, utilizando el Triángulo de Pascal para obtener los coeficientes en lugar de fórmulas factoriales tradicionales.

### 🧠 Lógica Paso a Paso

1. **El Problema del Desbordamiento (Overflow):**
   Al calcular el Triángulo de Pascal hasta la fila $n=100$, los números se vuelven gigantescos. 
   - En **Python** esto se maneja automáticamente ya que soporta precisión arbitraria.
   - En **Java** los tipos nativos como `int` o `long` no son suficientes, por lo que se utiliza la clase `BigInteger`.

2. **Generación del Triángulo de Pascal:**
   Se utiliza una lista dinámica (`ArrayList` en Java o `list` en Python). 
   - Comienzas con la fila `[1]`.
   - Para generar la siguiente, colocas un `1` al principio, luego sumas los elementos adyacentes de la fila anterior, y cierras con otro `1`.
   - Esto se repite dentro de un ciclo hasta alcanzar la fila $n$.

3. **Construcción y Formateo del Polinomio:**
   Sabiendo que los coeficientes vienen del triángulo, la potencia más alta ($n$) se le asigna al primer término y va disminuyendo hasta $0$.
   - Se crea un texto iterando por la fila: si el coeficiente no es 1, se imprime; luego la variable `x` y su potencia. Ejemplo: `10x^3 + 5x^2...`

4. **Evaluación (Cálculo Final):**
   Con un ciclo se recorre la fila, obteniendo el coeficiente y la potencia de ese turno.
   - Se calcula el valor del término como: `Coeficiente * (x^potencia)`
   - Se acumula ese resultado en una variable total.
   - Todo este desglose y el resultado final se escriben dinámicamente en los archivos `.txt`.

---

## ♟️ Problema 2: Validador de Notación FEN
**Lenguaje implementado:** Python

### 🎯 Objetivo
Verificar si una cadena de texto (string) representa una configuración válida en ajedrez utilizando el estándar FEN (Forsyth-Edwards Notation).

### 🧠 Lógica Paso a Paso

El FEN divide la información en **6 campos**, separados por espacios. El código divide la cadena usando `split(' ')` y verifica uno a uno:

1. **Campo 1: Ubicación de las Piezas (`placement`)**
   - Se separa por `/` para obtener las 8 filas del tablero.
   - Se verifica que cada fila sume exactamente **8 casillas**.
   - Los números representan casillas vacías y las letras (p, n, b, r, q, k) las piezas. Cualquier otro carácter vuelve la cadena inválida.

2. **Campo 2: Turno Activo (`color`)**
   - Solo puede ser `"w"` (White / Blancas) o `"b"` (Black / Negras).

3. **Campo 3: Enroque (`castling`)**
   - Puede ser un guion `"-"` si no hay enroque disponible.
   - Si no es guion, se usa una expresión regular (`[KQkq]+`) para verificar que solo se incluyan letras permitidas y sin repetirse.

4. **Campo 4: Captura al paso (`en_passant`)**
   - Puede ser `"-"`.
   - Si hay casilla destino, debe coincidir con el formato de tablero: una letra `a-h` seguida por un número `3` o `6` (que son las filas donde esto puede ocurrir lógicamente).

5. **Campo 5: Reloj de Medio Movimiento (`halfmove`)**
   - Debe ser únicamente un dígito numérico mayor o igual a 0.

6. **Campo 6: Número de Movimiento Completo (`fullmove`)**
   - Debe ser un dígito entero, pero debe ser **mayor estricto a 0**.

---

## 🗣️ Problema 3: Traductor de Palabras Reservadas
**Lenguaje implementado:** C

### 🎯 Objetivo
Cargar en la memoria un archivo fuente escrito en lenguaje C y traducir **únicamente** las palabras reservadas al español, ignorando todo lo que esté dentro de strings `" "` o comentarios `//` y `/* */`.

### 🧠 Lógica Paso a Paso

1. **Manejo Dinámico de Memoria (`malloc`):**
   - Primero se abre el archivo en modo binario y se desplaza el puntero hasta el final (`fseek`) para saber exactamente de qué tamaño (en bytes) es el archivo.
   - Se reserva en la memoria dinámica un bloque exacto de ese tamaño y se carga todo el archivo.

2. **El Diccionario de Traducción:**
   - Se crea una estructura (`struct`) que asocia la palabra en inglés con la de español (ej. `{"while", "mientras"}`). Esto actúa como una pequeña tabla de búsqueda.

3. **La Máquina de Estados (El escáner de caracteres):**
   Esta es la parte más importante. El código lee carácter por carácter e identifica "en qué estado" está utilizando *banderas* (variables booleanas/enteras 0 o 1):
   - **`en_string`**: ¿El carácter actual está dentro de comillas `""`?
   - **`en_comentario_linea`**: ¿El código encontró un `//`? (Se reinicia con un salto de línea `\n`).
   - **`en_comentario_bloque`**: ¿El código encontró un `/*`? (Se reinicia al encontrar `*/`).

4. **Análisis Léxico:**
   - Si el carácter **no** está en un string ni en un comentario, el código asume que puede ser código C real.
   - Si el carácter es alfanumérico (una letra, un número, o `_`), lo guarda en un arreglo temporal `temporal[]`. Todavía no lo imprime, porque está "formando" una palabra.
   - En el instante en que detecta algo que **no es letra ni número** (un espacio, un paréntesis, un punto y coma):
     1. Toma la palabra armada en `temporal`.
     2. Llama a `buscar_traduccion()` para ver si es reservada. Si lo es, imprime la traducción en español; si no, imprime la variable original.
     3. Imprime el símbolo (el espacio o el paréntesis) que causó el corte.
     4. Vacía la variable `temporal` para la siguiente palabra.
