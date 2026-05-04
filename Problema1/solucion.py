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
import os

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
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n==================================================")
        print(" EXPANSION POLINOMIAL (TRIANGULO DE PASCAL) - PYTHON")
        print("==================================================")
        print("  [1] Usar valores por defecto (n=100, x=2)")
        print("  [2] Ingresar valores manualmente")
        print("  [0] Salir")
        print("--------------------------------------------------")
        
        opcion = input("Seleccione una opcion > ").strip()
        
        if opcion == "0":
            print("Saliendo...")
            break
        
        n, x = 100, 2 # Valores base

        if opcion == "2":
            print("\n--- CONFIGURACION MANUAL ---")
            while True:
                entrada_n = input("Ingrese el valor de n: ").strip()
                try:
                    n = int(entrada_n)
                    if n >= 0: break
                    print("Error: n debe ser >= 0.")
                except ValueError:
                    print("Error: Ingrese un numero entero.")

            while True:
                entrada_x = input("Ingrese el valor de x: ").strip()
                try:
                    x = int(entrada_x)
                    break
                except ValueError:
                    print("Error: Ingrese un numero entero.")
        elif opcion != "1":
            print("[!] Opcion no valida.")
            continue

        # Proceso de calculo
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n[INFO] Calculando para n={n}, x={x}...")
        inicio = time.perf_counter()
        coeficientes = generar_fila_pascal(n)
        fin = time.perf_counter()
        
        pasos, resultado = calcular_paso_a_paso(x, n, coeficientes)
        
        with open("resultados_python.txt", "w") as f:
            linea80 = "="*80 + "\n"
            linea_sep = "-"*80 + "\n"
            f.write(linea80)
            f.write("           RESULTADOS DEL CALCULO POLINOMIAL (Problema 1)\n")
            f.write(linea80)
            f.write(f"CONFIGURACION:\n  Grado (n) : {n}\n  Valor (x) : {x}\n")
            f.write(linea_sep)
            f.write(f"TIEMPO DE EJECUCION: {fin - inicio:.6f} segundos\n")
            f.write(linea_sep + "\n")
            f.write(f"RESULTADO FINAL:\n{resultado}\n\n")
            f.write(linea80)
        
        print(f"[OK] Completado en {fin - inicio:.6f} s. Revisa 'resultados_python.txt'")
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    ejecutar_problema1()
