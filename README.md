# Proyecto de Redes y Compiladores

Este repositorio contiene la resolución de los problemas planteados para la asignatura. Todos los programas cuentan con **interactividad**, **validación de datos** y **valores por defecto**.

## Estructura del Proyecto
- **Problema1/**: Expansión polinómica (Triángulo de Pascal) en Python y Java.
- **Problema2/**: Validador de notación FEN para ajedrez (Python).
- **Problema3/**: Traductor de palabras reservadas del lenguaje C (C).
- **Defensa/**: Contiene el material o referencia para la defensa.

## Enlace a la Defensa
[Insertar aquí el enlace a tu video de la defensa]

---

## Problema 1: Triángulo de Pascal y Expansión Polinómica
Este programa calcula los coeficientes de la expansión polinómica de $(x+1)^n$.

- **Interactividad:** El programa solicitará los valores de `n` (grado) y `x`. Si presionas **Enter** sin escribir, usará `n=100` y `x=2`.
- **Ejecución:**
  - **Python:** `python Problema1/solucion.py`
  - **Java:** 
    1. Compilar: `javac Problema1/Solucion.java`
    2. Ejecutar: `java -cp Problema1 Solucion`
- **Resultados:** Los archivos `.txt` se generan automáticamente dentro de la carpeta `Problema1/`.

## Problema 2: Validación de notación FEN
Valida si una cadena de texto sigue la notación Forsyth-Edwards de ajedrez mediante un bucle interactivo.

- **Interactividad:** Permite elegir entre importar la cadena FEN desde un archivo de código externo (`datos_fen.py`) o ingresarla manualmente por teclado.
- **Ejecución:** `python Problema2/fen_validator.py`

## Problema 3: Traductor de palabras reservadas de C
Analizador léxico que traduce palabras reservadas de C al español cargando el archivo dinámicamente en memoria.

- **Interactividad:** Al iniciar, presenta un menú para elegir entre:
  1. Ingresar nombre de archivo manualmente.
  2. Usar ejemplo básico.
  3. Usar ejemplo completo (Predeterminado).
- **Ejecución:** 
  1. Compilar: `gcc Problema3/traductor_palabras.c -o traductor.exe`
  2. Ejecutar: `./traductor.exe`

---

### Notas de Instalación y Dependencias
Cada carpeta incluye un archivo `instalar.bat` que verifica e instala automáticamente (vía `winget`) los compiladores necesarios (Python, JDK o GCC).
