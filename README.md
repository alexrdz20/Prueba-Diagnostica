# UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA
**VICERRECTORADO ACADÉMICO**  
**COORDINACIÓN DE INGENIERÍA EN INFORMÁTICA**  
**LENGUAJES Y COMPILADORES**  
Msc. Félix Márquez (fmarquez@e.uneg.edu.ve)  
Periodo lectivo: 2025-II  

## Prueba Diagnóstica

**1)** Dado un número entero no negativo n, a) genere los coeficientes del polinomio (x+1)n, muestre el resultado del polinomio y b) muestre por pasos el cálculo para x dado, f(x) = (x+1)n, según el polinomio generado. Implemente el algoritmo utilizando memoria dinámica. Codificar en dos lenguajes y medir el tiempo de ejecución de cada código para n=100 el resultado escribirlo en archivo txt.

**2)** Dado una cadena C, valide si C se encuentra en notación FEN (Forsyth-Edwards Notation).

**3)** Para un programa escrito en lenguaje C, cargado en una memoria de forma dinámica verifique si existen palabras reservadas en C y tradúzcalas a su equivalente en español.

---

# Resolución de los Problemas (Lo que hice)

Este repositorio contiene la resolución de los problemas planteados para la asignatura. Todos los programas cuentan con **interactividad**, **validación de datos** y **valores por defecto**.

## Estructura de la Prueba
- **Problema1/**: Expansión polinómica (Triángulo de Pascal) en Python y Java.
- **Problema2/**: Validador de notación FEN para ajedrez en Python.
- **Problema3/**: Traductor de palabras reservadas del lenguaje C en C.
- **Defensa/**: Contiene el material o referencia para la defensa.

## Enlace a la Defensa
[Insertar aquí el enlace a tu video de la defensa en YouTube]

---

## Problema 1: Triángulo de Pascal y Expansión Polinómica
Este programa calcula los coeficientes de la expansión polinómica de $(x+1)^n$.

- **Interactividad:** El programa solicitará los valores de `n` (grado) y `x`. Si presionas **Enter** sin escribir, usará `n=100` y `x=2`.
- **Ruta y Ejecución (Python):**
  1. Abrir terminal e ingresar a la carpeta: `cd Problema1`
  2. Ejecutar: `python solucion.py`
- **Ruta y Ejecución (Java):** 
  1. Abrir terminal e ingresar a la carpeta: `cd Problema1`
  2. Compilar: `javac Solucion.java`
  3. Ejecutar: `java Solucion`
- **Resultados:** Los archivos `.txt` se generan automáticamente dentro de la misma carpeta con un formato limpio y profesional detallando el tiempo de ejecución.

## Problema 2: Validación de notación FEN
Valida si una cadena de texto sigue la notación Forsyth-Edwards de ajedrez mediante un bucle interactivo.

- **Interactividad:** Permite elegir entre cargar la cadena FEN desde un archivo de código externo o ingresarla manualmente por teclado.
- **Ruta y Ejecución:** 
  1. Abrir terminal e ingresar a la carpeta: `cd Problema2`
  2. Ejecutar: `python fen_validator.py`

## Problema 3: Traductor de palabras reservadas de C
Analizador léxico optimizado que traduce palabras reservadas de C al español leyendo el código directamente en flujo continuo (`fgetc`), sin saturar la memoria y manteniendo un diseño de código altamente limpio y compacto.

- **Interactividad:** Cuenta con un menú interactivo con limpieza de pantalla (`cls`) para elegir entre:
  1. Ingresar nombre de archivo manualmente.
  2. Usar ejemplo básico.
  3. Usar ejemplo completo.
- **Ruta y Ejecución:** 
  1. Abrir terminal e ingresar a la carpeta: `cd Problema3`
  2. Compilar: `gcc traductor_palabras.c -o traductor.exe`
  3. Ejecutar: `./traductor.exe` (en Windows) o `.\traductor.exe`

---

### Notas de Instalación y Dependencias
Cada carpeta incluye un archivo `instalar.bat` que verifica e instala automáticamente (vía `winget`) los compiladores necesarios (Python, JDK o GCC).
