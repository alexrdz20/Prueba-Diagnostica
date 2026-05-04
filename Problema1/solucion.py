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

def obtener_terminos_polinomio(coeficientes):
    n = len(coeficientes) - 1
    terminos = []
    for i, coeff in enumerate(coeficientes):
        potencia = n - i
        termino = ""
        if coeff != 1 or potencia == 0:
            termino += str(coeff)
        if potencia > 0:
            termino += "x"
            if potencia > 1:
                termino += f"^{potencia}"
        terminos.append(termino)
    return terminos

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
    print("--- CONFIGURACIÓN DEL POLINOMIO ---")
    
    # Entrada para n
    while True:
        entrada_n = input("Ingrese el valor de n (Enter para 100): ").strip()
        if not entrada_n:
            n = 100
            break
        try:
            n = int(entrada_n)
            if n >= 0: break
            print("Error: n debe ser un número no negativo.")
        except ValueError:
            print("Error: Entrada inválida. Ingrese un número entero.")

    # Entrada para x
    while True:
        entrada_x = input("Ingrese el valor de x para evaluar f(x) (Enter para 2): ").strip()
        if not entrada_x:
            x = 2
            break
        try:
            x = int(entrada_x)
            break
        except ValueError:
            print("Error: Entrada inválida. Ingrese un número entero.")
    
    # Benchmarking
    inicio = time.perf_counter()
    coeficientes = generar_fila_pascal(n)
    fin = time.perf_counter()
    
    terminos = obtener_terminos_polinomio(coeficientes)
    pasos, resultado = calcular_paso_a_paso(x, n, coeficientes)
    
    with open("resultados_python.txt", "w") as f:
        linea80 = "="*80 + "\n"
        linea_sep = "-"*80 + "\n"
        
        f.write(linea80)
        f.write("           RESULTADOS DEL CALCULO POLINOMIAL (Problema 1)\n")
        f.write(linea80)
        f.write(f"CONFIGURACION:\n")
        f.write(f"  Grado (n) : {n}\n")
        f.write(f"  Valor (x) : {x}\n")
        f.write(linea_sep)
        f.write(f"TIEMPO DE EJECUCION: {fin - inicio:.6f} segundos\n")
        f.write(linea_sep + "\n")
        
        f.write(f"RESULTADO FINAL:\n")
        f.write(f"{resultado}\n\n")
        f.write(linea80)

if __name__ == "__main__":
    ejecutar_problema1()
