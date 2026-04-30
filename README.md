# Prueba de lenguajes y compiladores

Este repositorio contiene la resolución de los problemas planteados para la asignatura.

## Estructura de la prueba
- **Problema1/**: Expansión polinómica (Triángulo de Pascal) en Python y Java.
- **Problema2/**: Validador de notación FEN para ajedrez (Python).
- **Problema3/**: Traductor de palabras reservadas del lenguaje C (C).
- **Defensa/**: Contiene el material o referencia para la defensa.

## Enlace a la Defensa
[Insertar aquí el enlace a tu video de la defensa]

---

## Problema 1: Triángulo de Pascal y Expansión Polinómica
Este programa calcula los coeficientes de la expansión polinómica de (x+1)^n.

- **Instalador:** `Problema1/instalar.bat` (Verifica/Instala Python y Java JDK).
- **Ejecución:**
  - Python: `python Problema1/solucion.py`
  - Java: `javac Problema1/Solucion.java` y `java Solucion`

## Problema 2: Validación de notación FEN
Valida si una cadena de texto sigue la notación Forsyth-Edwards de ajedrez.

- **Instalador:** `Problema2/instalar.bat` (Verifica/Instala Python).
- **Ejecución:** `python Problema2/fen_validator.py`

## Problema 3: Traductor de palabras reservadas de C
Analizador léxico que traduce palabras reservadas de C al español.

- **Instalador:** `Problema3/instalar.bat` (Verifica/Instala GCC).
- **Ejecución:** 
  1. `gcc Problema3/traductor_palabras.c -o traductor.exe`
  2. `./traductor.exe ejemplo_completo.c`

---

### Nota sobre los scripts de instalación (.bat)
Cada carpeta incluye un archivo `instalar.bat`. Estos son scripts de automatización que:
1. Verifican si el lenguaje/compilador necesario está instalado en su sistema.
2. Si no lo está, intentan instalar automáticamente la dependencia mediante el gestor de paquetes de Windows (`winget`).
3. Mantienen la ventana abierta al finalizar para que pueda confirmar el éxito del proceso.
