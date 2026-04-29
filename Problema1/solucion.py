"""
UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA
Asignatura: Lenguajes y Compiladores
Problema 1: Polinomio (x+1)^n usando Triángulo de Pascal

Explicación:
Este código implementa la generación de coeficientes binomiales mediante
el Triángulo de Pascal. Utiliza memoria dinámica (listas de Python) y
precisión arbitraria para manejar n=100.
"""
import time

def generar_fila_pascal(n):
    # Genera la fila n del Triángulo de Pascal
    fila = [1]
    for _ in range(n):
        nueva_fila = [1]
        for i in range(len(fila) - 1):
            nueva_fila.append(fila[i] + fila[i+1])
        nueva_fila.append(1)
        fila = nueva_fila
    return fila

def formatear_polinomio(coeficientes):
    n = len(coeficientes) - 1
    partes = []
    for i, coeff in enumerate(coeficientes):
        potencia = n - i
        termino = ""
        if coeff != 1 or potencia == 0:
            termino += str(coeff)
        if potencia > 0:
            termino += "x"
            if potencia > 1:
                termino += f"^{potencia}"
        partes.append(termino)
    return " + ".join(partes)

def calcular_paso_a_paso(x, n, coeficientes):
    resultado = 0
    pasos = []
    for i, coeff in enumerate(coeficientes):
        potencia = n - i
        valor_termino = coeff * (x ** potencia)
        resultado += valor_termino
        pasos.append(f"{coeff}*({x}^{potencia}) = {valor_termino}")
    return pasos, resultado

def ejecutar_problema1():
    n = 100
    x = 2
    
    # Benchmarking
    inicio = time.perf_counter()
    coeficientes = generar_fila_pascal(n)
    fin = time.perf_counter()
    
    polinomio_str = formatear_polinomio(coeficientes)
    pasos, resultado = calcular_paso_a_paso(x, n, coeficientes)
    
    with open("resultados_python.txt", "w") as f:
        f.write(f"Resultados para n={n}, x={x}\n")
        f.write(f"Tiempo de ejecucion: {fin - inicio:.6f} segundos\n\n")
        f.write(f"Polinomio: {polinomio_str}\n\n")
        f.write("Calculo paso a paso:\n")
        for paso in pasos:
            f.write(paso + "\n")
        f.write(f"\nResultado final: {resultado}\n")

if __name__ == "__main__":
    ejecutar_problema1()
